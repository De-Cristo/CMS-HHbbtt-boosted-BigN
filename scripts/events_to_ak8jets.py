import numpy as np
import awkward
import uproot as u
import os
import time
import argparse
import json
import ROOT as R

from tqdm import tqdm
import multiprocessing
from multiprocessing import Pool

import gc

def track_var_to_flat(arr, idx_low, idx_high):
    return awkward.to_awkward0(awkward.Array( [[ ev[ka : kb] for ka, kb in zip(kidx_a, kidx_b)] for ev, kidx_a, kidx_b in zip(arr, idx_low, idx_high)])).flatten(axis=0)

parser = argparse.ArgumentParser()
parser.add_argument("--InJson", "-i", dest='inJson', default='./AutoMake_Run2_2018_MC_BigNtuplewithWeight.json', type=str, help="Input json-file")
parser.add_argument("--OutDir", "-o", dest='outDir', default='./AK8based_Out_625/', type=str, help="output direction")
args = parser.parse_args()

base_dir = args.outDir
os.makedirs(base_dir, exist_ok = True)

# process_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
# process_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
# process_list = ['VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep']
process_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep']
# process_list = ['SMHH']


interest_variables = [
                      'ak8jets_SoftDropMass',
                      'bParticleNetTauAK8JetTags_probHtt','bParticleNetTauAK8JetTags_probHtm','bParticleNetTauAK8JetTags_probHte',
                      'bParticleNetTauAK8JetTags_probHbb','bParticleNetTauAK8JetTags_probHcc', 'bParticleNetTauAK8JetTags_probHqq','bParticleNetTauAK8JetTags_probHgg',
                      'bParticleNetTauAK8JetTags_probQCD0hf','bParticleNetTauAK8JetTags_probQCD1hf','bParticleNetTauAK8JetTags_probQCD2hf',
                      'bParticleNetTauAK8JetTags_masscorr',
                     ]

# interest_variables = ['ak8jets_px']

helper_variables = ['ak8jets_px','ak8jets_py','ak8jets_pz','ak8jets_e',
                    'genpart_px', 'genpart_py', 'genpart_pz', 'genpart_e', 'genpart_pdg', 'genpart_flags', 'genpart_TauGenDecayMode',
                    'genjet_px', 'genjet_py', 'genjet_pz', 'genjet_e', 'genjet_partonFlavour', 'genjet_hadronFlavour',
                    'genpart_HMothInd', 'genpart_ZMothInd', 'daughters_byDeepTau2017v2p1VSjetraw',
                    'PDGIdDaughters', 'daughters_isTauMatched', 'daughters_px', 'daughters_py', 'daughters_pz', 'daughters_e',
                    'aMCatNLOweight'
                   ]


def calc_ak8jets_pT(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e):
    return R.Math.PxPyPzEVector(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e).Pt()

def calc_ak8jets_eta(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e):
    return R.Math.PxPyPzEVector(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e).Eta()

def ak8Jets_mass_corr(ak8jets_SoftDropMass, bParticleNetTauAK8JetTags_masscorr):
    return ak8jets_SoftDropMass * bParticleNetTauAK8JetTags_masscorr

def calc_prob_Htt(bParticleNetTauAK8JetTags_probHtt, bParticleNetTauAK8JetTags_probHtm, bParticleNetTauAK8JetTags_probHte,
                  bParticleNetTauAK8JetTags_probQCD0hf, bParticleNetTauAK8JetTags_probQCD1hf, bParticleNetTauAK8JetTags_probQCD2hf
                 ):
    if (bParticleNetTauAK8JetTags_probHtt+bParticleNetTauAK8JetTags_probHtm+bParticleNetTauAK8JetTags_probHte+bParticleNetTauAK8JetTags_probQCD0hf+bParticleNetTauAK8JetTags_probQCD1hf+bParticleNetTauAK8JetTags_probQCD2hf) == 0:
        return 0.
    else:
        return float(bParticleNetTauAK8JetTags_probHtt/(bParticleNetTauAK8JetTags_probHtt+bParticleNetTauAK8JetTags_probHtm+bParticleNetTauAK8JetTags_probHte+bParticleNetTauAK8JetTags_probQCD0hf+bParticleNetTauAK8JetTags_probQCD1hf+bParticleNetTauAK8JetTags_probQCD2hf))
    
def check_bit(number, bitpos):
    res = number & (1 << bitpos)
    return bool(res)

def process_event(args):
    # Unpack the arguments
    evt_idx, ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e, \
    genpart_px, genpart_py, genpart_pz, genpart_e, \
    genpart_pdg, genpart_flags, \
    genjet_px, genjet_py, genjet_pz, genjet_e, \
    genjet_partonFlavour, genjet_hadronFlavour, genpart_TauGenDecayMode,\
    genpart_HMothInd, genpart_ZMothInd, \
    PDGIdDaughters, daughters_isTauMatched, \
    daughters_px, daughters_py, daughters_pz, daughters_e, daughters_byDeepTau2017v2p1VSjetraw = args

    ak8_obj = R.TLorentzVector()
    gen_obj = R.TLorentzVector()
    genjet_obj = R.TLorentzVector()
    daughter_obj = R.TLorentzVector()

    sub_arr_tau_matched = []
    sub_arr_emu_matched = []
    sub_arr_hav_matched = []
    sub_arr_hps_matched = []
    sub_arr_hps_matched_test = []
    
    sub_arr_hps1_Pt = []
    sub_arr_hps2_Pt = []
    sub_arr_hps1_E = []
    sub_arr_hps2_E = []
    sub_arr_hps1_Eta = []
    sub_arr_hps2_Eta = []
    sub_arr_hps1_Phi = []
    sub_arr_hps2_Phi = []
    sub_arr_hps1_M = []
    sub_arr_hps2_M = []
    sub_arr_hps1_DeepTauVSJets = []
    sub_arr_hps2_DeepTauVSJets = []

    for ak8_obj_idx in range(len(ak8jets_px)):
        ak8_obj.SetPxPyPzE(ak8jets_px[ak8_obj_idx], ak8jets_py[ak8_obj_idx], ak8jets_pz[ak8_obj_idx], ak8jets_e[ak8_obj_idx])

        tau_matched = 0
        for gen_obj_idx in range(len(genpart_px)):
            gen_obj.SetPxPyPzE(genpart_px[gen_obj_idx], genpart_py[gen_obj_idx], genpart_pz[gen_obj_idx], genpart_e[gen_obj_idx])
            # DeltaR < 0.8; obj is tau; genflag 13 == 1 is last copy; TauGenDecayMode == 2 is hadronic decay.
            if ak8_obj.DeltaR(gen_obj) < 0.8 \
                and abs(genpart_pdg[gen_obj_idx]) == 15 \
                and (genpart_flags[gen_obj_idx] & (1 << 13)) \
                and (genpart_TauGenDecayMode[gen_obj_idx] == 2):
                tau_matched += 1
                
        emu_matched = 0
        for gen_obj_idx in range(len(genpart_px)):
            gen_obj.SetPxPyPzE(genpart_px[gen_obj_idx], genpart_py[gen_obj_idx], genpart_pz[gen_obj_idx], genpart_e[gen_obj_idx])
            if ak8_obj.DeltaR(gen_obj) < 0.8 \
                and (abs(genpart_pdg[gen_obj_idx]) == 11 or abs(genpart_pdg[gen_obj_idx]) == 13) \
                and (genpart_flags[gen_obj_idx] & (1 << 13))\
                and (genpart_HMothInd[gen_obj_idx] > -1 or genpart_ZMothInd[gen_obj_idx] > -1):
                emu_matched += 1

        hav_matched = 0
        for genjet_obj_idx in range(len(genjet_px)):
            genjet_obj.SetPxPyPzE(genjet_px[genjet_obj_idx], genjet_py[genjet_obj_idx], genjet_pz[genjet_obj_idx], genjet_e[genjet_obj_idx])
            if ak8_obj.DeltaR(genjet_obj) < 0.8 and (abs(genjet_hadronFlavour[genjet_obj_idx]) == 4 or abs(genjet_hadronFlavour[genjet_obj_idx]) == 5):
                hav_matched += 1
                
        hps_matched = 0
        hps_matched_idx = []
        hps_matched_pt = []
        
        hps1_Pt = -99.
        hps2_Pt = -99.
        hps1_E = -99.
        hps2_E = -99.
        hps1_Eta = -99.
        hps2_Eta = -99.
        hps1_Phi = -99.
        hps2_Phi = -99.
        hps1_M = -99.
        hps2_M = -99.
        hps1_DeepTauVSJets = -99.
        hps2_DeepTauVSJets = -99
        
        for daughter_obj_idx in range(len(PDGIdDaughters)):
            daughter_obj.SetPxPyPzE(daughters_px[daughter_obj_idx], daughters_py[daughter_obj_idx], daughters_pz[daughter_obj_idx], daughters_e[daughter_obj_idx])
            # if ak8_obj.DeltaR(daughter_obj) < 0.8 and (abs(PDGIdDaughters[daughter_obj_idx])!=11 and abs(PDGIdDaughters[daughter_obj_idx])!=13):
            if ak8_obj.DeltaR(daughter_obj) < 0.8 and (abs(PDGIdDaughters[daughter_obj_idx])==15):
                hps_matched += 1
                hps_matched_idx.append(daughter_obj_idx)
                hps_matched_pt.append(daughter_obj.Pt())
                
        if hps_matched == 0:
            pass
        elif hps_matched == 1:
            daughter_obj_idx = hps_matched_idx[0]
            daughter_obj.SetPxPyPzE(daughters_px[daughter_obj_idx], daughters_py[daughter_obj_idx], daughters_pz[daughter_obj_idx], daughters_e[daughter_obj_idx])
            hps1_Pt = daughter_obj.Pt()
            hps1_E = daughter_obj.E()
            hps1_Eta = daughter_obj.Eta()
            hps1_Phi = daughter_obj.Phi()
            hps1_M = daughter_obj.M()
            hps1_DeepTauVSJets = daughters_byDeepTau2017v2p1VSjetraw[daughter_obj_idx]
        else:                
            sorted_lists = sorted(zip(hps_matched_pt, hps_matched_idx))
            hps_matched_pt, hps_matched_idx = zip(*sorted_lists)
            hps_matched_idx = list(reversed(hps_matched_idx))
            hps_count = 0
            for daughter_obj_idx in range(len(hps_matched_idx)):
                daughter_obj.SetPxPyPzE(daughters_px[daughter_obj_idx], daughters_py[daughter_obj_idx], daughters_pz[daughter_obj_idx], daughters_e[daughter_obj_idx])
                hps_count += 1
                if hps_count == 1:
                    hps1_Pt = daughter_obj.Pt()
                    hps1_E = daughter_obj.E()
                    hps1_Eta = daughter_obj.Eta()
                    hps1_Phi = daughter_obj.Phi()
                    hps1_M = daughter_obj.M()
                    hps1_DeepTauVSJets = daughters_byDeepTau2017v2p1VSjetraw[daughter_obj_idx]
                elif hps_count == 2:
                    hps2_Pt = daughter_obj.Pt()
                    hps2_E = daughter_obj.E()
                    hps2_Eta = daughter_obj.Eta()
                    hps2_Phi = daughter_obj.Phi()
                    hps2_M = daughter_obj.M()
                    hps2_DeepTauVSJets = daughters_byDeepTau2017v2p1VSjetraw[daughter_obj_idx]
                else:
                    break

        
        if hps_matched == 1:
            hps1_Pt = daughter_obj.Pt()
            hps1_E = daughter_obj.E()
            hps1_Eta = daughter_obj.Eta()
            hps1_Phi = daughter_obj.Phi()
            hps1_M = daughter_obj.M()
            hps1_DeepTauVSJets = daughters_byDeepTau2017v2p1VSjetraw[daughter_obj_idx]
        if hps_matched == 2:
            hps2_Pt = daughter_obj.Pt()
            hps2_E = daughter_obj.E()
            hps2_Eta = daughter_obj.Eta()
            hps2_Phi = daughter_obj.Phi()
            hps2_M = daughter_obj.M()
            hps2_DeepTauVSJets = daughters_byDeepTau2017v2p1VSjetraw[daughter_obj_idx]
        
        hps_matched_test = 0
        for daughter_obj_idx in range(len(daughters_isTauMatched)):
            daughter_obj.SetPxPyPzE(daughters_px[daughter_obj_idx], daughters_py[daughter_obj_idx], daughters_pz[daughter_obj_idx], daughters_e[daughter_obj_idx])
            if ak8_obj.DeltaR(daughter_obj) < 0.8 and (daughters_isTauMatched[daughter_obj_idx]==1) :
                hps_matched_test += 1

        sub_arr_tau_matched.append(tau_matched)
        sub_arr_emu_matched.append(emu_matched)
        sub_arr_hav_matched.append(hav_matched)
        sub_arr_hps_matched.append(hps_matched)
        sub_arr_hps_matched_test.append(hps_matched_test)
        
        sub_arr_hps1_Pt.append(hps1_Pt)
        sub_arr_hps1_E.append(hps1_E)
        sub_arr_hps1_Eta.append(hps1_Eta)
        sub_arr_hps1_Phi.append(hps1_Phi)
        sub_arr_hps1_M.append(hps1_M)
        sub_arr_hps1_DeepTauVSJets.append(hps1_DeepTauVSJets)
        sub_arr_hps2_Pt.append(hps2_Pt)
        sub_arr_hps2_E.append(hps2_E)
        sub_arr_hps2_Eta.append(hps2_Eta)
        sub_arr_hps2_Phi.append(hps2_Phi)
        sub_arr_hps2_M.append(hps2_M)
        sub_arr_hps2_DeepTauVSJets.append(hps2_DeepTauVSJets)
        
    return sub_arr_tau_matched, sub_arr_emu_matched, sub_arr_hav_matched, sub_arr_hps_matched, sub_arr_hps_matched_test, \
           sub_arr_hps1_Pt, sub_arr_hps1_E, sub_arr_hps1_Eta, sub_arr_hps1_Phi, sub_arr_hps1_M, sub_arr_hps1_DeepTauVSJets, \
           sub_arr_hps2_Pt, sub_arr_hps2_E, sub_arr_hps2_Eta, sub_arr_hps2_Phi, sub_arr_hps2_M, sub_arr_hps2_DeepTauVSJets

def match_ak8jets_with_tau(ARR_ak8jets_px, ARR_ak8jets_py, ARR_ak8jets_pz, ARR_ak8jets_e, \
                           ARR_genpart_px, ARR_genpart_py, ARR_genpart_pz, ARR_genpart_e, \
                           ARR_genpart_pdg, ARR_genpart_flags, \
                           ARR_genjet_px, ARR_genjet_py, ARR_genjet_pz, ARR_genjet_e, \
                           ARR_genjet_partonFlavour, ARR_genjet_hadronFlavour, ARR_genpart_TauGenDecayMode, \
                           ARR_genpart_HMothInd, ARR_genpart_ZMothInd, \
                           ARR_PDGIdDaughters, ARR_daughters_isTauMatched, \
                           ARR_daughters_px, ARR_daughters_py, ARR_daughters_pz, ARR_daughters_e, ARR_daughters_byDeepTau2017v2p1VSjetraw
                          ):
    num_events = len(ARR_ak8jets_px)
    # print('there are {} events'.format(num_events))

    arr_tau_matched = []
    arr_emu_matched = []
    arr_hav_matched = []
    arr_hps_matched = []
    arr_hps_matched_test = []
    
    arr_hps1_Pt = []
    arr_hps1_E = []
    arr_hps1_Eta = []
    arr_hps1_Phi = []
    arr_hps1_M = []
    arr_hps1_DeepTauVSJets = []
    arr_hps2_Pt = []
    arr_hps2_E = []
    arr_hps2_Eta = []
    arr_hps2_Phi = []
    arr_hps2_M = []
    arr_hps2_DeepTauVSJets = []
    
    # Create a list of arguments for each event
    event_args = []
    for evt_idx in range(num_events):
        # Create a list of arguments for each event
        event_args.append((evt_idx,
                           ARR_ak8jets_px[evt_idx],
                           ARR_ak8jets_py[evt_idx],
                           ARR_ak8jets_pz[evt_idx],
                           ARR_ak8jets_e[evt_idx],
                           ARR_genpart_px[evt_idx],
                           ARR_genpart_py[evt_idx],
                           ARR_genpart_pz[evt_idx],
                           ARR_genpart_e[evt_idx],
                           ARR_genpart_pdg[evt_idx],
                           ARR_genpart_flags[evt_idx],
                           ARR_genjet_px[evt_idx],
                           ARR_genjet_py[evt_idx],
                           ARR_genjet_pz[evt_idx],
                           ARR_genjet_e[evt_idx],
                           ARR_genjet_partonFlavour[evt_idx],
                           ARR_genjet_hadronFlavour[evt_idx],
                           ARR_genpart_TauGenDecayMode[evt_idx],
                           ARR_genpart_HMothInd[evt_idx],
                           ARR_genpart_ZMothInd[evt_idx],
                           ARR_PDGIdDaughters[evt_idx],
                           ARR_daughters_isTauMatched[evt_idx],
                           ARR_daughters_px[evt_idx],
                           ARR_daughters_py[evt_idx],
                           ARR_daughters_pz[evt_idx],
                           ARR_daughters_e[evt_idx],
                           ARR_daughters_byDeepTau2017v2p1VSjetraw[evt_idx]
                          ),
                         )

    # Process events in parallel using multithreading
    # with Pool(10) as pool:
    #     results = list(tqdm(pool.imap(process_event, event_args), total=num_events))
    
    results = []
    for _args in event_args:
        results.append(process_event(_args))
    
    # Unpack the results
    for res in results:
        arr_tau_matched.append(res[0])
        arr_emu_matched.append(res[1])
        arr_hav_matched.append(res[2])
        arr_hps_matched.append(res[3])
        arr_hps_matched_test.append(res[4])
        arr_hps1_Pt.append(res[5])
        arr_hps1_E.append(res[6])
        arr_hps1_Eta.append(res[7])
        arr_hps1_Phi.append(res[8])
        arr_hps1_M.append(res[9])
        arr_hps1_DeepTauVSJets.append(res[10])
        arr_hps2_Pt.append(res[11])
        arr_hps2_E.append(res[12])
        arr_hps2_Eta.append(res[13])
        arr_hps2_Phi.append(res[14])
        arr_hps2_M.append(res[15])
        arr_hps2_DeepTauVSJets.append(res[16])

    return awkward.to_awkward0(awkward.Array(arr_tau_matched)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_emu_matched)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hav_matched)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps_matched)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps_matched_test)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Pt)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_E)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Eta)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Phi)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_M)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps1_DeepTauVSJets)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Pt)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_E)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Eta)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Phi)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_M)).flatten(axis=0), \
           awkward.to_awkward0(awkward.Array(arr_hps2_DeepTauVSJets)).flatten(axis=0)

def calc_true_weight(ARR_aMCatNLOweight, ARR_ak8jets_px, XS, lumi, sumOfweights):
    arr_weights = ARR_aMCatNLOweight * XS * lumi / sumOfweights
    arr_weights_flat = np.concatenate( np.array([np.repeat(weight, len(ak8jet)) for weight, ak8jet in zip(arr_weights, ARR_ak8jets_px)], dtype=object) )
    
    return arr_weights_flat

with open(args.inJson, 'r') as f:
    data = f.read()
    fileset = json.loads(data)
    
for process in process_list:
    print(process)
    os.makedirs(base_dir+'/'+process, exist_ok = True)
    
    def process_file(file):
        with u.open(file, num_workers = 4)["HTauTauTree"]["HTauTauTree"] as event_tree:
            branch_dict = {}
            branch_dict_helper = {}
            ak8_file = u.recreate( os.path.join( base_dir+'/'+process+'/', "{}".format(file.split("/")[-1]) ), compression=u.ZLIB(4) )
            for variable in interest_variables:
                arr = awkward.to_awkward0( awkward.Array(event_tree[variable].array()) ).flatten(axis=0)
                branch_dict[variable] = arr

            for variable in helper_variables:
                arr = awkward.to_awkward0( awkward.Array(event_tree[variable].array()) )
                branch_dict_helper[variable] = arr
                
            vectorized_function = np.vectorize(calc_ak8jets_pT)
            result = vectorized_function(branch_dict_helper['ak8jets_px'].flatten(axis=0), branch_dict_helper['ak8jets_py'].flatten(axis=0), branch_dict_helper['ak8jets_pz'].flatten(axis=0), branch_dict_helper['ak8jets_e'].flatten(axis=0))
            branch_dict['ak8jets_Pt'] = result
            
            vectorized_function = np.vectorize(calc_ak8jets_eta)
            result = vectorized_function(branch_dict_helper['ak8jets_px'].flatten(axis=0), branch_dict_helper['ak8jets_py'].flatten(axis=0), branch_dict_helper['ak8jets_pz'].flatten(axis=0), branch_dict_helper['ak8jets_e'].flatten(axis=0))
            branch_dict['ak8jets_Eta'] = result

            vectorized_function = np.vectorize(ak8Jets_mass_corr)
            result = vectorized_function(branch_dict['ak8jets_SoftDropMass'], branch_dict['bParticleNetTauAK8JetTags_masscorr'])
            branch_dict['ak8jets_Mass'] = result
            
            vectorized_function = np.vectorize(calc_prob_Htt)
            result = vectorized_function(branch_dict['bParticleNetTauAK8JetTags_probHtt'], branch_dict['bParticleNetTauAK8JetTags_probHtm'], branch_dict['bParticleNetTauAK8JetTags_probHte'],branch_dict['bParticleNetTauAK8JetTags_probQCD0hf'],branch_dict['bParticleNetTauAK8JetTags_probQCD1hf'],branch_dict['bParticleNetTauAK8JetTags_probQCD2hf'])
            branch_dict['ak8jets_probHtt'] = result

            branch_dict['match_gen_tau'], \
            branch_dict['match_gen_emu'], \
            branch_dict['match_gen_hav'], \
            branch_dict['match_hps_tau'], \
            branch_dict['match_hps_tau_test'],\
            branch_dict['hps_tau1_Pt'],\
            branch_dict['hps_tau1_E'],\
            branch_dict['hps_tau1_Eta'],\
            branch_dict['hps_tau1_Phi'],\
            branch_dict['hps_tau1_M'],\
            branch_dict['hps_tau1_DeepTauVSJets'],\
            branch_dict['hps_tau2_Pt'],\
            branch_dict['hps_tau2_E'],\
            branch_dict['hps_tau2_Eta'],\
            branch_dict['hps_tau2_Phi'],\
            branch_dict['hps_tau2_M'], \
            branch_dict['hps_tau2_DeepTauVSJets'] = match_ak8jets_with_tau( \
                    branch_dict_helper['ak8jets_px'], branch_dict_helper['ak8jets_py'], branch_dict_helper['ak8jets_pz'], branch_dict_helper['ak8jets_e'], \
                    branch_dict_helper['genpart_px'], branch_dict_helper['genpart_py'], branch_dict_helper['genpart_pz'], branch_dict_helper['genpart_e'], \
                    branch_dict_helper['genpart_pdg'], branch_dict_helper['genpart_flags'],\
                    branch_dict_helper['genjet_px'], branch_dict_helper['genjet_py'], branch_dict_helper['genjet_pz'], branch_dict_helper['genjet_e'], \
                    branch_dict_helper['genjet_partonFlavour'], branch_dict_helper['genjet_hadronFlavour'], branch_dict_helper['genpart_TauGenDecayMode'],\
                    branch_dict_helper['genpart_HMothInd'], branch_dict_helper['genpart_ZMothInd'], \
                    branch_dict_helper['PDGIdDaughters'], branch_dict_helper['daughters_isTauMatched'], \
                    branch_dict_helper['daughters_px'], branch_dict_helper['daughters_py'], branch_dict_helper['daughters_pz'], branch_dict_helper['daughters_e'], \
                    branch_dict_helper['daughters_byDeepTau2017v2p1VSjetraw'],
                )
                        
            XS = fileset[process][1]
            lumi = fileset[process][2]
            sumOfweights = fileset[process][3]
            branch_dict['true_weight'] = calc_true_weight(branch_dict_helper['aMCatNLOweight'], branch_dict_helper['ak8jets_px'], XS, lumi, sumOfweights)

            ak8_file["ak8tree"] = branch_dict
            # ak8_file["ak8tree"].show()

            del event_tree
            del ak8_file
            del branch_dict
            
            gc.collect()
            return 0
        
    
    # for process_ in fileset[process][0][:1]:
    #     process_file(process_)
        
    num_processes = multiprocessing.cpu_count()
    pool = Pool(round(num_processes*0.8))
    print('using {} cores'.format(round(num_processes*0.8)))
    results = []
    with tqdm(total=len(fileset[process][0])) as pbar:
        for result in tqdm(pool.imap(process_file, fileset[process][0])):
            results.append(result)
            pbar.update()
            
    pool.close()
    pool.join()
          
    ## with Pool(round(num_processes*0.8)) as pool:
    ##     results = pool.map(process_file, fileset[process][0])
          
        
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

from python.ur_utils import \
calc_obj_pT,calc_obj_pT_vec,calc_mass_corr,calc_obj_eta,calc_obj_phi,\
calc_prob_Htt,check_bit,HLT_path_checker,calc_true_weight,lepton_type_checker,\
good_AK8_checker, FatJet_Lepton_Matcher, process_event, match_ak8jets_with_tau, \
channel_tagger, higgs_tagger

from configs.plot_config_bigNtuple import ak8_interest_variables,helper_variables,event_interest_variables,lepton_interest_variables

parser = argparse.ArgumentParser()
parser.add_argument("--InJson", "-i", dest='inJson', default='./AutoMake_Run2_2018_MC_BigNtuplewithWeight.json', type=str, help="Input json-file")
parser.add_argument("--OutDir", "-o", dest='outDir', default='./MixBased_Out_20231221/', type=str, help="output direction")
args = parser.parse_args()

base_dir = args.outDir
os.makedirs(base_dir, exist_ok = True)

# process_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
process_list = ['TTbarSemi']
# process_list = ['VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi'78%, 'TTbarDiLep']
# process_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep']
# process_list = ['SMHH']

with open(args.inJson, 'r') as f:
    data = f.read()
    fileset = json.loads(data)
    
for process in process_list:
    print(process)
    os.makedirs(base_dir+'/'+process, exist_ok = True)
    
    def process_file(file):
        with u.open(file, num_workers = 4)["HTauTauTree"]["HTauTauTree"] as event_tree:
            event_branch_dict = {}
            event_helper_branch_dict = {}
            lepton_branch_dict = {}
            lepton_helper_branch_dict = {}
            ak8_branch_dict = {}
            ak8_helper_branch_dict = {}
        
            out_file = u.recreate( os.path.join( base_dir+'/'+process+'/', "{}".format(file.split("/")[-1]) ), compression=u.ZLIB(4) )
                
            ak8_jagged_arr = awkward.Array(event_tree['ak8jets_px'].array())
            lepton_jagged_arr = awkward.Array(event_tree['PDGIdDaughters'].array())
            
            list_ak8evtidx = [ [i]*len(ak8_jagged_arr[i]) for i in range(len(ak8_jagged_arr)) ]
            list_lepevtidx = [ [i]*len(lepton_jagged_arr[i]) for i in range(len(lepton_jagged_arr)) ]
            list_ak8idx = [ i for i in range(len(awkward.to_awkward0(ak8_jagged_arr).flatten())) ]
            list_lepidx = [ i for i in range(len(awkward.to_awkward0(lepton_jagged_arr).flatten())) ]
            list_evtidx = [ i for i in range(len(ak8_jagged_arr)) ]
            list_evtnlep = [ len(lepton_jagged_arr[i]) for i in range(len(lepton_jagged_arr)) ]
            list_evtnak8 = [ len(ak8_jagged_arr[i]) for i in range(len(ak8_jagged_arr)) ]
            
            event_branch_dict['evt_index'] = awkward.Array(list_evtidx)
            event_branch_dict['evtnlep'] = awkward.Array(list_evtnlep)
            event_branch_dict['evtnak8'] = awkward.Array(list_evtnak8)
            
            lepton_branch_dict['lep_evt_index'] = awkward.to_awkward0( awkward.Array(list_lepevtidx) ).flatten()
            lepton_branch_dict['lep_index'] = awkward.Array(list_lepidx)
            
            ak8_branch_dict['ak8_evt_index'] = awkward.to_awkward0( awkward.Array(list_ak8evtidx) ).flatten()
            ak8_branch_dict['ak8_index'] = awkward.Array(list_ak8idx)
            
            for variable in ak8_interest_variables:
                arr = awkward.to_awkward0( awkward.Array(event_tree[variable].array()) ).flatten()
                ak8_branch_dict[variable] = arr
                
            for variable in lepton_interest_variables:
                arr = awkward.to_awkward0( awkward.Array(event_tree[variable].array()) ).flatten()
                lepton_branch_dict[variable] = arr
                
            for variable in event_interest_variables:
                arr = awkward.to_awkward0( awkward.Array(event_tree[variable].array()) )
                event_branch_dict[variable] = arr

            for variable in helper_variables:
                arr = awkward.Array(event_tree[variable].array())
                event_helper_branch_dict[variable] = awkward.to_awkward0(arr)
                lepton_helper_branch_dict[variable] = awkward.to_awkward0(arr)
                ak8_helper_branch_dict[variable] = awkward.to_awkward0(arr)
                
            ### calculating basic event based parameters
            # for parameter PassHLTPath [0, 0, 0], if 1 means pass the HLT path. the order is [Muon Path, Electron Path, Hadronic(Jet/Met) Path]
            vectorized_function = np.vectorize(HLT_path_checker)
            result = vectorized_function(
                event_helper_branch_dict['triggerbit'])
            event_branch_dict['PassMuonPath'], event_branch_dict['PassElectronPath'], event_branch_dict['PassHadronicPath'] = result
            
            XS = fileset[process][1]
            lumi = fileset[process][2]
            sumOfweights = fileset[process][3]
            event_branch_dict['Weight'] = calc_true_weight(event_helper_branch_dict['aMCatNLOweight'], XS, lumi, sumOfweights)
            
            ### calculating Lepton parameters
            vectorized_function = np.vectorize(calc_obj_pT)
            result = vectorized_function(
                lepton_helper_branch_dict['daughters_px'].flatten(),
                lepton_helper_branch_dict['daughters_py'].flatten(),
                lepton_helper_branch_dict['daughters_pz'].flatten(),
                lepton_helper_branch_dict['daughters_e'].flatten())
            lepton_branch_dict['Lepton_Pt'] = result
            
            vectorized_function = np.vectorize(calc_obj_eta)
            result = vectorized_function(
                lepton_helper_branch_dict['daughters_px'].flatten(), 
                lepton_helper_branch_dict['daughters_py'].flatten(), 
                lepton_helper_branch_dict['daughters_pz'].flatten(), 
                lepton_helper_branch_dict['daughters_e'].flatten())
            lepton_branch_dict['Lepton_Eta'] = result
            
            vectorized_function = np.vectorize(calc_obj_phi)
            result = vectorized_function(
                lepton_helper_branch_dict['daughters_px'].flatten(),
                lepton_helper_branch_dict['daughters_py'].flatten(),
                lepton_helper_branch_dict['daughters_pz'].flatten(),
                lepton_helper_branch_dict['daughters_e'].flatten())
            lepton_branch_dict['Lepton_Phi'] = result
            
            vectorized_function = np.vectorize(lepton_type_checker)
            result = vectorized_function(
                lepton_branch_dict['Lepton_Pt'],
                lepton_branch_dict['Lepton_Eta'],
                lepton_helper_branch_dict['dxy'].flatten(),
                lepton_helper_branch_dict['dz'].flatten(),
                lepton_helper_branch_dict['daughters_muonID'].flatten(),
                lepton_helper_branch_dict['daughters_iseleWP90'].flatten(),
                lepton_helper_branch_dict['daughters_iseleNoIsoWP90'].flatten())
            lepton_branch_dict['GoodMuon'], lepton_branch_dict['VetoMuon'], lepton_branch_dict['GoodElectron'], lepton_branch_dict['VetoElectron'] = result
            
            ### calculating AK8Jets parameters
            vectorized_function = np.vectorize(calc_obj_pT)
            result = vectorized_function(
                ak8_helper_branch_dict['ak8jets_px'].flatten(), 
                ak8_helper_branch_dict['ak8jets_py'].flatten(), 
                ak8_helper_branch_dict['ak8jets_pz'].flatten(), 
                ak8_helper_branch_dict['ak8jets_e'].flatten())
            ak8_branch_dict['AK8jets_Pt'] = result
            
            vectorized_function = np.vectorize(calc_obj_eta)
            result = vectorized_function(
                ak8_helper_branch_dict['ak8jets_px'].flatten(), 
                ak8_helper_branch_dict['ak8jets_py'].flatten(), 
                ak8_helper_branch_dict['ak8jets_pz'].flatten(), 
                ak8_helper_branch_dict['ak8jets_e'].flatten())
            ak8_branch_dict['AK8jets_Eta'] = result
            
            vectorized_function = np.vectorize(good_AK8_checker)
            result = vectorized_function(
                 ak8_branch_dict['AK8jets_Pt'],
                 ak8_branch_dict['AK8jets_Eta'])
            ak8_branch_dict['AK8jets_Kin_Good'] = result
            
            ak8_branch_dict['AK8jets_GoodElectron_Matched'], \
            ak8_branch_dict['AK8jets_GoodMuon_Matched'], \
            ak8_branch_dict['AK8jets_GoodElectron_Matched_Ele_ID'], \
            ak8_branch_dict['AK8jets_GoodMuon_Matched_Mu_ID'] = FatJet_Lepton_Matcher(
                ak8_branch_dict['ak8_index'],
                ak8_branch_dict['ak8_evt_index'],
                ak8_branch_dict['AK8jets_Kin_Good'],
                ak8_helper_branch_dict['ak8jets_px'].flatten(),
                ak8_helper_branch_dict['ak8jets_py'].flatten(),
                ak8_helper_branch_dict['ak8jets_pz'].flatten(),
                ak8_helper_branch_dict['ak8jets_e'].flatten(),
                lepton_branch_dict['lep_index'],
                lepton_branch_dict['lep_evt_index'],
                lepton_helper_branch_dict['daughters_px'].flatten(),
                lepton_helper_branch_dict['daughters_py'].flatten(),
                lepton_helper_branch_dict['daughters_pz'].flatten(),
                lepton_helper_branch_dict['daughters_e'].flatten(),
                lepton_branch_dict['GoodElectron'],
                lepton_branch_dict['GoodMuon'],
            )
            
            vectorized_function = np.vectorize(calc_obj_phi)
            result = vectorized_function(
                ak8_helper_branch_dict['ak8jets_px'].flatten(), 
                ak8_helper_branch_dict['ak8jets_py'].flatten(), 
                ak8_helper_branch_dict['ak8jets_pz'].flatten(), 
                ak8_helper_branch_dict['ak8jets_e'].flatten())
            ak8_branch_dict['AK8jets_Phi'] = result
            
            vectorized_function = np.vectorize(calc_mass_corr)
            result = vectorized_function(
                ak8_helper_branch_dict['ak8jets_SoftDropMass'].flatten(), 
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_masscorr'].flatten())
            ak8_branch_dict['AK8jets_Mass'] = result
            
            # ak8jets_probQCD0hf is ak8jets_PNet_score my typo ONLY in 0820 dR0p8 version
            ak8_branch_dict['AK8jets_probHttOverQCD'],\
            ak8_branch_dict['AK8jets_probHtl'],\
            ak8_branch_dict['AK8jets_probHttOverLepton'],\
            ak8_branch_dict['AK8jets_PNet_score'],\
            ak8_branch_dict['AK8jets_probHbb'], \
            ak8_branch_dict['AK8jets_9Xbb'], \
            ak8_branch_dict['AK8jets_9Xtt'], \
            ak8_branch_dict['AK8jets_9Xtm'], \
            ak8_branch_dict['AK8jets_9Xte'] = calc_prob_Htt( \
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHtt'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHtm'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHte'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probQCD0hf'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probQCD1hf'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probQCD2hf'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHbb'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHcc'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHqq'],\
                ak8_helper_branch_dict['bParticleNetTauAK8JetTags_probHgg'])
            
            ak8_branch_dict['Match_gen_tau'], \
            ak8_branch_dict['Match_gen_taus_sign'], \
            ak8_branch_dict['Match_gen_taus_dR'], \
            ak8_branch_dict['Match_gen_tau1_Mother'], \
            ak8_branch_dict['Match_gen_tau2_Mother'], \
            ak8_branch_dict['Match_gen_emu'], \
            ak8_branch_dict['Match_gen_hav'], \
            ak8_branch_dict['Match_hps_tau'], \
            ak8_branch_dict['Hps_tau1_Pt'],\
            ak8_branch_dict['Hps_tau1_E'],\
            ak8_branch_dict['Hps_tau1_Eta'],\
            ak8_branch_dict['Hps_tau1_Phi'],\
            ak8_branch_dict['Hps_tau1_M'],\
            ak8_branch_dict['Hps_tau1_DeepTauVSJets'],\
            ak8_branch_dict['Hps_tau2_Pt'],\
            ak8_branch_dict['Hps_tau2_E'],\
            ak8_branch_dict['Hps_tau2_Eta'],\
            ak8_branch_dict['Hps_tau2_Phi'],\
            ak8_branch_dict['Hps_tau2_M'], \
            ak8_branch_dict['Hps_tau2_DeepTauVSJets'] = match_ak8jets_with_tau( \
                    ak8_helper_branch_dict['ak8jets_px'], ak8_helper_branch_dict['ak8jets_py'], \
                    ak8_helper_branch_dict['ak8jets_pz'], ak8_helper_branch_dict['ak8jets_e'], \
                    ak8_helper_branch_dict['genpart_px'], ak8_helper_branch_dict['genpart_py'], \
                    ak8_helper_branch_dict['genpart_pz'], ak8_helper_branch_dict['genpart_e'], \
                    ak8_helper_branch_dict['genpart_pdg'], ak8_helper_branch_dict['genpart_flags'],\
                    ak8_helper_branch_dict['genjet_px'], ak8_helper_branch_dict['genjet_py'], \
                    ak8_helper_branch_dict['genjet_pz'], ak8_helper_branch_dict['genjet_e'], \
                    ak8_helper_branch_dict['genjet_partonFlavour'], ak8_helper_branch_dict['genjet_hadronFlavour'], \
                    ak8_helper_branch_dict['genpart_TauGenDecayMode'], ak8_helper_branch_dict['genpart_HMothInd'], \
                    ak8_helper_branch_dict['genpart_ZMothInd'], ak8_helper_branch_dict['genpart_TauMothInd'], \
                    ak8_helper_branch_dict['genpart_WMothInd'], ak8_helper_branch_dict['genpart_bMothInd'], \
                    ak8_helper_branch_dict['PDGIdDaughters'], ak8_helper_branch_dict['daughters_isTauMatched'], \
                    ak8_helper_branch_dict['daughters_px'], ak8_helper_branch_dict['daughters_py'], \
                    ak8_helper_branch_dict['daughters_pz'], ak8_helper_branch_dict['daughters_e'], \
                    ak8_helper_branch_dict['daughters_byDeepTau2017v2p1VSjetraw']
                )
            
            ### back to add some tags to the events
            event_branch_dict['IsMuonTau'], \
            event_branch_dict['IsElectronTau'], \
            event_branch_dict['IsTauTau'] = channel_tagger(
                ak8_branch_dict['ak8_index'],
                ak8_branch_dict['ak8_evt_index'],
                ak8_branch_dict['AK8jets_Kin_Good'],
                ak8_branch_dict['AK8jets_GoodElectron_Matched'],
                ak8_branch_dict['AK8jets_GoodElectron_Matched_Ele_ID'],
                ak8_branch_dict['AK8jets_GoodMuon_Matched'],
                ak8_branch_dict['AK8jets_GoodMuon_Matched_Mu_ID'],
                lepton_branch_dict['lep_index'],
                lepton_branch_dict['lep_evt_index'],
                lepton_branch_dict['GoodElectron'],
                lepton_branch_dict['GoodMuon'],
                lepton_branch_dict['VetoElectron'],
                lepton_branch_dict['VetoMuon'],
                event_branch_dict['PassMuonPath'],
                event_branch_dict['PassElectronPath'],
                event_branch_dict['PassHadronicPath']
            )
            
            event_branch_dict['Hbb_jet_index'], \
            event_branch_dict['Hbb_mass'], \
            event_branch_dict['Hbb_pt'], \
            event_branch_dict['Hbb_eta'], \
            event_branch_dict['Hbb_phi'], \
            event_branch_dict['Hbb_9Xbb'], \
            event_branch_dict['Htx_jet_index'], \
            event_branch_dict['Htx_mass'], \
            event_branch_dict['Htx_pt'], \
            event_branch_dict['Htx_eta'], \
            event_branch_dict['Htx_phi'], \
            event_branch_dict['Htx_9Xtx'], \
            event_branch_dict['Hbb_Htx_dR'], \
            event_branch_dict['Hbb_Htx_dPhi'], \
            event_branch_dict['Hbb_Htx_distinct'], \
            event_branch_dict['Hbb_T_Htx_T'], \
            event_branch_dict['Hbb_T_Htx_L'], \
            event_branch_dict['Hbb_L_Htx_T'], \
            event_branch_dict['Hbb_L_Htx_L'] = higgs_tagger(
                event_branch_dict['IsMuonTau'],
                event_branch_dict['IsElectronTau'],
                event_branch_dict['IsTauTau'],
                ak8_branch_dict['ak8_index'],
                ak8_branch_dict['ak8_evt_index'],
                ak8_branch_dict['AK8jets_9Xbb'],
                ak8_branch_dict['AK8jets_9Xtt'],
                ak8_branch_dict['AK8jets_9Xtm'],
                ak8_branch_dict['AK8jets_9Xte'],
                ak8_branch_dict['AK8jets_Mass'],
                ak8_branch_dict['AK8jets_Pt'],
                ak8_branch_dict['AK8jets_Eta'],
                ak8_branch_dict['AK8jets_Phi']
            )
            
            ### saving trees
            out_file["Eventree"] = event_branch_dict
            out_file["Leptree"] = lepton_branch_dict
            out_file["AK8tree"] = ak8_branch_dict
            
            del event_tree
            del out_file
            del event_branch_dict
            del lepton_branch_dict
            del ak8_branch_dict
            
            gc.collect()
            return 0
        
    num_processes = multiprocessing.cpu_count()
    pool = Pool(round(num_processes*0.85))
    # pool = Pool(1)
    print('using {} cores'.format(round(num_processes*0.85)))
    results = []
    with tqdm(total=len(fileset[process][0])) as pbar:
        for result in tqdm(pool.imap(process_file, fileset[process][0])):
            results.append(result)
            pbar.update()
            
    pool.close()
    pool.join()
          
        
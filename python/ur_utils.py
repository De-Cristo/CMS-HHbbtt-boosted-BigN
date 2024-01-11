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

import math

def check_bit(number, bitpos):
    res = number & (1 << bitpos)
    return bool(res)

def track_var_to_flat(arr, idx_low, idx_high):
    return awkward.to_awkward0(awkward.Array( [[ ev[ka : kb] for ka, kb in zip(kidx_a, kidx_b)] for ev, kidx_a, kidx_b in zip(arr, idx_low, idx_high)])).flatten()

def calc_true_weight(ARR_aMCatNLOweight, XS, lumi, sumOfweights):
    arr_weights = ARR_aMCatNLOweight * XS * lumi / sumOfweights
    return arr_weights

def calc_obj_pT(obj_px, obj_py, obj_pz, obj_e):
    return R.Math.PxPyPzEVector(obj_px, obj_py, obj_pz, obj_e).Pt()

def calc_obj_eta(obj_px, obj_py, obj_pz, obj_e):
    return R.Math.PxPyPzEVector(obj_px, obj_py, obj_pz, obj_e).Eta()

def calc_obj_phi(obj_px, obj_py, obj_pz, obj_e):
    return R.Math.PxPyPzEVector(obj_px, obj_py, obj_pz, obj_e).Phi()

def calc_obj_pT_vec(obj_px_v, obj_py_v, obj_pz_v, obj_e_v):
    pT_v = []
    for _subarr in zip(obj_px_v, obj_py_v, obj_pz_v, obj_e_v):
        pT_v.append(calc_obj_pT(*_subarr))
    return awkward.Array(pT_v)

def calc_mass_corr(original_mass, correction_factor):
    return original_mass * correction_factor

def calc_prob_Htt(arr_bParticleNetTauAK8JetTags_probHtt,
                  arr_bParticleNetTauAK8JetTags_probHtm, 
                  arr_bParticleNetTauAK8JetTags_probHte,
                  arr_bParticleNetTauAK8JetTags_probQCD0hf, 
                  arr_bParticleNetTauAK8JetTags_probQCD1hf, 
                  arr_bParticleNetTauAK8JetTags_probQCD2hf,
                  arr_bParticleNetTauAK8JetTags_probHbb,
                  bParticleNetTauAK8JetTags_probHcc,
                  bParticleNetTauAK8JetTags_probHqq,
                  bParticleNetTauAK8JetTags_probHgg):
    
    arr_ak8jets_probHttOverQCD = []
    arr_ak8jets_probHtl = []
    arr_ak8jets_probHttOverLepton = []
    arr_ak8jets_PNet_score = []
    arr_ak8jets_probHbb = []
    arr_ak8jets_Xbb = []
    arr_ak8jets_Xtt = []
    arr_ak8jets_Xtm = []
    arr_ak8jets_Xte = []
    
    event_num = len(arr_bParticleNetTauAK8JetTags_probHtt)
    
    for evt_idx in range(event_num):
        jet_num = len(arr_bParticleNetTauAK8JetTags_probHtt[evt_idx])
        
        subarr_ak8jets_probHttOverQCD = []
        subarr_ak8jets_probHtl = []
        subarr_ak8jets_probHttOverLepton = []
        subarr_ak8jets_PNet_score = []
        subarr_ak8jets_probHbb = []
        subarr_ak8jets_Xbb = []
        subarr_ak8jets_Xtt = []
        subarr_ak8jets_Xtm = []
        subarr_ak8jets_Xte = []
        
        for _jet in range(0,jet_num):
        
            Htt = arr_bParticleNetTauAK8JetTags_probHtt[evt_idx][_jet]
            Htm = arr_bParticleNetTauAK8JetTags_probHtm[evt_idx][_jet]
            Hte = arr_bParticleNetTauAK8JetTags_probHte[evt_idx][_jet]
            hf_0 = arr_bParticleNetTauAK8JetTags_probQCD0hf[evt_idx][_jet]
            hf_1 = arr_bParticleNetTauAK8JetTags_probQCD1hf[evt_idx][_jet]
            hf_2 = arr_bParticleNetTauAK8JetTags_probQCD2hf[evt_idx][_jet]
            Hbb = arr_bParticleNetTauAK8JetTags_probHbb[evt_idx][_jet]
            Hcc = bParticleNetTauAK8JetTags_probHcc[evt_idx][_jet]
            Hqq = bParticleNetTauAK8JetTags_probHqq[evt_idx][_jet]
            Hgg = bParticleNetTauAK8JetTags_probHgg[evt_idx][_jet]
            
            subarr_ak8jets_probHtl.append(float(Htm+Hte))
            subarr_ak8jets_probHbb.append(float(Hbb))
        
            if (Htt + hf_0 + hf_1 + hf_2) == 0:
                subarr_ak8jets_probHttOverQCD.append(-99.)
            else:
                subarr_ak8jets_probHttOverQCD.append(float(Htt / (Htt + hf_0 + hf_1 + hf_2)))
        
            if (Htt+Htm+Hte) == 0:
                subarr_ak8jets_probHttOverLepton.append(-99.)
            else:
                subarr_ak8jets_probHttOverLepton.append(float(Htt/(Htt+Htm+Hte)))
                
            if (Htt + hf_0 + hf_1 + hf_2 + Htm + Hte) == 0:
                subarr_ak8jets_PNet_score.append(-99.)
            else:
                subarr_ak8jets_PNet_score.append(float(Htt/(Htt + hf_0 + hf_1 + hf_2 + Htm + Hte)))
                
            if (Htt + Htm + Hte + Hbb + Hcc + Hqq + Hgg + hf_0 + hf_1 + hf_2) == 0:
                subarr_ak8jets_Xbb.append(-99.)
                subarr_ak8jets_Xtt.append(-99.)
                subarr_ak8jets_Xtm.append(-99.)
                subarr_ak8jets_Xte.append(-99.)
            else:
                _Xbb = float(Hbb / (Htt + Htm + Hte + Hbb + Hcc + Hqq + Hgg + hf_0 + hf_1 + hf_2))
                _Xtt = float(Htt / (Htt + Htm + Hte + Hbb + Hcc + Hqq + Hgg + hf_0 + hf_1 + hf_2))
                _Xtm = float(Htm / (Htt + Htm + Hte + Hbb + Hcc + Hqq + Hgg + hf_0 + hf_1 + hf_2))
                _Xte = float(Hte / (Hte + Hbb + Hcc + Hqq + Hgg + hf_0 + hf_1 + hf_2)) # need double check
                
                subarr_ak8jets_Xbb.append(-99. if _Xbb == 0 else -math.log(1-_Xbb+1e-18,10))
                subarr_ak8jets_Xtt.append(-99. if _Xtt == 0 else -math.log(1-_Xtt+1e-18,10))
                subarr_ak8jets_Xtm.append(-99. if _Xtm == 0 else -math.log(1-_Xtm+1e-18,10))
                subarr_ak8jets_Xte.append(-99. if _Xte == 0 else -math.log(1-_Xte+1e-18,10))
                
                
        arr_ak8jets_probHttOverQCD.append(subarr_ak8jets_probHttOverQCD)
        arr_ak8jets_probHtl.append(subarr_ak8jets_probHtl)
        arr_ak8jets_probHttOverLepton.append(subarr_ak8jets_probHttOverLepton)
        arr_ak8jets_PNet_score.append(subarr_ak8jets_PNet_score)
        arr_ak8jets_probHbb.append(subarr_ak8jets_probHbb)
        arr_ak8jets_Xbb.append(subarr_ak8jets_Xbb)
        arr_ak8jets_Xtt.append(subarr_ak8jets_Xtt)
        arr_ak8jets_Xtm.append(subarr_ak8jets_Xtm)
        arr_ak8jets_Xte.append(subarr_ak8jets_Xte)
            
    return awkward.to_awkward0(awkward.Array(arr_ak8jets_probHttOverQCD)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_probHtl)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_probHttOverLepton)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_PNet_score)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_probHbb)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_Xbb)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_Xtt)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_Xtm)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_ak8jets_Xte)).flatten()

def HLT_path_checker(triggerbit):
    # for parameter PassHLTPath [0, 0, 0], if 1 means pass the HLT path. the order is [Muon Path, Electron Path, Hadronic(Jet/Met) Path]
    muon_path = 0
    electron_path = 0
    hadronic_path = 0
    # Muon Path
    if check_bit(triggerbit, 0) or check_bit(triggerbit, 27): muon_path = 1
    if check_bit(triggerbit, 2) or check_bit(triggerbit, 46): electron_path = 1
    if check_bit(triggerbit, 39) or check_bit(triggerbit, 42) or check_bit(triggerbit, 43) or check_bit(triggerbit, 44) or check_bit(triggerbit, 45): 
        hadronic_path = 1
    return muon_path, electron_path, hadronic_path
    
def lepton_type_checker(pT, eta, dxy, dz, MuonID, iseleWP90, iseleNoIsoID90):
    GoodMuon = 0
    VetoMuon = 0
    GoodElectron = 0
    VetoElectron = 0
    
    if (pT > 30) and abs(eta) < 2.4 and abs(dxy) < 0.05 and abs(dz) < 0.2 and (check_bit(MuonID, 4) or check_bit(MuonID, 3)):
        GoodMuon = 1
    if (pT > 10) and abs(eta) < 2.4 and abs(dxy) < 0.05 and abs(dz) < 0.2 and check_bit(MuonID, 0):
        VetoMuon = 1
    if (pT > 40) and abs(eta) < 2.5 and abs(dxy) < 0.05 and abs(dz) < 0.2 and iseleWP90 == 1:
        GoodElectron = 1
    if (pT > 20) and abs(eta) < 2.5 and abs(dxy) < 0.05 and abs(dz) < 0.2 and iseleNoIsoID90 == 1:
        VetoElectron = 1
    
    return GoodMuon, VetoMuon, GoodElectron, VetoElectron

def good_AK8_checker(pT, Eta):
    if pT > 200 and abs(Eta) < 2.4: return 1
    else: return 0

def FatJet_Lepton_Matcher(ak8_index, ak8_evt_index, ak8jets_kin_good, ak8_px, ak8_py, ak8_pz, ak8_e, \
                          lep_index, lep_evt_index, lepton_px, lepton_py, lepton_pz, lepton_e, GoodElectron, GoodMuon):
    
    AK8jets_GoodElectron_Matched = []
    AK8jets_GoodMuon_Matched = []
    AK8jets_GoodElectron_Matched_Ele_ID = []
    AK8jets_GoodMuon_Matched_Mu_ID = []
    
    for evt_idx in range(0, ak8_evt_index[-1]+1):
        ak8_obj = R.TLorentzVector()
        lep_obj = R.TLorentzVector()
        
        for _ak8_idx in ak8_index[ ak8_evt_index==evt_idx ]:
            _match_ele = 0
            _match_mu = 0
            _ele_id = -99
            _mu_id = -99
            if ak8jets_kin_good[_ak8_idx]==1:
                ak8_obj.SetPxPyPzE(ak8_px[_ak8_idx], ak8_py[_ak8_idx], ak8_pz[_ak8_idx], ak8_e[_ak8_idx])

                for _lep_idx in lep_index[ lep_evt_index==evt_idx ]:
                    lep_obj.SetPxPyPzE(lepton_px[_lep_idx], lepton_py[_lep_idx], lepton_pz[_lep_idx], lepton_e[_lep_idx])
                    if abs(ak8_obj.DeltaR(lep_obj)) < 0.8:
                        if GoodElectron[_lep_idx] == 1: 
                            _match_ele += 1
                            _ele_id = _lep_idx
                        if GoodMuon[_lep_idx] == 1: 
                            _match_mu += 1
                            _mu_id = _lep_idx
            
            if _match_ele != 1: _ele_id = -99
            if _match_mu != 1: _mu_id = -99
            
            AK8jets_GoodElectron_Matched_Ele_ID.append(_ele_id)
            AK8jets_GoodMuon_Matched_Mu_ID.append(_mu_id)
            AK8jets_GoodElectron_Matched.append(_match_ele)
            AK8jets_GoodMuon_Matched.append(_match_mu)
    
    return awkward.to_awkward0(awkward.Array(AK8jets_GoodElectron_Matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(AK8jets_GoodMuon_Matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(AK8jets_GoodElectron_Matched_Ele_ID)).flatten(), \
           awkward.to_awkward0(awkward.Array(AK8jets_GoodMuon_Matched_Mu_ID)).flatten()


def process_event(args):
    # Unpack the arguments
    evt_idx, ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e, \
    genpart_px, genpart_py, genpart_pz, genpart_e, \
    genpart_pdg, genpart_flags, \
    genjet_px, genjet_py, genjet_pz, genjet_e, \
    genjet_partonFlavour, genjet_hadronFlavour, genpart_TauGenDecayMode,\
    genpart_HMothInd, genpart_ZMothInd, genpart_TauMothInd, genpart_WMothInd, genpart_bMothInd, \
    PDGIdDaughters, daughters_isTauMatched, \
    daughters_px, daughters_py, daughters_pz, daughters_e, daughters_byDeepTau2017v2p1VSjetraw = args

    ak8_obj = R.TLorentzVector()
    gen_obj = R.TLorentzVector()
    genjet_obj = R.TLorentzVector()
    daughter_obj = R.TLorentzVector()

    sub_arr_tau_matched = []
    sub_arr_taus_sign = []
    sub_arr_taus_dR = []
    sub_arr_tau1_Mother = []
    sub_arr_tau2_Mother = []
    
    sub_arr_emu_matched = []
    sub_arr_hav_matched = []
    sub_arr_hps_matched = []
    
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
        taus_sign = -99.
        taus_dR = -99.
        tau1_Mother = -99.
        tau2_Mother = -99.
        tau_pt = []
        tau_idx = []
        for gen_obj_idx in range(len(genpart_px)):
            gen_obj.SetPxPyPzE(genpart_px[gen_obj_idx], genpart_py[gen_obj_idx], genpart_pz[gen_obj_idx], genpart_e[gen_obj_idx])
            # DeltaR < 0.8 (we also check the 0.4 version); obj is tau; genflag 13 == 1 is last copy; TauGenDecayMode == 2 is hadronic decay.
            if ak8_obj.DeltaR(gen_obj) < 0.8 \
                and abs(genpart_pdg[gen_obj_idx]) == 15 \
                and (genpart_flags[gen_obj_idx] & (1 << 13)) \
                and (genpart_TauGenDecayMode[gen_obj_idx] == 2):
                tau_matched += 1
                tau_pt.append(gen_obj.Pt())
                tau_idx.append(gen_obj_idx)
                
        if tau_matched == 0:
            pass
        elif tau_matched == 1:
            pass
        else:
            sorted_lists = sorted(zip(tau_pt, tau_idx))
            tau_pt, tau_idx = zip(*sorted_lists)
            tau_idx = list(reversed(tau_idx))
            gentau_count = 0
            _tau1 = R.TLorentzVector()
            _tau2 = R.TLorentzVector()
            _tau1.SetPxPyPzE(genpart_px[tau_idx[0]], genpart_py[tau_idx[0]], genpart_pz[tau_idx[0]], genpart_e[tau_idx[0]])
            _tau2.SetPxPyPzE(genpart_px[tau_idx[1]], genpart_py[tau_idx[1]], genpart_pz[tau_idx[1]], genpart_e[tau_idx[1]])
            if genpart_pdg[tau_idx[0]]*genpart_pdg[tau_idx[1]] < 0: taus_sign = -1
            else: taus_sign = 1
            taus_dR = _tau1.DeltaR(_tau2)
            
            if genpart_HMothInd[tau_idx[0]] > -1: tau1_Mother = 25
            elif genpart_ZMothInd[tau_idx[0]] > -1: tau1_Mother = 23
            elif genpart_TauMothInd[tau_idx[0]] > -1: tau1_Mother = 15
            elif genpart_WMothInd[tau_idx[0]] > -1: tau1_Mother = 24
            elif genpart_bMothInd[tau_idx[0]] > -1: tau1_Mother = 5
            else: tau1_Mother = -99
            
            if genpart_HMothInd[tau_idx[1]] > -1: tau2_Mother = 25
            elif genpart_ZMothInd[tau_idx[1]] > -1: tau2_Mother = 23
            elif genpart_TauMothInd[tau_idx[1]] > -1: tau2_Mother = 15
            elif genpart_WMothInd[tau_idx[1]] > -1: tau2_Mother = 24
            elif genpart_bMothInd[tau_idx[1]] > -1: tau2_Mother = 5
            else: tau2_Mother = -99
                
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
            for daughter_obj_idx in hps_matched_idx:
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

        sub_arr_tau_matched.append(tau_matched)
        sub_arr_taus_sign.append(taus_sign)
        sub_arr_taus_dR.append(taus_dR)
        sub_arr_tau1_Mother.append(tau1_Mother)
        sub_arr_tau2_Mother.append(tau2_Mother)
        
        sub_arr_emu_matched.append(emu_matched)
        sub_arr_hav_matched.append(hav_matched)
        sub_arr_hps_matched.append(hps_matched)
        
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
        
    return sub_arr_tau_matched, sub_arr_taus_sign, sub_arr_taus_dR, sub_arr_tau1_Mother, sub_arr_tau2_Mother,\
           sub_arr_emu_matched, sub_arr_hav_matched, sub_arr_hps_matched, \
           sub_arr_hps1_Pt, sub_arr_hps1_E, sub_arr_hps1_Eta, sub_arr_hps1_Phi, sub_arr_hps1_M, sub_arr_hps1_DeepTauVSJets, \
           sub_arr_hps2_Pt, sub_arr_hps2_E, sub_arr_hps2_Eta, sub_arr_hps2_Phi, sub_arr_hps2_M, sub_arr_hps2_DeepTauVSJets

def match_ak8jets_with_tau(ARR_ak8jets_px, ARR_ak8jets_py, ARR_ak8jets_pz, ARR_ak8jets_e, \
                           ARR_genpart_px, ARR_genpart_py, ARR_genpart_pz, ARR_genpart_e, \
                           ARR_genpart_pdg, ARR_genpart_flags, \
                           ARR_genjet_px, ARR_genjet_py, ARR_genjet_pz, ARR_genjet_e, \
                           ARR_genjet_partonFlavour, ARR_genjet_hadronFlavour, ARR_genpart_TauGenDecayMode, \
                           ARR_genpart_HMothInd, ARR_genpart_ZMothInd, ARR_genpart_TauMothInd, ARR_genpart_WMothInd, ARR_genpart_bMothInd, \
                           ARR_PDGIdDaughters, ARR_daughters_isTauMatched, \
                           ARR_daughters_px, ARR_daughters_py, ARR_daughters_pz, ARR_daughters_e, \
                           ARR_daughters_byDeepTau2017v2p1VSjetraw
                          ):
    num_events = len(ARR_ak8jets_px)
    # print('there are {} events'.format(num_events))

    arr_tau_matched = []
    arr_taus_sign = []
    arr_taus_dR = []
    arr_tau1_Mother = []
    arr_tau2_Mother = []
    
    arr_emu_matched = []
    arr_hav_matched = []
    arr_hps_matched = []
    
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
                           ARR_genpart_TauMothInd[evt_idx],
                           ARR_genpart_WMothInd[evt_idx],
                           ARR_genpart_bMothInd[evt_idx],
                           ARR_PDGIdDaughters[evt_idx],
                           ARR_daughters_isTauMatched[evt_idx],
                           ARR_daughters_px[evt_idx],
                           ARR_daughters_py[evt_idx],
                           ARR_daughters_pz[evt_idx],
                           ARR_daughters_e[evt_idx],
                           ARR_daughters_byDeepTau2017v2p1VSjetraw[evt_idx]
                          ),
                         )
    
    results = []
    for _args in event_args:
        results.append(process_event(_args))
    
    # Unpack the results
    for res in results:
        arr_tau_matched.append(res[0])
        arr_taus_sign.append(res[1])
        arr_taus_dR.append(res[2])
        arr_tau1_Mother.append(res[3])
        arr_tau2_Mother.append(res[4])
        arr_emu_matched.append(res[5])
        arr_hav_matched.append(res[6])
        arr_hps_matched.append(res[7])
        arr_hps1_Pt.append(res[8])
        arr_hps1_E.append(res[9])
        arr_hps1_Eta.append(res[10])
        arr_hps1_Phi.append(res[11])
        arr_hps1_M.append(res[12])
        arr_hps1_DeepTauVSJets.append(res[13])
        arr_hps2_Pt.append(res[14])
        arr_hps2_E.append(res[15])
        arr_hps2_Eta.append(res[16])
        arr_hps2_Phi.append(res[17])
        arr_hps2_M.append(res[18])
        arr_hps2_DeepTauVSJets.append(res[19])

    return awkward.to_awkward0(awkward.Array(arr_tau_matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_taus_sign)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_taus_dR)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_tau1_Mother)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_tau2_Mother)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_emu_matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hav_matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps_matched)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Pt)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_E)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Eta)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_Phi)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_M)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps1_DeepTauVSJets)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Pt)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_E)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Eta)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_Phi)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_M)).flatten(), \
           awkward.to_awkward0(awkward.Array(arr_hps2_DeepTauVSJets)).flatten()


def channel_tagger(ak8_index, ak8_evt_index, ak8_kin_good, \
                   ak8_goodelectron_matched, ak8jets_goodelectron_matched_ele_id, \
                   ak8_goodmuon_matched, ak8jets_goodmuon_matched_mu_id, \
                   lep_index, lep_evt_index, \
                   goodelectron, goodmuon, vetoelectron, vetomuon, \
                   passmuonpath, passelectronpath, passhadronicpath):
    
    IsMuonTau = []
    IsElectronTau = []
    IsTauTau = []
    
    for evt_idx in range(0, ak8_evt_index[-1]+1):
        _isMT = 0
        _isET = 0
        _isTT = 0
        
        if passmuonpath[evt_idx] == 1:
            _goodAK8 = 0
            _muonAK8 = 0
            for _ak8_idx in ak8_index[ ak8_evt_index==evt_idx ]:
                if ak8_kin_good[_ak8_idx] == 1: 
                    _goodAK8 += 1
                    if ak8_goodmuon_matched[_ak8_idx] == 1:
                        _muonAK8 += 1
                    
            if _goodAK8 > 1 and _muonAK8 > 0:
                _isMT = 1
                
        if passelectronpath[evt_idx] == 1:
            _goodAK8 = 0
            _electronAK8 = 0
            for _ak8_idx in ak8_index[ ak8_evt_index==evt_idx ]:
                if ak8_kin_good[_ak8_idx] == 1: 
                    _goodAK8 += 1
                    if ak8_goodelectron_matched[_ak8_idx] == 1:
                        _electronAK8 += 1
                    
            if _goodAK8 > 1 and _electronAK8 > 0:
                _isET = 1
                
        if passhadronicpath[evt_idx] == 1:
            _goodAK8 = 0
            _vetoLep = 0
            for _ak8_idx in ak8_index[ ak8_evt_index==evt_idx ]:
                if ak8_kin_good[_ak8_idx] == 1: 
                    _goodAK8 += 1
            
            for _lep_idx in lep_index[ lep_evt_index==evt_idx ]:
                if vetoelectron[_lep_idx] == 1 or vetomuon[_lep_idx] == 1:
                    _vetoLep += 1
            
            if _goodAK8 > 1 and _vetoLep < 1:
                _isTT = 1
                
        IsMuonTau.append(_isMT)
        IsElectronTau.append(_isET)
        IsTauTau.append(_isTT)
    
    return awkward.to_awkward0(awkward.Array(IsMuonTau)).flatten(),\
           awkward.to_awkward0(awkward.Array(IsElectronTau)).flatten(),\
           awkward.to_awkward0(awkward.Array(IsTauTau)).flatten()


def higgs_tagger(IsMuonTau, IsElectronTau, IsTauTau, \
                 ak8_index, ak8_evt_index, \
                 AK8jets_9Xbb, AK8jets_9Xtt, AK8jets_9Xtm, AK8jets_9Xte,\
                 AK8jets_Mass, AK8jets_Pt, AK8jets_Eta, AK8jets_Phi):

    Hbb_jet_index = []
    Hbb_mass = []
    Hbb_pt = []
    Hbb_eta = []
    Hbb_phi = []
    Hbb_9Xbb = []
    Htx_jet_index = []
    Htx_mass = []
    Htx_pt = []
    Htx_eta = []
    Htx_phi = []
    Htx_9Xtx = []
    Hbb_Htx_dR = []
    Hbb_Htx_dPhi = []
    Hbb_Htx_distinct = []
    Hbb_T_Htx_T = []
    Hbb_T_Htx_L = []
    Hbb_L_Htx_T = []
    Hbb_L_Htx_L = []
    
    for evt_idx in range(0, ak8_evt_index[-1]+1):
        _Hbb_jet_index = -99.
        _Hbb_mass = -99.
        _Hbb_pt = -99.
        _Hbb_eta = -99.
        _Hbb_phi = -99.
        _Hbb_9Xbb = -99.
        _Htx_jet_index = -99.
        _Htx_mass = -99.
        _Htx_pt = -99.
        _Htx_eta = -99.
        _Htx_phi = -99.
        _Htx_9Xtx = -99.
        
        _Hbb_4v = R.TLorentzVector()
        _Htx_4v = R.TLorentzVector()
        
        _Hbb_Htx_dR = -99.
        _Hbb_Htx_dPhi = -99.
        
        _Hbb_Htx_distinct = 0
        _Hbb_T_Htx_T = 0
        _Hbb_T_Htx_L = 0
        _Hbb_L_Htx_T = 0
        _Hbb_L_Htx_L = 0
        
        _Hbb_FLT = 0
        _Htx_FLT = 0
        
        # hbb: type: xbb vs all, F < 1, T > 1.75
        # htt: type: xtt vs all, F < 1, T > 2
        # htm: type: xtm vs all, F < 3, T > 4
        # hte: type: xte vs sf, F < 2, T > 2.5

        
        if IsMuonTau[evt_idx] == 1:
            _Hbb_jet_index = ak8_index[ak8_evt_index==evt_idx][awkward.argmax(AK8jets_9Xbb[ak8_evt_index==evt_idx])]
            _Hbb_mass = AK8jets_Mass[_Hbb_jet_index]
            _Hbb_pt = AK8jets_Pt[_Hbb_jet_index]
            _Hbb_eta = AK8jets_Eta[_Hbb_jet_index]
            _Hbb_phi = AK8jets_Phi[_Hbb_jet_index]
            _Hbb_9Xbb = AK8jets_9Xbb[_Hbb_jet_index]
            
            _Hbb_4v.SetPtEtaPhiM(_Hbb_pt, _Hbb_eta, _Hbb_phi, _Hbb_mass)
            
            _Htx_jet_index = \
                ak8_index[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)]\
                [awkward.argmax(AK8jets_9Xtm[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)])]
            
            _Htx_mass = AK8jets_Mass[_Htx_jet_index]
            _Htx_pt = AK8jets_Pt[_Htx_jet_index]
            _Htx_eta = AK8jets_Eta[_Htx_jet_index]
            _Htx_phi = AK8jets_Phi[_Htx_jet_index]
            _Htx_9Xtx = AK8jets_9Xtm[_Htx_jet_index]
            
            _Htx_4v.SetPtEtaPhiM(_Htx_pt, _Htx_eta, _Htx_phi, _Htx_mass)
            
            _Hbb_Htx_dR = _Hbb_4v.DeltaR(_Htx_4v)
            _Hbb_Htx_dPhi = _Hbb_4v.DeltaPhi(_Htx_4v)
            
            if _Htx_9Xtx>3.0 and _Htx_9Xtx<4.0:
                _Htx_FLT = 1
            elif _Htx_9Xtx>=4.0:
                _Htx_FLT = 2
            
        if IsElectronTau[evt_idx] == 1:
            _Hbb_jet_index = ak8_index[ak8_evt_index==evt_idx][awkward.argmax(AK8jets_9Xbb[ak8_evt_index==evt_idx])]
            _Hbb_mass = AK8jets_Mass[_Hbb_jet_index]
            _Hbb_pt = AK8jets_Pt[_Hbb_jet_index]
            _Hbb_eta = AK8jets_Eta[_Hbb_jet_index]
            _Hbb_phi = AK8jets_Phi[_Hbb_jet_index]
            _Hbb_9Xbb = AK8jets_9Xte[_Hbb_jet_index]
            
            _Hbb_4v.SetPtEtaPhiM(_Hbb_pt, _Hbb_eta, _Hbb_phi, _Hbb_mass)
            
            _Htx_jet_index = \
                ak8_index[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)]\
                [awkward.argmax(AK8jets_9Xte[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)])]
            
            _Htx_mass = AK8jets_Mass[_Htx_jet_index]
            _Htx_pt = AK8jets_Pt[_Htx_jet_index]
            _Htx_eta = AK8jets_Eta[_Htx_jet_index]
            _Htx_phi = AK8jets_Phi[_Htx_jet_index]
            
            _Htx_4v.SetPtEtaPhiM(_Htx_pt, _Htx_eta, _Htx_phi, _Htx_mass)
            
            _Hbb_Htx_dR = _Hbb_4v.DeltaR(_Htx_4v)
            _Hbb_Htx_dPhi = _Hbb_4v.DeltaPhi(_Htx_4v)
            
            if _Htx_9Xtx>2.0 and _Htx_9Xtx<2.5:
                _Htx_FLT = 1
            elif _Htx_9Xtx>=2.5:
                _Htx_FLT = 2
            
        if IsTauTau[evt_idx] == 1:
            _Hbb_jet_index = ak8_index[ak8_evt_index==evt_idx][awkward.argmax(AK8jets_9Xbb[ak8_evt_index==evt_idx])]
            _Hbb_mass = AK8jets_Mass[_Hbb_jet_index]
            _Hbb_pt = AK8jets_Pt[_Hbb_jet_index]
            _Hbb_eta = AK8jets_Eta[_Hbb_jet_index]
            _Hbb_phi = AK8jets_Phi[_Hbb_jet_index]
            _Hbb_9Xbb = AK8jets_9Xtt[_Hbb_jet_index]
            
            _Hbb_4v.SetPtEtaPhiM(_Hbb_pt, _Hbb_eta, _Hbb_phi, _Hbb_mass)
            
            _Htx_jet_index = \
                ak8_index[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)]\
                [awkward.argmax(AK8jets_9Xtt[(ak8_evt_index==evt_idx)&(ak8_index!=_Hbb_jet_index)])]
            
            _Htx_mass = AK8jets_Mass[_Htx_jet_index]
            _Htx_pt = AK8jets_Pt[_Htx_jet_index]
            _Htx_eta = AK8jets_Eta[_Htx_jet_index]
            _Htx_phi = AK8jets_Phi[_Htx_jet_index]
            
            _Htx_4v.SetPtEtaPhiM(_Htx_pt, _Htx_eta, _Htx_phi, _Htx_mass)
            
            _Hbb_Htx_dR = _Hbb_4v.DeltaR(_Htx_4v)
            _Hbb_Htx_dPhi = _Hbb_4v.DeltaPhi(_Htx_4v)
            
            if _Htx_9Xtx>1.0 and _Htx_9Xtx<2.0:
                _Htx_FLT = 1
            elif _Htx_9Xtx>=2.0:
                _Htx_FLT = 2
            
        if _Hbb_Htx_dR > 1.6 and _Hbb_Htx_dPhi > 3*math.pi/4:
            _Hbb_Htx_distinct = 1
            
        if _Hbb_9Xbb > 1.0 and _Hbb_9Xbb < 1.75:
            _Hbb_FLT = 1
        elif _Hbb_9Xbb >= 1.75:
            _Hbb_FLT = 2
            
        if _Hbb_FLT == 2 and _Htx_FLT == 2:
            _Hbb_T_Htx_T = 1
        elif _Hbb_FLT == 2 and _Htx_FLT == 1:
            _Hbb_T_Htx_L = 1
        elif _Hbb_FLT == 1 and _Htx_FLT == 2:
            _Hbb_L_Htx_T = 1
        elif _Hbb_FLT == 1 and _Htx_FLT == 1:
            _Hbb_L_Htx_L = 1
            
        Hbb_jet_index.append(_Hbb_jet_index)
        Hbb_mass.append(_Hbb_mass)
        Hbb_pt.append(_Hbb_pt)
        Hbb_eta.append(_Hbb_eta)
        Hbb_phi.append(_Hbb_phi)
        Hbb_9Xbb.append(_Hbb_9Xbb)
        Htx_jet_index.append(_Htx_jet_index)
        Htx_mass.append(_Htx_mass)
        Htx_pt.append(_Htx_pt)
        Htx_eta.append(_Htx_eta)
        Htx_phi.append(_Htx_phi)
        Htx_9Xtx.append(_Htx_9Xtx)
        Hbb_Htx_dR.append(_Hbb_Htx_dR)
        Hbb_Htx_dPhi.append(_Hbb_Htx_dPhi)
        Hbb_Htx_distinct.append(_Hbb_Htx_distinct)
        Hbb_T_Htx_T.append(_Hbb_T_Htx_T)
        Hbb_T_Htx_L.append(_Hbb_T_Htx_L)
        Hbb_L_Htx_T.append(_Hbb_L_Htx_T)
        Hbb_L_Htx_L.append(_Hbb_L_Htx_L)
        
    return awkward.to_awkward0(awkward.Array(Hbb_jet_index)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_mass)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_pt)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_eta)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_phi)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_9Xbb)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_jet_index)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_mass)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_pt)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_eta)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_phi)).flatten(),\
           awkward.to_awkward0(awkward.Array(Htx_9Xtx)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_Htx_dR)).flatten(),\
           awkward.to_awkward0(awkward.Array(Hbb_Htx_dPhi)).flatten(), \
           awkward.to_awkward0(awkward.Array(Hbb_Htx_distinct)).flatten(), \
           awkward.to_awkward0(awkward.Array(Hbb_T_Htx_T)).flatten(), \
           awkward.to_awkward0(awkward.Array(Hbb_T_Htx_L)).flatten(), \
           awkward.to_awkward0(awkward.Array(Hbb_L_Htx_T)).flatten(), \
           awkward.to_awkward0(awkward.Array(Hbb_L_Htx_L)).flatten()



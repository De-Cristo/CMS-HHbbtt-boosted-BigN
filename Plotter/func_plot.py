import ROOT as R
import re
import argparse
from array import array
import os
R.EnableImplicitMT()
R.gROOT.SetBatch(True)
from Plotter.plot_utils import *

path = "/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/" + "AK8based_Out_810_hadd/"

process_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarSemi', 'TTbarDiLep']
sample_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarSemi', 'TTbarDiLep']
DY_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
SH_list = ['VBFH', 'ggFH']
TT_list = ['TTbarHad', 'TTbarSemi', 'TTbarDiLep']

fileset = {}
fileset['SMHH'] = []
fileset['VBFH'] = []
fileset['ggFH'] = []
fileset['DY+Jets50To100'] = []
fileset['DY+Jets100To250'] = []
fileset['DY+Jets250To400'] = []
fileset['DY+Jets400To650'] = []
fileset['DY+Jets650ToInf'] = []
fileset['TTbarHad'] = []
fileset['TTbarSemi'] = []
fileset['TTbarDiLep'] = []
# for process in process_list:
for process in sample_list:
    for file in os.listdir(path+process):
        if file.endswith(".root"):
            fileset[process].append(path+'/'+process+'/'+file)
            
print("root files are read.")
            
df_dict = {}
histo_dict = {}

interested_variables = {"ak8jets_SoftDropMass", "bParticleNetTauAK8JetTags_masscorr","true_weight","ak8jets_Pt","ak8jets_Mass",\
                        "ak8jets_probHttOverQCD","ak8jets_probHtl","ak8jets_probHttOverLepton","ak8jets_probQCD0hf",\
                        "match_gen_tau","match_gen_hav","bParticleNetTauAK8JetTags_probHtt",\
                        "match_gen_taus_sign","match_gen_taus_dR"}

eta_cut = "abs(ak8jets_Eta)<2.5"
# mass_cut = "ak8jets_SoftDropMass>30"
mass_cut = "ak8jets_SoftDropMass>60 && ak8jets_SoftDropMass<150"
match_gen_tau_0 = "match_gen_tau==0"
match_gen_tau_1 = "match_gen_tau==1"
match_gen_tau_2 = "match_gen_tau==2"
veto_emu = "match_gen_emu==0"
match_reco_taus = "match_hps_tau==2"
match_gen_hav = "match_gen_hav>0"
match_gen_hav_0 = "match_gen_hav==0"

htl_cut = "ak8jets_probHttOverLepton>0.5"

pt_range_A = "ak8jets_Pt>250 && ak8jets_Pt<350"
pt_range_B = "ak8jets_Pt>350 && ak8jets_Pt<500"
pt_range_C = "ak8jets_Pt>500 && ak8jets_Pt<750"
pt_range_D = "ak8jets_Pt>750"

for sample in sample_list:
    df_dict[sample] = R.RDataFrame("ak8tree", fileset[sample], interested_variables)
    
    # each type will be matched with 2 reco taus and cutted with softdrop Higgs mass window
    # Type 1 matched with 2 gen taus
    df_dict[sample+'_T1'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_2).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T1_A'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_A).Filter(match_gen_tau_2).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T1_B'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_B).Filter(match_gen_tau_2).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T1_C'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_C).Filter(match_gen_tau_2).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T1_D'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_D).Filter(match_gen_tau_2).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    
    # Type 2 matched with 1 gen tau
    df_dict[sample+'_T2'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_1).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T2_A'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_A).Filter(match_gen_tau_1).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T2_B'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_B).Filter(match_gen_tau_1).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T2_C'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_C).Filter(match_gen_tau_1).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    df_dict[sample+'_T2_D'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(pt_range_D).Filter(match_gen_tau_1).Filter(veto_emu).Filter(match_reco_taus).Filter(htl_cut)
    
    # Type 3 matched with 0 gen tau and at least 1 heavy gen jet
    df_dict[sample+'_T3'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(veto_emu).Filter(match_reco_taus).Filter(match_gen_hav).Filter(htl_cut)
    df_dict[sample+'_T3_A'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(pt_range_A).Filter(veto_emu).Filter(match_reco_taus).Filter(match_gen_hav).Filter(htl_cut)
    df_dict[sample+'_T3_B'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(pt_range_B).Filter(veto_emu).Filter(match_reco_taus).Filter(match_gen_hav).Filter(htl_cut)
    df_dict[sample+'_T3_C'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(pt_range_C).Filter(veto_emu).Filter(match_reco_taus).Filter(match_gen_hav).Filter(htl_cut)
    df_dict[sample+'_T3_D'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(pt_range_D).Filter(veto_emu).Filter(match_reco_taus).Filter(match_gen_hav).Filter(htl_cut)
    
    # Type 4 matched with 0 gen taus and 0 heavy gen jet
    df_dict[sample+'_T4'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(match_gen_hav_0).Filter(veto_emu).Filter(match_reco_taus).Filter(veto_emu).Filter(htl_cut)
    df_dict[sample+'_T4_A'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(match_gen_hav_0).Filter(pt_range_A).Filter(veto_emu).Filter(match_reco_taus).Filter(veto_emu).Filter(htl_cut)
    df_dict[sample+'_T4_B'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(match_gen_hav_0).Filter(pt_range_B).Filter(veto_emu).Filter(match_reco_taus).Filter(veto_emu).Filter(htl_cut)
    df_dict[sample+'_T4_C'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(match_gen_hav_0).Filter(pt_range_C).Filter(veto_emu).Filter(match_reco_taus).Filter(veto_emu).Filter(htl_cut)
    df_dict[sample+'_T4_D'] = df_dict[sample].Filter(eta_cut).Filter(mass_cut).Filter(match_gen_tau_0).Filter(match_gen_hav_0).Filter(pt_range_D).Filter(veto_emu).Filter(match_reco_taus).Filter(veto_emu).Filter(htl_cut)
    
type_name = ['T1', 'T2', 'T3', 'T4', 'T1_A', 'T2_A', 'T3_A', 'T4_A', 'T1_B', 'T2_B', 'T3_B', 'T4_B', 'T1_C', 'T2_C', 'T3_C', 'T4_C', 'T1_D', 'T2_D', 'T3_D', 'T4_D']

for sample in Sig_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 1000, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverQCD'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverQCD', f'{sample}_{jet_type}_ak8jets_probHttOverQCD', 1000, 0, 1), "ak8jets_probHttOverQCD", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHtl'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHtl', f'{sample}_{jet_type}_ak8jets_probHtl', 1000, 0, 1), "ak8jets_probHtl", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverLepton'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverLepton', f'{sample}_{jet_type}_ak8jets_probHttOverLepton', 1000, 0, 1), "ak8jets_probHttOverLepton", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probQCD0hf'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probQCD0hf', f'{sample}_{jet_type}_ak8jets_probQCD0hf', 1000, 0, 1), "ak8jets_probQCD0hf", "true_weight").GetPtr()
                
        
for sample in SH_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 1000, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverQCD'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverQCD', f'{sample}_{jet_type}_ak8jets_probHttOverQCD', 1000, 0, 1), "ak8jets_probHttOverQCD", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHtl'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHtl', f'{sample}_{jet_type}_ak8jets_probHtl', 1000, 0, 1), "ak8jets_probHtl", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverLepton'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverLepton', f'{sample}_{jet_type}_ak8jets_probHttOverLepton', 1000, 0, 1), "ak8jets_probHttOverLepton", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probQCD0hf'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probQCD0hf', f'{sample}_{jet_type}_ak8jets_probQCD0hf', 1000, 0, 1), "ak8jets_probQCD0hf", "true_weight").GetPtr()
        
        
for sample in DY_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 1000, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverQCD'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverQCD', f'{sample}_{jet_type}_ak8jets_probHttOverQCD', 1000, 0, 1), "ak8jets_probHttOverQCD", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHtl'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHtl', f'{sample}_{jet_type}_ak8jets_probHtl', 1000, 0, 1), "ak8jets_probHtl", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverLepton'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverLepton', f'{sample}_{jet_type}_ak8jets_probHttOverLepton', 1000, 0, 1), "ak8jets_probHttOverLepton", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probQCD0hf'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probQCD0hf', f'{sample}_{jet_type}_ak8jets_probQCD0hf', 1000, 0, 1), "ak8jets_probQCD0hf", "true_weight").GetPtr()
        
for sample in TT_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 1000, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverQCD'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverQCD', f'{sample}_{jet_type}_ak8jets_probHttOverQCD', 1000, 0, 1), "ak8jets_probHttOverQCD", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHtl'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHtl', f'{sample}_{jet_type}_ak8jets_probHtl', 1000, 0, 1), "ak8jets_probHtl", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverLepton'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probHttOverLepton', f'{sample}_{jet_type}_ak8jets_probHttOverLepton', 1000, 0, 1), "ak8jets_probHttOverLepton", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_ak8jets_probQCD0hf'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_ak8jets_probQCD0hf', f'{sample}_{jet_type}_ak8jets_probQCD0hf', 1000, 0, 1), "ak8jets_probQCD0hf", "true_weight").GetPtr()

histo_file_out = R.TFile("histo_2hps_Masscut_Htlcut_0820.root", "RECREATE")
for key, value in histo_dict.items():
    value.Write()
    print(key + ' written')
histo_file_out.Close()

exit(0)
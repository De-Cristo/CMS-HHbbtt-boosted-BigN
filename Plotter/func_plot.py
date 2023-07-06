import ROOT as R
import re
import argparse
from array import array
import os
R.EnableImplicitMT()
R.gROOT.SetBatch(True)
    
path = "/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/" + "AK8based_Out_625/"

process_list = ['SMHH', 'VBFH', 'ggFH']
sample_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarSemi', 'TTbarDiLep']
Sig_list = ['SMHH']
SH_list = ['VBFH', 'ggFH']
DY_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
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
            
df_dict = {}
histo_dict = {}

interested_variables = {"ak8jets_SoftDropMass","true_weight","ak8jets_Pt","ak8jets_Eta","ak8jets_Mass","ak8jets_probHtt","match_gen_tau","match_gen_hav","bParticleNetTauAK8JetTags_probHtt"}

for sample in sample_list:
    df_dict[sample] = R.RDataFrame("ak8tree", fileset[sample], interested_variables)
    
    df_dict[sample+'_T1'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_S'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>60 && ak8jets_SoftDropMass<130").Filter("ak8jets_Pt>250").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_A'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250 && ak8jets_Pt<350").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_B'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>350 && ak8jets_Pt<500").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_C'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>500 && ak8jets_Pt<750").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_D'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>750 && ak8jets_Pt<1000").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T1_E'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>1000").Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_S'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>60 && ak8jets_SoftDropMass<130").Filter("ak8jets_Pt>250").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_A'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250 && ak8jets_Pt < 350").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_B'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>350 && ak8jets_Pt<500").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_C'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>500 && ak8jets_Pt<750").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_D'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>750 && ak8jets_Pt<1000").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T2_E'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>1000").Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_S'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>60 && ak8jets_SoftDropMass<130").Filter("ak8jets_Pt>250").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_A'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250 && ak8jets_Pt < 350").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_B'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>350 && ak8jets_Pt<500").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_C'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>500 && ak8jets_Pt<750").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_D'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>750 && ak8jets_Pt<1000").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T3_E'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>1000").Filter("match_gen_tau==0").Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_S'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>60 && ak8jets_SoftDropMass<130").Filter("ak8jets_Pt>250").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_A'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>250 && ak8jets_Pt < 350").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_B'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>350 && ak8jets_Pt<500").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_C'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>500 && ak8jets_Pt<750").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_D'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>750 && ak8jets_Pt<1000").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
    df_dict[sample+'_T4_E'] = df_dict[sample].Filter("abs(ak8jets_Eta)<2.5").Filter("ak8jets_SoftDropMass>30").Filter("ak8jets_Pt>1000").Filter("match_gen_tau==0").Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("match_hps_tau==2")
    
type_name = ['T1', 'T2', 'T3', 'T4', 'T1_A', 'T2_A', 'T3_A', 'T4_A', 'T1_B', 'T2_B', 'T3_B', 'T4_B', 'T1_C', 'T2_C', 'T3_C', 'T4_C', 'T1_D', 'T2_D', 'T3_D', 'T4_D', 'T1_E', 'T2_E', 'T3_E', 'T4_E', 'T1_S', 'T2_S', 'T3_S', 'T4_S']

for sample in Sig_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 200, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', 200, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', 200, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight").GetPtr()
        
for sample in SH_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 200, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', 200, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', 200, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight").GetPtr()
        
for sample in DY_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 200, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', 200, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', 200, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight").GetPtr()
        
for sample in TT_list:
    for jet_type in type_name:
        print(f'{sample}_{jet_type}')
        histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt', 200, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets', 200, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight").GetPtr()
        
        histo_dict[f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{sample}_{jet_type}'].Histo1D((f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets', 200, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight").GetPtr()

histo_file_out = R.TFile("histo_no_hps.root", "RECREATE")        
for key, value in histo_dict.items():
    value.Write()
    print(key + ' written')
histo_file_out.Close()

exit(0)
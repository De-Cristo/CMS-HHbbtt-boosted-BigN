import ROOT as R
import re
import argparse
from array import array
import os
R.EnableImplicitMT()
R.gROOT.SetBatch(True)

def add_lumi(year):
    lowX=0.55
    lowY=0.835
    lumi  = R.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.06)
    lumi.SetTextFont (   42 )
    if (year=="2018"): lumi.AddText("2018, 60 fb^{-1} (13 TeV)")
    if (year=="2017"): lumi.AddText("2017, 41 fb^{-1} (13 TeV)")
    if (year=="2016"): lumi.AddText("2016, 36 fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.11
    lowY=0.835
    lumi  = R.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.08)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.25
    lowY=0.835
    lumi  = R.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend():
        output = R.TLegend(0.5, 0.65, 0.92, 0.86, "", "brNDC")
        output.SetNColumns(2)
        output.SetLineWidth(0)
        output.SetLineStyle(0)
        output.SetFillStyle(0)
        output.SetBorderSize(0)
        output.SetTextFont(62)
        return output

def make_legend2():
        output = R.TLegend(0.45, 0.6, 0.92, 0.86, "", "brNDC")
        output.SetNColumns(2)
        output.SetLineWidth(0)
        output.SetLineStyle(0)
        output.SetFillStyle(0)
        output.SetBorderSize(0)
        output.SetTextFont(62)
        return output
    
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
    
type_name = ['T1', 'T2', 'T3', 'T4', 'T1_A', 'T2_A', 'T3_A', 'T4_A', 'T1_B', 'T2_B', 'T3_B', 'T4_B', 'T1_C', 'T2_C', 'T3_C', 'T4_C', 'T1_D', 'T2_D', 'T3_D', 'T4_D', 'T1_E', 'T2_E', 'T3_E', 'T4_E', 'T1_S', 'T2_S', 'T3_S', 'T4_S']


histo_file_in = R.TFile("histo_hps.root", "READ")
histo_names = histo_file_in.GetListOfKeys()

for histo_name in histo_names:
    # print(histo_name.GetName())
    histo_dict[histo_name.GetName()] = histo_file_in.Get(histo_name.GetName())
    # histo_dict[histo_name.GetName()].SetDirectory(R.gROOT)
    
for jet_type in type_name:
    histo_dict[f'SMHH_{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Scale(0.01)
    histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = histo_dict[f'SMHH_{jet_type}_bParticleNetTauAK8JetTags_probHtt']
    histo_dict[f'SMHH_{jet_type}_hps_tau1_DeepTauVSJets'].Scale(0.01)
    histo_dict[f'{jet_type}_hps_tau1_DeepTauVSJets'] = histo_dict[f'SMHH_{jet_type}_hps_tau1_DeepTauVSJets']
    histo_dict[f'SMHH_{jet_type}_hps_tau2_DeepTauVSJets'].Scale(0.01)
    histo_dict[f'{jet_type}_hps_tau2_DeepTauVSJets'] = histo_dict[f'SMHH_{jet_type}_hps_tau2_DeepTauVSJets']
    
for sample in sample_list[1:]:
    for jet_type in type_name:
        histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] + histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt']
        histo_dict[f'{jet_type}_hps_tau1_DeepTauVSJets'] = histo_dict[f'{jet_type}_hps_tau1_DeepTauVSJets'] + histo_dict[f'{sample}_{jet_type}_hps_tau1_DeepTauVSJets']
        histo_dict[f'{jet_type}_hps_tau2_DeepTauVSJets'] = histo_dict[f'{jet_type}_hps_tau2_DeepTauVSJets'] + histo_dict[f'{sample}_{jet_type}_hps_tau2_DeepTauVSJets']
        
import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6], dtype=np.float64)
names = ['pT[250, Inf]', 'pT[250, 350]', 'pT[350, 500]', 'pT[500, 750]', 'pT[750, 1000]', 'pT[1000, Inf]', 'mass [60, 130]']
y = {}
y['T1'] = np.array([],dtype=np.float64)
y['T2'] = np.array([],dtype=np.float64)
y['T3'] = np.array([],dtype=np.float64)
y['T4'] = np.array([],dtype=np.float64)
        
for jet_type in type_name:
    print(f'{jet_type}_bParticleNetTauAK8JetTags_probHtt')
    integral = histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Integral()
    # print(integral)
    if 'T1' in jet_type:
        y['T1'] = np.append(y['T1'], integral)
    if 'T2' in jet_type:
        y['T2'] = np.append(y['T2'], integral)
    if 'T3' in jet_type:
        y['T3'] = np.append(y['T3'], integral)
    if 'T4' in jet_type:
        y['T4'] = np.append(y['T4'], integral)
        
print(y)

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

leg = R.TLegend(0.60,0.60,0.80,0.90)
leg.AddEntry(histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'], "Type 1", "l")
leg.AddEntry(histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'], "Type 2", "l")
leg.AddEntry(histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'], "Type 3", "l")
leg.AddEntry(histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'], "Type 4", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Score_T124.pdf')
c.SaveAs('Score_T124.png')

## Efficiency plot

histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_A_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_A_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_A_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_A_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_B_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_B_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_B_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_B_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_C_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_C_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_C_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_C_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_D_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_D_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_D_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_D_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_E_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_E_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_E_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_E_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_S_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_S_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_S_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)
histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_S_bParticleNetTauAK8JetTags_probHtt", "", 200, 0, 1)

histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_A_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_A_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_A_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_A_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_A_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_A_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_A_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_A_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_B_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_B_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_B_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_B_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_B_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_B_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_B_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_B_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_C_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_C_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_C_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_C_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_C_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_C_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_C_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_C_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_D_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_D_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_D_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_D_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_D_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_D_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_D_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_D_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_E_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_E_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_E_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_E_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_E_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_E_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_E_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_E_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

histo_dict['Eff_T1_S_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T1_S_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T2_S_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T2_S_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T3_S_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T3_S_hps_tau1_DeepTauVSJets", "", 200, 0, 1)
histo_dict['Eff_T4_S_hps_tau1_DeepTauVSJets'] = R.TH1F("Eff_T4_S_hps_tau1_DeepTauVSJets", "", 200, 0, 1)

for jet_type in type_name:
    for ibin in range(0,200):
        eff = histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Integral(ibin, 200)/histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Integral()
        histo_dict[f'Eff_{jet_type}_bParticleNetTauAK8JetTags_probHtt'].SetBinContent(ibin+1, eff)
        
for jet_type in type_name:
    for ibin in range(0,200):
        eff = histo_dict[f'{jet_type}_hps_tau1_DeepTauVSJets'].Integral(ibin, 200)/histo_dict[f'{jet_type}_hps_tau1_DeepTauVSJets'].Integral()
        histo_dict[f'Eff_{jet_type}_hps_tau1_DeepTauVSJets'].SetBinContent(ibin+1, eff)
        
c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

leg = R.TLegend(0.1,0.15,0.4,0.4)
leg.AddEntry(histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'], "Type 1", "l")
leg.AddEntry(histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'], "Type 2", "l")
leg.AddEntry(histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'], "Type 3", "l")
leg.AddEntry(histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'], "Type 4", "l")
leg.SetFillColorAlpha(1,0.1)
leg.SetLineColorAlpha(1,0.0)
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency.pdf')
c.SaveAs('Efficiency.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'].SetLineWidth(2)
histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'].Draw('histo')
histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'].GetXaxis().SetTitle("tau1_DeepTauVSJets")
histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'].SetLineWidth(2)
histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'].Draw('histo same')

histo_dict['Eff_T3_hps_tau1_DeepTauVSJets'].SetLineWidth(2)
histo_dict['Eff_T3_hps_tau1_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_hps_tau1_DeepTauVSJets'].Draw('histo same')

histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'].SetLineWidth(2)
histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'].Draw('histo same')

leg = R.TLegend(0.6,0.7,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'], "Type 1", "l")
leg.AddEntry(histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'], "Type 2", "l")
leg.AddEntry(histo_dict['Eff_T3_hps_tau1_DeepTauVSJets'], "Type 3", "l")
leg.AddEntry(histo_dict['Eff_T4_hps_tau1_DeepTauVSJets'], "Type 4", "l")
leg.SetFillColorAlpha(1,0.1)
leg.SetLineColorAlpha(1,0.0)
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency_DeepTau1.pdf')
c.SaveAs('Efficiency_DeepTau1.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#958CDD"),1.0)
histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#016269"),1.0)
histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')


leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(750,1000)", "l")
leg.AddEntry(histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(1000,Inf)", "l")
leg.AddEntry(histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Mass(60,130)", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency_T1_Pt_logy.pdf')
c.SaveAs('Efficiency_T1_Pt_logy.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#958CDD"),1.0)
histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#016269"),1.0)
histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')


leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(750,1000)", "l")
leg.AddEntry(histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(1000,Inf)", "l")
leg.AddEntry(histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Mass(60,130)", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency_T2_Pt_logy.pdf')
c.SaveAs('Efficiency_T2_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#958CDD"),1.0)
histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#016269"),1.0)
histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')


leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(750,1000)", "l")
leg.AddEntry(histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(1000,Inf)", "l")
leg.AddEntry(histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Mass(60,130)", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency_T3_Pt_logy.pdf')
c.SaveAs('Efficiency_T3_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#958CDD"),1.0)
histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#016269"),1.0)
histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')


leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(750,1000)", "l")
leg.AddEntry(histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(1000,Inf)", "l")
leg.AddEntry(histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Mass(60,130)", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetLogy()
c.SaveAs('Efficiency_T4_Pt_logy.pdf')
c.SaveAs('Efficiency_T4_Pt_logy.png')


import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline

fprs_T2 = []
fprs_T3 = []
fprs_T4 = []
tprs = []


for ibin in range(0,200):
    tprs.append(histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2.append(histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3.append(histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4.append(histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
tprs = np.array(list(reversed(tprs)))
fprs_T2 = np.array(list(reversed(fprs_T2)))
fprs_T3 = np.array(list(reversed(fprs_T3)))
fprs_T4 = np.array(list(reversed(fprs_T4)))

# tpr_spline = InterpolatedUnivariateSpline(fprs_T2, tprs)
# # Define the range of fprs for evaluation
# smooth_fprs = np.linspace(min(fprs_T2), max(fprs_T2), 1000)
# # Evaluate the spline function to get the smoothed TPR values
# smooth_tprs = tpr_spline(smooth_fprs)

# x2 = smooth_fprs
# y2 = smooth_tprs

x2 = fprs_T2
y2 = tprs

# tpr_spline = InterpolatedUnivariateSpline(fprs_T3, tprs)
# # Define the range of fprs for evaluation
# smooth_fprs = np.linspace(min(fprs_T3), max(fprs_T3), 1000)
# # Evaluate the spline function to get the smoothed TPR values
# smooth_tprs = tpr_spline(smooth_fprs)

# x3 = smooth_fprs
# y3 = smooth_tprs

x3 = fprs_T3
y3 = tprs

# tpr_spline = InterpolatedUnivariateSpline(fprs_T4, tprs)
# # Define the range of fprs for evaluation
# smooth_fprs = np.linspace(min(fprs_T4), max(fprs_T4), 1000)
# # Evaluate the spline function to get the smoothed TPR values
# smooth_tprs = tpr_spline(smooth_fprs)

# x4 = smooth_fprs
# y4 = smooth_tprs

x4 = fprs_T4
y4 = tprs

gr2 = R.TGraph( 200, x2, y2 )
gr2.SetName("roccurve_2")

gr3 = R.TGraph( 200, x3, y3 )
gr3.SetName("roccurve_3")

gr4 = R.TGraph( 200, x4, y4 )
gr4.SetName("roccurve_4")


c = R.TCanvas()
c.SetGridx()
c.SetGridy()
c.SetLogy(0)

gr2.SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
gr2.SetLineWidth(2)
gr2.GetXaxis().SetTitle("FPRs")
gr2.GetYaxis().SetTitle("TPRs")

gr3.SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
gr3.SetLineWidth(2)

gr4.SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
gr4.SetLineWidth(2)

gr2.Draw()
gr3.Draw("SAME")
gr4.Draw("SAME")

lg = R.TLegend(0.45,0.15,0.85,0.35)
lg.AddEntry(gr2,'Type1 vs Type 2','l')
lg.AddEntry(gr3,'Type1 vs Type 3','l')
lg.AddEntry(gr4,'Type1 vs Type 4','l')

lg.SetFillColorAlpha(1,0.1)
lg.SetLineColorAlpha(1,0.0)
lg.Draw("SAME")
c.SaveAs("ROC.pdf")
c.SaveAs("ROC.png")


c = R.TCanvas()
c.SetGridx()
c.SetGridy()
c.SetLogy()

gr2.SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
gr2.SetLineWidth(2)
gr2.GetXaxis().SetTitle("FPRs")
gr2.GetXaxis().SetRangeUser(0.0, 0.3)
gr2.GetYaxis().SetTitle("TPRs")

gr3.SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
gr3.SetLineWidth(2)

gr4.SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
gr4.SetLineWidth(2)

gr2.Draw()
gr3.Draw("SAME")
gr4.Draw("SAME")

lg = R.TLegend(0.45,0.15,0.85,0.35)
lg.AddEntry(gr2,'Type1 vs Type 2','l')
lg.AddEntry(gr3,'Type1 vs Type 3','l')
lg.AddEntry(gr4,'Type1 vs Type 4','l')

lg.SetFillColorAlpha(1,0.1)
lg.SetLineColorAlpha(1,0.0)
lg.Draw("SAME")
c.SaveAs("ROC_logy.pdf")
c.SaveAs("ROC_logy.png")


c = R.TCanvas()
c.SetGridx()
c.SetGridy()
c.SetLogy()
c.SetLogx()

gr2.SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
gr2.SetLineWidth(2)
gr2.GetXaxis().SetTitle("FPRs")
gr2.GetYaxis().SetTitle("TPRs")

gr3.SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
gr3.SetLineWidth(2)

gr4.SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
gr4.SetLineWidth(2)

gr2.Draw()
gr3.Draw("SAME")
gr4.Draw("SAME")

lg = R.TLegend(0.45,0.15,0.85,0.35)
lg.AddEntry(gr2,'Type1 vs Type 2','l')
lg.AddEntry(gr3,'Type1 vs Type 3','l')
lg.AddEntry(gr4,'Type1 vs Type 4','l')

lg.SetFillColorAlpha(1,0.1)
lg.SetLineColorAlpha(1,0.0)
lg.Draw("SAME")
c.SaveAs("ROC_logy_logx.pdf")
c.SaveAs("ROC_logy_logx.png")




tprs_A = []
tprs_B = []
tprs_C = []
tprs_D = []
tprs_E = []
tprs_S = []

fprs_T2_A = []
fprs_T2_B = []
fprs_T2_C = []
fprs_T2_D = []
fprs_T2_E = []
fprs_T2_S = []

fprs_T3_A = []
fprs_T3_B = []
fprs_T3_C = []
fprs_T3_D = []
fprs_T3_E = []
fprs_T3_S = []

fprs_T4_A = []
fprs_T4_B = []
fprs_T4_C = []
fprs_T4_D = []
fprs_T4_E = []
fprs_T4_S = []


for ibin in range(0,200):
    tprs_A.append(histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_A.append(histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_A.append(histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_A.append(histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    tprs_B.append(histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_B.append(histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_B.append(histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_B.append(histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    tprs_C.append(histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_C.append(histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_C.append(histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_C.append(histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    tprs_D.append(histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_D.append(histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_D.append(histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_D.append(histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    tprs_E.append(histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_E.append(histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_E.append(histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_E.append(histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    tprs_S.append(histo_dict['Eff_T1_S_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T2_S.append(histo_dict['Eff_T2_S_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T3_S.append(histo_dict['Eff_T3_S_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    fprs_T4_S.append(histo_dict['Eff_T4_S_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
    
tprs_A = np.array(list(reversed(tprs_A)))
tprs_B = np.array(list(reversed(tprs_B)))
tprs_C = np.array(list(reversed(tprs_C)))
tprs_D = np.array(list(reversed(tprs_D)))
tprs_E = np.array(list(reversed(tprs_E)))
tprs_S = np.array(list(reversed(tprs_S)))

fprs_T2_A = np.array(list(reversed(fprs_T2_A)))
fprs_T2_B = np.array(list(reversed(fprs_T2_B)))
fprs_T2_C = np.array(list(reversed(fprs_T2_C)))
fprs_T2_D = np.array(list(reversed(fprs_T2_D)))
fprs_T2_E = np.array(list(reversed(fprs_T2_E)))
fprs_T2_S = np.array(list(reversed(fprs_T2_S)))

fprs_T3_A = np.array(list(reversed(fprs_T3_A)))
fprs_T3_B = np.array(list(reversed(fprs_T3_B)))
fprs_T3_C = np.array(list(reversed(fprs_T3_C)))
fprs_T3_D = np.array(list(reversed(fprs_T3_D)))
fprs_T3_E = np.array(list(reversed(fprs_T3_E)))
fprs_T3_S = np.array(list(reversed(fprs_T3_S)))
    
fprs_T4_A = np.array(list(reversed(fprs_T4_A)))
fprs_T4_B = np.array(list(reversed(fprs_T4_B)))
fprs_T4_C = np.array(list(reversed(fprs_T4_C)))
fprs_T4_D = np.array(list(reversed(fprs_T4_D)))
fprs_T4_E = np.array(list(reversed(fprs_T4_E)))
fprs_T4_S = np.array(list(reversed(fprs_T4_S)))


xA = fprs_T4_A
xB = fprs_T4_B
xC = fprs_T4_C
xD = fprs_T4_D
xE = fprs_T4_E
xS = fprs_T4_S


yA = tprs_A
yB = tprs_B
yC = tprs_C
yD = tprs_D
yE = tprs_E
yS = tprs_S

grA = R.TGraph( 200, xA, yA )
grA.SetName("roccurve_A")

grB = R.TGraph( 200, xB, yB )
grB.SetName("roccurve_B")

grC = R.TGraph( 200, xC, yC )
grC.SetName("roccurve_C")

grD = R.TGraph( 200, xD, yD )
grD.SetName("roccurve_D")

grE = R.TGraph( 200, xE, yE )
grE.SetName("roccurve_E")

grS = R.TGraph( 200, xS, yS )
grS.SetName("roccurve_S")



c = R.TCanvas("c","c",800,800)
c.SetGrid()
c.SetLogy()

grA.SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
grA.SetLineWidth(2)

grA.GetXaxis().SetTitle("FPRs")
grA.GetXaxis().SetRangeUser(0.0, 0.3)
grA.GetYaxis().SetTitle("TPRs")

grB.SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
grB.SetLineWidth(2)
grC.SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
grC.SetLineWidth(2)
grD.SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
grD.SetLineWidth(2)
grE.SetLineColorAlpha(R.TColor.GetColor("#958CDD"),1.0)
grE.SetLineWidth(2)
grS.SetLineColorAlpha(R.TColor.GetColor("#016269"),1.0)
grS.SetLineWidth(2)

grA.Draw("APL")
grB.Draw("PL same")
grC.Draw("PL same")
grD.Draw("PL same")
grE.Draw("PL same")
grS.Draw("PL same")

lg = R.TLegend(0.45,0.15,0.85,0.35)
lg.AddEntry(grA,'Type1 vs Type 4 Pt[250, 350]','l')
lg.AddEntry(grB,'Type1 vs Type 4 Pt[350, 500]','l')
lg.AddEntry(grC,'Type1 vs Type 4 Pt[500, 750]','l')
lg.AddEntry(grD,'Type1 vs Type 4 Pt[750, 1000]','l')
lg.AddEntry(grE,'Type1 vs Type 4 Pt[1000, Inf]','l')
lg.AddEntry(grS,'Type1 vs Type 4 Mass[60, 130]','l')
lg.Draw("SAME")

c.SaveAs("ROC_logy_pT.pdf")
c.SaveAs("ROC_logy_pT.png")




fprs_DT = []
fprs_PNET = []
tprs_DT = []
tprs_PNET = []


for ibin in range(0,200):
    tprs_DT.append(histo_dict['Eff_T1_hps_tau1_DeepTauVSJets'].GetBinContent(ibin+1))
    fprs_DT.append(histo_dict['Eff_T2_hps_tau1_DeepTauVSJets'].GetBinContent(ibin+1))
    fprs_PNET.append(histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    tprs_PNET.append(histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].GetBinContent(ibin+1))
    
tprs_DT = np.array(list(reversed(tprs_DT)))
fprs_DT = np.array(list(reversed(fprs_DT)))
tprs_PNET = np.array(list(reversed(tprs_PNET)))
fprs_PNET = np.array(list(reversed(fprs_PNET)))

xDT = fprs_DT
yDT = tprs_DT

xPNET = fprs_PNET
yPNET = tprs_PNET

grDT = R.TGraph( 200, xDT, yDT )
grDT.SetName("roccurve_DT")

grPNET = R.TGraph( 200, xPNET, yPNET )
grPNET.SetName("roccurve_PNET")

c = R.TCanvas()
c.SetGridx()
c.SetGridy()
c.SetLogy()

grDT.SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
grDT.SetLineWidth(2)
grDT.GetXaxis().SetTitle("FPRs")
grDT.GetXaxis().SetRangeUser(0.0, 0.3)
grDT.GetYaxis().SetTitle("TPRs")

grPNET.SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
grPNET.SetLineWidth(2)

grDT.Draw()
grPNET.Draw("SAME")

lg = R.TLegend(0.45,0.15,0.85,0.35)
lg.AddEntry(grDT,'Type1 vs Type 2 DeepTau (Tau1)','l')
lg.AddEntry(grPNET,'Type1 vs Type 3 ParticleNet','l')

lg.SetFillColorAlpha(1,0.1)
lg.SetLineColorAlpha(1,0.0)
lg.Draw("SAME")

c.SaveAs("ROC_logy_DTvsPNET.pdf")
c.SaveAs("ROC_logy_DTvsPNET.png")
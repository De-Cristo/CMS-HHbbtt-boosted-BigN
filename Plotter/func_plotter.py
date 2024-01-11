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

path = "/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/" + "AK8based_Out_810/"

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
# # for process in process_list:
# for process in sample_list:
#     for file in os.listdir(path+process):
#         if file.endswith(".root"):
#             fileset[process].append(path+'/'+process+'/'+file)
            
df_dict = {}
histo_dict = {}

interested_variables = {"ak8jets_SoftDropMass","true_weight","ak8jets_Pt","ak8jets_Eta","ak8jets_Mass","ak8jets_probHtt","match_gen_tau","match_gen_hav","bParticleNetTauAK8JetTags_probHtt"}
    
type_name = ['T1', 'T2', 'T3', 'T4', 'T1_A', 'T2_A', 'T3_A', 'T4_A', 'T1_B', 'T2_B', 'T3_B', 'T4_B', 'T1_C', 'T2_C', 'T3_C', 'T4_C', 'T1_D', 'T2_D', 'T3_D', 'T4_D']


histo_file_in = R.TFile("histo_2hps_Masscut_0820.root", "READ")
histo_names = histo_file_in.GetListOfKeys()

for histo_name in histo_names:
    # print(histo_name.GetName())
    histo_dict[histo_name.GetName()] = histo_file_in.Get(histo_name.GetName())
    # histo_dict[histo_name.GetName()].SetDirectory(R.gROOT)
    
for jet_type in type_name:
    histo_dict[f'SMHH_{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Scale(0.074)
    histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = histo_dict[f'SMHH_{jet_type}_bParticleNetTauAK8JetTags_probHtt']
    
    histo_dict[f'SMHH_{jet_type}_ak8jets_probHttOverQCD'].Scale(0.074)
    histo_dict[f'{jet_type}_ak8jets_probHttOverQCD'] = histo_dict[f'SMHH_{jet_type}_ak8jets_probHttOverQCD']
    
    histo_dict[f'SMHH_{jet_type}_ak8jets_probQCD0hf'].Scale(0.074)
    histo_dict[f'{jet_type}_ak8jets_probQCD0hf'] = histo_dict[f'SMHH_{jet_type}_ak8jets_probQCD0hf']
    
for sample in sample_list[1:]:
    for jet_type in type_name:
        histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] = histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'] + histo_dict[f'{sample}_{jet_type}_bParticleNetTauAK8JetTags_probHtt']
        histo_dict[f'{jet_type}_ak8jets_probHttOverQCD'] = histo_dict[f'{jet_type}_ak8jets_probHttOverQCD'] + histo_dict[f'{sample}_{jet_type}_ak8jets_probHttOverQCD']
        histo_dict[f'{jet_type}_ak8jets_probQCD0hf'] = histo_dict[f'{jet_type}_ak8jets_probQCD0hf'] + histo_dict[f'{sample}_{jet_type}_ak8jets_probQCD0hf']
        
import numpy as np
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
        
color_dict = {}
color_dict['T4'] = "#D05426"
color_dict['T3'] = "#731512"
color_dict['T2'] = "#F4E85E"
color_dict['T1'] = "#322E95"

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].SetTitle(" ")
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['T4_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
histo_dict['T1_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['T2_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['T3_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
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
c.SetTitle(" ")
c.SetLogy()
c.SaveAs('Plots_0820/PNet_Htt_Score.pdf')
c.SaveAs('Plots_0820/PNet_Htt_Score.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['T4_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['T4_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['T4_ak8jets_probHttOverQCD'].SetTitle(" ")
histo_dict['T4_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['T4_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("ProbHttOverQCD")
histo_dict['T4_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")

histo_dict['T1_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['T1_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
histo_dict['T1_ak8jets_probHttOverQCD'].Draw('histo same')

histo_dict['T2_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['T2_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['T2_ak8jets_probHttOverQCD'].Draw('histo same')

histo_dict['T3_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['T3_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
histo_dict['T3_ak8jets_probHttOverQCD'].Draw('histo same')

leg = R.TLegend(0.60,0.60,0.80,0.90)
leg.AddEntry(histo_dict['T1_ak8jets_probHttOverQCD'], "Type 1", "l")
leg.AddEntry(histo_dict['T2_ak8jets_probHttOverQCD'], "Type 2", "l")
leg.AddEntry(histo_dict['T3_ak8jets_probHttOverQCD'], "Type 3", "l")
leg.AddEntry(histo_dict['T4_ak8jets_probHttOverQCD'], "Type 4", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetTitle(" ")
c.SetLogy()
c.SaveAs('Plots_0820/ProbHtt_over_QCD_Score.pdf')
c.SaveAs('Plots_0820/ProbHtt_over_QCD_Score.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['T4_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['T4_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['T4_ak8jets_probQCD0hf'].SetTitle(" ")
histo_dict['T4_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['T4_ak8jets_probQCD0hf'].GetXaxis().SetTitle("ProbHttOverQCDLep")
histo_dict['T4_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")

histo_dict['T1_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['T1_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
histo_dict['T1_ak8jets_probQCD0hf'].Draw('histo same')

histo_dict['T2_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['T2_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['T2_ak8jets_probQCD0hf'].Draw('histo same')

histo_dict['T3_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['T3_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
histo_dict['T3_ak8jets_probQCD0hf'].Draw('histo same')

leg = R.TLegend(0.60,0.60,0.80,0.90)
leg.AddEntry(histo_dict['T1_ak8jets_probQCD0hf'], "Type 1", "l")
leg.AddEntry(histo_dict['T2_ak8jets_probQCD0hf'], "Type 2", "l")
leg.AddEntry(histo_dict['T3_ak8jets_probQCD0hf'], "Type 3", "l")
leg.AddEntry(histo_dict['T4_ak8jets_probQCD0hf'], "Type 4", "l")
leg.Draw('same')
l1=add_lumi('2018')
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
c.SetTitle(" ")
c.SetLogy()
c.SaveAs('Plots_0820/ProbHtt_over_QCDLep_Score.pdf')
c.SaveAs('Plots_0820/ProbHtt_over_QCDLep_Score.png')

## Efficiency plot

histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_A_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_A_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_A_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_A_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_B_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_B_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_B_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_B_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_C_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_C_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_C_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_C_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_D_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_D_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_D_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_D_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T1_E_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T2_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T2_E_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T3_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T3_E_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)
histo_dict['Eff_T4_E_bParticleNetTauAK8JetTags_probHtt'] = R.TH1F("Eff_T4_E_bParticleNetTauAK8JetTags_probHtt", "", 1000, 0, 1)

histo_dict['Eff_T1_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_ak8jets_probHttOverQCD", "", 1000, 0, 1)

histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_A_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_A_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_A_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_A_ak8jets_probHttOverQCD", "", 1000, 0, 1)

histo_dict['Eff_T1_B_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_B_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_B_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_B_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_B_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_B_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_B_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_B_ak8jets_probHttOverQCD", "", 1000, 0, 1)

histo_dict['Eff_T1_C_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_C_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_C_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_C_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_C_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_C_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_C_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_C_ak8jets_probHttOverQCD", "", 1000, 0, 1)

histo_dict['Eff_T1_D_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_D_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_D_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_D_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_D_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_D_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_D_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_D_ak8jets_probHttOverQCD", "", 1000, 0, 1)

histo_dict['Eff_T1_E_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T1_E_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T2_E_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T2_E_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T3_E_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T3_E_ak8jets_probHttOverQCD", "", 1000, 0, 1)
histo_dict['Eff_T4_E_ak8jets_probHttOverQCD'] = R.TH1F("Eff_T4_E_ak8jets_probHttOverQCD", "", 1000, 0, 1)


histo_dict['Eff_T1_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_ak8jets_probQCD0hf", "", 1000, 0, 1)

histo_dict['Eff_T1_A_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_A_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_A_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_A_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_A_ak8jets_probQCD0hf", "", 1000, 0, 1)

histo_dict['Eff_T1_B_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_B_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_B_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_B_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_B_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_B_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_B_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_B_ak8jets_probQCD0hf", "", 1000, 0, 1)

histo_dict['Eff_T1_C_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_C_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_C_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_C_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_C_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_C_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_C_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_C_ak8jets_probQCD0hf", "", 1000, 0, 1)

histo_dict['Eff_T1_D_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_D_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_D_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_D_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_D_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_D_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_D_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_D_ak8jets_probQCD0hf", "", 1000, 0, 1)

histo_dict['Eff_T1_E_ak8jets_probQCD0hf'] = R.TH1F("Eff_T1_E_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T2_E_ak8jets_probQCD0hf'] = R.TH1F("Eff_T2_E_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T3_E_ak8jets_probQCD0hf'] = R.TH1F("Eff_T3_E_ak8jets_probQCD0hf", "", 1000, 0, 1)
histo_dict['Eff_T4_E_ak8jets_probQCD0hf'] = R.TH1F("Eff_T4_E_ak8jets_probQCD0hf", "", 1000, 0, 1)

for jet_type in type_name:
    for ibin in range(0,1000):
        eff = histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Integral(ibin, 1000)/histo_dict[f'{jet_type}_bParticleNetTauAK8JetTags_probHtt'].Integral()
        histo_dict[f'Eff_{jet_type}_bParticleNetTauAK8JetTags_probHtt'].SetBinContent(ibin+1, eff)
        
for jet_type in type_name:
    for ibin in range(0,1000):
        eff = histo_dict[f'{jet_type}_ak8jets_probHttOverQCD'].Integral(ibin, 1000)/histo_dict[f'{jet_type}_ak8jets_probHttOverQCD'].Integral()
        histo_dict[f'Eff_{jet_type}_ak8jets_probHttOverQCD'].SetBinContent(ibin+1, eff)
        
for jet_type in type_name:
    for ibin in range(0,1000):
        eff = histo_dict[f'{jet_type}_ak8jets_probQCD0hf'].Integral(ibin, 1000)/histo_dict[f'{jet_type}_ak8jets_probQCD0hf'].Integral()
        histo_dict[f'Eff_{jet_type}_ak8jets_probQCD0hf'].SetBinContent(ibin+1, eff)
        
c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T4_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['Eff_T2_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
histo_dict['Eff_T3_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
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
c.SaveAs('Plots_0820/Efficiency_PNetHtt.pdf')
c.SaveAs('Plots_0820/Efficiency_PNetHtt.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T4_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['Eff_T4_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['Eff_T4_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("probHttOverQCD")
histo_dict['Eff_T4_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T2_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['Eff_T2_ak8jets_probHttOverQCD'].Draw('histo same')

histo_dict['Eff_T3_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T3_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
histo_dict['Eff_T3_ak8jets_probHttOverQCD'].Draw('histo same')

histo_dict['Eff_T1_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T1_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
histo_dict['Eff_T1_ak8jets_probHttOverQCD'].Draw('histo same')

leg = R.TLegend(0.6,0.7,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_ak8jets_probHttOverQCD'], "Type 1", "l")
leg.AddEntry(histo_dict['Eff_T2_ak8jets_probHttOverQCD'], "Type 2", "l")
leg.AddEntry(histo_dict['Eff_T3_ak8jets_probHttOverQCD'], "Type 3", "l")
leg.AddEntry(histo_dict['Eff_T4_ak8jets_probHttOverQCD'], "Type 4", "l")
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
c.SaveAs('Plots_0820/Efficiency_PNetHttOverQCD.pdf')
c.SaveAs('Plots_0820/Efficiency_PNetHttOverQCD.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T4_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T4']),1.0)
histo_dict['Eff_T4_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['Eff_T4_ak8jets_probQCD0hf'].GetXaxis().SetTitle("probHttOverQCDLep")
histo_dict['Eff_T4_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")

histo_dict['Eff_T2_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T2_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T2']),1.0)
histo_dict['Eff_T2_ak8jets_probQCD0hf'].Draw('histo same')

histo_dict['Eff_T3_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T3_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T3']),1.0)
histo_dict['Eff_T3_ak8jets_probQCD0hf'].Draw('histo same')

histo_dict['Eff_T1_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T1_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor(color_dict['T1']),1.0)
histo_dict['Eff_T1_ak8jets_probQCD0hf'].Draw('histo same')

leg = R.TLegend(0.6,0.7,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_ak8jets_probQCD0hf'], "Type 1", "l")
leg.AddEntry(histo_dict['Eff_T2_ak8jets_probQCD0hf'], "Type 2", "l")
leg.AddEntry(histo_dict['Eff_T3_ak8jets_probQCD0hf'], "Type 3", "l")
leg.AddEntry(histo_dict['Eff_T4_ak8jets_probQCD0hf'], "Type 4", "l")
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
c.SaveAs('Plots_0820/Efficiency_PNetHttOverQCDLep.pdf')
c.SaveAs('Plots_0820/Efficiency_PNetHttOverQCDLep.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'].SetMaximum(1.1)

histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_A_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T1_B_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T1_C_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T1_D_bParticleNetTauAK8JetTags_probHtt'], "Type 1 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNET_Efficiency_T1_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNET_Efficiency_T1_Pt_logy.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'].SetMaximum(1.1)

histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')


leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T2_A_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T2_B_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T2_C_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T2_D_bParticleNetTauAK8JetTags_probHtt'], "Type 2 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNET_Efficiency_T2_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNET_Efficiency_T2_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'].SetMaximum(1.1)

histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T3_A_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T3_B_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T3_C_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T3_D_bParticleNetTauAK8JetTags_probHtt'], "Type 3 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNET_Efficiency_T3_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNET_Efficiency_T3_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].Draw('histo')
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'].SetMaximum(1.1)

histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T4_A_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T4_B_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T4_C_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T4_D_bParticleNetTauAK8JetTags_probHtt'], "Type 4 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNET_Efficiency_T4_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNET_Efficiency_T4_Pt_logy.png')


c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("probHttOverQCD")
histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'].SetMaximum(1.1)

histo_dict['Eff_T1_B_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T1_B_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T1_B_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T1_C_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T1_C_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T1_C_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T1_D_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T1_D_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_D_ak8jets_probHttOverQCD'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_A_ak8jets_probHttOverQCD'], "Type 1 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T1_B_ak8jets_probHttOverQCD'], "Type 1 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T1_C_ak8jets_probHttOverQCD'], "Type 1 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T1_D_ak8jets_probHttOverQCD'], "Type 1 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T1_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T1_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("probHttOverQCD")
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'].SetMaximum(1.1)

histo_dict['Eff_T2_B_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T2_B_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_B_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T2_C_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T2_C_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T2_C_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T2_D_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T2_D_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T2_D_ak8jets_probHttOverQCD'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T2_A_ak8jets_probHttOverQCD'], "Type 2 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T2_B_ak8jets_probHttOverQCD'], "Type 2 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T2_C_ak8jets_probHttOverQCD'], "Type 2 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T2_D_ak8jets_probHttOverQCD'], "Type 2 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T2_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T2_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("probHttOverQCD")
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'].SetMaximum(1.1)

histo_dict['Eff_T3_B_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T3_B_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T3_B_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T3_C_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T3_C_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_C_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T3_D_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T3_D_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T3_D_ak8jets_probHttOverQCD'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T3_A_ak8jets_probHttOverQCD'], "Type 3 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T3_B_ak8jets_probHttOverQCD'], "Type 3 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T3_C_ak8jets_probHttOverQCD'], "Type 3 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T3_D_ak8jets_probHttOverQCD'], "Type 3 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T3_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T3_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].Draw('histo')
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].GetXaxis().SetTitle("probHttOverQCD")
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'].SetMaximum(1.1)

histo_dict['Eff_T4_B_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T4_B_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T4_B_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T4_C_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T4_C_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T4_C_ak8jets_probHttOverQCD'].Draw('histosame')

histo_dict['Eff_T4_D_ak8jets_probHttOverQCD'].SetLineWidth(2)
histo_dict['Eff_T4_D_ak8jets_probHttOverQCD'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T4_D_ak8jets_probHttOverQCD'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T4_A_ak8jets_probHttOverQCD'], "Type 4 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T4_B_ak8jets_probHttOverQCD'], "Type 4 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T4_C_ak8jets_probHttOverQCD'], "Type 4 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T4_D_ak8jets_probHttOverQCD'], "Type 4 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T4_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCD_Efficiency_T4_Pt_logy.png')



c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].GetXaxis().SetTitle("probHttOverQCDLep")
histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T1_A_ak8jets_probQCD0hf'].SetMaximum(1.1)

histo_dict['Eff_T1_B_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T1_B_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T1_B_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T1_C_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T1_C_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T1_C_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T1_D_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T1_D_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T1_D_ak8jets_probQCD0hf'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T1_A_ak8jets_probQCD0hf'], "Type 1 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T1_B_ak8jets_probQCD0hf'], "Type 1 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T1_C_ak8jets_probQCD0hf'], "Type 1 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T1_D_ak8jets_probQCD0hf'], "Type 1 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T1_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T1_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].GetXaxis().SetTitle("probHttOverQCDLep")
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T2_A_ak8jets_probQCD0hf'].SetMaximum(1.1)

histo_dict['Eff_T2_B_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T2_B_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T2_B_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T2_C_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T2_C_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T2_C_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T2_D_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T2_D_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T2_D_ak8jets_probQCD0hf'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T2_A_ak8jets_probQCD0hf'], "Type 2 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T2_B_ak8jets_probQCD0hf'], "Type 2 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T2_C_ak8jets_probQCD0hf'], "Type 2 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T2_D_ak8jets_probQCD0hf'], "Type 2 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T2_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T2_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].GetXaxis().SetTitle("probHttOverQCDLep")
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T3_A_ak8jets_probQCD0hf'].SetMaximum(1.1)

histo_dict['Eff_T3_B_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T3_B_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T3_B_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T3_C_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T3_C_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T3_C_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T3_D_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T3_D_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T3_D_ak8jets_probQCD0hf'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T3_A_ak8jets_probQCD0hf'], "Type 3 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T3_B_ak8jets_probQCD0hf'], "Type 3 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T3_C_ak8jets_probQCD0hf'], "Type 3 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T3_D_ak8jets_probQCD0hf'], "Type 3 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T3_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T3_Pt_logy.png')

c = R.TCanvas()
R.gStyle.SetOptStat(0000)

histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#322E95"),1.0)
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].Draw('histo')
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].GetXaxis().SetTitle("probHttOverQCDLep")
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].GetYaxis().SetTitle("Efficiency")
histo_dict['Eff_T4_A_ak8jets_probQCD0hf'].SetMaximum(1.1)

histo_dict['Eff_T4_B_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T4_B_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#F4E85E"),1.0)
histo_dict['Eff_T4_B_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T4_C_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T4_C_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#731512"),1.0)
histo_dict['Eff_T4_C_ak8jets_probQCD0hf'].Draw('histosame')

histo_dict['Eff_T4_D_ak8jets_probQCD0hf'].SetLineWidth(2)
histo_dict['Eff_T4_D_ak8jets_probQCD0hf'].SetLineColorAlpha(R.TColor.GetColor("#D05426"),1.0)
histo_dict['Eff_T4_D_ak8jets_probQCD0hf'].Draw('histosame')

leg = R.TLegend(0.60,0.65,0.9,0.9)
leg.AddEntry(histo_dict['Eff_T4_A_ak8jets_probQCD0hf'], "Type 4 Pt(250,350)", "l")
leg.AddEntry(histo_dict['Eff_T4_B_ak8jets_probQCD0hf'], "Type 4 Pt(350,500)", "l")
leg.AddEntry(histo_dict['Eff_T4_C_ak8jets_probQCD0hf'], "Type 4 Pt(500,750)", "l")
leg.AddEntry(histo_dict['Eff_T4_D_ak8jets_probQCD0hf'], "Type 4 Pt(750,Inf)", "l")
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
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T4_Pt_logy.pdf')
c.SaveAs('Plots_0820/PNetoverQCDLep_Efficiency_T4_Pt_logy.png')

exit(0)

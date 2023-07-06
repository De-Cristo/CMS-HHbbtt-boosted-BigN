import ROOT as R
import re
import argparse
from array import array
import os
R.EnableImplicitMT()
R.gROOT.SetBatch(True)
from Plotter.plot_utils import *

path = "/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/" + "AK8based_Out_625/"

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

interested_variables = {"ak8jets_SoftDropMass","true_weight","ak8jets_Pt","ak8jets_Eta","ak8jets_Mass","ak8jets_probHtt","match_gen_tau","match_gen_hav","match_gen_emu","bParticleNetTauAK8JetTags_probHtt"}
for sample in sample_list:
    df_dict[sample] = R.RDataFrame("ak8tree", fileset[sample], interested_variables)
    
    # df_dict[sample] = df_dict[sample]\
    #                 .Filter("abs(ak8jets_Eta)<2.5")\
    #                 .Filter("ak8jets_SoftDropMass>30")\
    #                 .Filter("ak8jets_Pt>250")\
    #                 .Filter("match_gen_tau==2").Filter("match_gen_emu==0")#.Filter("bParticleNetTauAK8JetTags_probHtt<0.1")
    
    # df_dict[sample] = df_dict[sample]\
    #                 .Filter("abs(ak8jets_Eta)<2.5")\
    #                 .Filter("ak8jets_SoftDropMass>30")\
    #                 .Filter("ak8jets_Pt>250")\
    #                 .Filter("match_gen_tau==1").Filter("match_gen_emu==0")#.Filter("bParticleNetTauAK8JetTags_probHtt>0.9")
                    
    # df_dict[sample] = df_dict[sample]\
    #                 .Filter("abs(ak8jets_Eta)<2.5")\
    #                 .Filter("ak8jets_SoftDropMass>30")\
    #                 .Filter("ak8jets_Pt>250")\
    #                 .Filter("match_gen_tau==0")\
    #                 .Filter("match_gen_hav>0").Filter("match_gen_emu==0")#.Filter("ak8jets_Pt<400")
                    
    df_dict[sample] = df_dict[sample]\
                    .Filter("abs(ak8jets_Eta)<2.5")\
                    .Filter("ak8jets_SoftDropMass>30")\
                    .Filter("ak8jets_Pt>250")\
                    .Filter("match_gen_tau==0")\
                    .Filter("match_gen_hav==0").Filter("match_gen_emu==0")#.Filter("bParticleNetTauAK8JetTags_probHtt>0.9")
    
suffix = '_type4'

dimention = '1D'

if dimention == '1D':
    
    histo_dict['SMHH_ak8jets_SoftDropMass'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_SoftDropMass", "true_weight")

    histo_dict['SMHH_ak8jets_Mass'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_Mass", "true_weight")

    histo_dict['SMHH_ak8jets_probHtt'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 50, 0, 1), "ak8jets_probHtt", "true_weight")

    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 50, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight")
    
    histo_dict['SMHH_hps_tau1_DeepTauVSJets'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 50, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight")
    
    histo_dict['SMHH_hps_tau2_DeepTauVSJets'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 50, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight")

    histo_dict['SMHH_ak8jets_Pt'] = \
        df_dict['SMHH'].Histo1D((" ", " ", 100, 200, 1300), "ak8jets_Pt", "true_weight")

    print("SM HH done.")

    for DY_proc in DY_list:
        histo_dict[f'{DY_proc}_ak8jets_SoftDropMass'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_SoftDropMass", "true_weight")

        histo_dict[f'{DY_proc}_ak8jets_Mass'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_Mass", "true_weight")

        histo_dict[f'{DY_proc}_ak8jets_probHtt'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 50, 0, 1), "ak8jets_probHtt", "true_weight")

        histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 50, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight")
        
        histo_dict[f'{DY_proc}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight")
        
        histo_dict[f'{DY_proc}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight")

        histo_dict[f'{DY_proc}_ak8jets_Pt'] = \
        df_dict[f'{DY_proc}'].Histo1D((" ", " ", 100, 200, 1300), "ak8jets_Pt", "true_weight")

    histo_dict['DY_ak8jets_SoftDropMass'] = histo_dict['DY+Jets50To100_ak8jets_SoftDropMass'].GetPtr()
    histo_dict['DY_ak8jets_Mass'] = histo_dict['DY+Jets50To100_ak8jets_Mass'].GetPtr()
    histo_dict['DY_ak8jets_probHtt'] = histo_dict['DY+Jets50To100_ak8jets_probHtt'].GetPtr()
    histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'] = histo_dict['DY+Jets50To100_bParticleNetTauAK8JetTags_probHtt'].GetPtr()
    histo_dict['DY_hps_tau1_DeepTauVSJets'] = histo_dict['DY+Jets50To100_hps_tau1_DeepTauVSJets'].GetPtr()
    histo_dict['DY_hps_tau2_DeepTauVSJets'] = histo_dict['DY+Jets50To100_hps_tau2_DeepTauVSJets'].GetPtr()
    histo_dict['DY_ak8jets_Pt'] = histo_dict['DY+Jets50To100_ak8jets_Pt'].GetPtr()

    for DY_proc in DY_list[1:]:
        histo_dict['DY_ak8jets_SoftDropMass'] = histo_dict['DY_ak8jets_SoftDropMass'] + histo_dict[f'{DY_proc}_ak8jets_SoftDropMass'].GetPtr()
        histo_dict['DY_ak8jets_Mass'] = histo_dict['DY_ak8jets_Mass'] + histo_dict[f'{DY_proc}_ak8jets_Mass'].GetPtr()
        histo_dict['DY_ak8jets_probHtt'] = histo_dict['DY_ak8jets_probHtt'] + histo_dict[f'{DY_proc}_ak8jets_probHtt'].GetPtr()
        histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'] = histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'] + histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt'].GetPtr()
        histo_dict['DY_hps_tau1_DeepTauVSJets'] = histo_dict['DY_hps_tau1_DeepTauVSJets'] + histo_dict[f'{DY_proc}_hps_tau1_DeepTauVSJets'].GetPtr()
        histo_dict['DY_hps_tau2_DeepTauVSJets'] = histo_dict['DY_hps_tau2_DeepTauVSJets'] + histo_dict[f'{DY_proc}_hps_tau2_DeepTauVSJets'].GetPtr()
        histo_dict['DY_ak8jets_Pt'] = histo_dict['DY_ak8jets_Pt'] + histo_dict[f'{DY_proc}_ak8jets_Pt'].GetPtr()

    print("DY+Jets done.")


    for SH_proc in SH_list:
        histo_dict[f'{SH_proc}_ak8jets_SoftDropMass'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_SoftDropMass", "true_weight")

        histo_dict[f'{SH_proc}_ak8jets_Mass'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_Mass", "true_weight")

        histo_dict[f'{SH_proc}_ak8jets_probHtt'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 50, 0, 1), "ak8jets_probHtt", "true_weight")

        histo_dict[f'{SH_proc}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 50, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight")
        
        histo_dict[f'{SH_proc}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight")
        
        histo_dict[f'{SH_proc}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight")

        histo_dict[f'{SH_proc}_ak8jets_Pt'] = \
        df_dict[f'{SH_proc}'].Histo1D((" ", " ", 100, 200, 1300), "ak8jets_Pt", "true_weight")
    print("Single Higgs done.")

    for TT_proc in TT_list:
        print(TT_proc)
        histo_dict[f'{TT_proc}_ak8jets_SoftDropMass'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_SoftDropMass", "true_weight")

        # histo_dict[f'{TT_proc}_ak8jets_Mass'] = \
        # df_dict[f'{TT_proc}'].Histo1D((" ", " ", 40, 0, 400), "ak8jets_Mass", "true_weight")

        histo_dict[f'{TT_proc}_ak8jets_Pt'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 100, 200, 1300), "ak8jets_Pt", "true_weight")

        histo_dict[f'{TT_proc}_ak8jets_probHtt'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 50, 0, 1), "ak8jets_probHtt", "true_weight")

        histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 50, 0, 1), "bParticleNetTauAK8JetTags_probHtt", "true_weight")
        
        histo_dict[f'{TT_proc}_hps_tau1_DeepTauVSJets'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau1_DeepTauVSJets", "true_weight")
        
        histo_dict[f'{TT_proc}_hps_tau2_DeepTauVSJets'] = \
        df_dict[f'{TT_proc}'].Histo1D((" ", " ", 50, 0, 1), "hps_tau2_DeepTauVSJets", "true_weight")

    histo_dict['TT_ak8jets_SoftDropMass'] = histo_dict['TTbarHad_ak8jets_SoftDropMass'].GetPtr()
    # histo_dict['TT_ak8jets_Mass'] = histo_dict['TTbarHad_ak8jets_Mass'].GetPtr()
    histo_dict['TT_ak8jets_Pt'] = histo_dict['TTbarHad_ak8jets_Pt'].GetPtr()
    histo_dict['TT_ak8jets_probHtt'] = histo_dict['TTbarHad_ak8jets_probHtt'].GetPtr()
    histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'] = histo_dict['TTbarHad_bParticleNetTauAK8JetTags_probHtt'].GetPtr()
    histo_dict['TT_hps_tau1_DeepTauVSJets'] = histo_dict['TTbarHad_hps_tau1_DeepTauVSJets'].GetPtr()
    histo_dict['TT_hps_tau2_DeepTauVSJets'] = histo_dict['TTbarHad_hps_tau2_DeepTauVSJets'].GetPtr()


    for TT_proc in TT_list[1:]:
        print(TT_proc)
        histo_dict['TT_ak8jets_SoftDropMass'] = histo_dict['TT_ak8jets_SoftDropMass'] + histo_dict[f'{TT_proc}_ak8jets_SoftDropMass'].GetPtr()
        # histo_dict['TT_ak8jets_Mass'] = histo_dict['TT_ak8jets_Mass'] + histo_dict[f'{TT_proc}_ak8jets_Mass'].GetPtr()
        histo_dict['TT_ak8jets_Pt'] = histo_dict['TT_ak8jets_Pt'] + histo_dict[f'{TT_proc}_ak8jets_Pt'].GetPtr()
        histo_dict['TT_ak8jets_probHtt'] = histo_dict['TT_ak8jets_probHtt'] + histo_dict[f'{TT_proc}_ak8jets_probHtt'].GetPtr()
        histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'] = histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'] + histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt'].GetPtr()
        histo_dict['TT_hps_tau1_DeepTauVSJets'] = histo_dict['TT_hps_tau1_DeepTauVSJets'] + histo_dict[f'{TT_proc}_hps_tau1_DeepTauVSJets'].GetPtr()
        histo_dict['TT_hps_tau2_DeepTauVSJets'] = histo_dict['TT_hps_tau2_DeepTauVSJets'] + histo_dict[f'{TT_proc}_hps_tau2_DeepTauVSJets'].GetPtr()


    print("Plotting...")

    stack=R.THStack("stack"," ")
    histo_dict['ggFH_ak8jets_SoftDropMass'].SetFillColorAlpha(R.TColor.GetColor('#731512'),0.9)
    stack.Add(histo_dict['ggFH_ak8jets_SoftDropMass'].GetPtr())
    histo_dict['VBFH_ak8jets_SoftDropMass'].SetFillColorAlpha(R.TColor.GetColor('#D05426'),0.9)
    stack.Add(histo_dict['VBFH_ak8jets_SoftDropMass'].GetPtr())
    histo_dict['DY_ak8jets_SoftDropMass'].SetFillColorAlpha(R.TColor.GetColor('#F4E85E'),0.9)
    stack.Add(histo_dict['DY_ak8jets_SoftDropMass'])
    histo_dict['TT_ak8jets_SoftDropMass'].SetFillColorAlpha(R.TColor.GetColor('#322E95'),0.9)
    stack.Add(histo_dict['TT_ak8jets_SoftDropMass'])

    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    stack.Draw('histo')
    stack.GetXaxis().SetTitle("AK8Jet softdrop mass [GeV]")
    stack.GetYaxis().SetTitle("AK8Jet Yields")


    histo_dict['SMHH_ak8jets_SoftDropMass'].SetLineWidth(2)
    histo_dict['SMHH_ak8jets_SoftDropMass'].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict['SMHH_ak8jets_SoftDropMass'].Scale(0.01)
    histo_dict['SMHH_ak8jets_SoftDropMass'].Draw('histo same')

    leg = R.TLegend(0.60,0.60,0.90,0.90)
    leg.AddEntry(histo_dict['ggFH_ak8jets_SoftDropMass'].GetPtr(), "ggF H", "f")
    leg.AddEntry(histo_dict['VBFH_ak8jets_SoftDropMass'].GetPtr(), "VBF H", "f")
    leg.AddEntry(histo_dict['DY_ak8jets_SoftDropMass'], "DY", "f")
    leg.AddEntry(histo_dict['TT_ak8jets_SoftDropMass'], "TT", "f")
    leg.AddEntry(histo_dict['SMHH_ak8jets_SoftDropMass'].GetPtr(), "SM HH", "l")
    leg.Draw('same')
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'Plots/SoftDropMass{suffix}.png')
    c.SaveAs(f'Plots/SoftDropMass{suffix}.pdf')

    stack=R.THStack("stack"," ")
    histo_dict['ggFH_bParticleNetTauAK8JetTags_probHtt'].SetFillColorAlpha(R.TColor.GetColor('#731512'),0.9)
    stack.Add(histo_dict['ggFH_bParticleNetTauAK8JetTags_probHtt'].GetPtr())
    histo_dict['VBFH_bParticleNetTauAK8JetTags_probHtt'].SetFillColorAlpha(R.TColor.GetColor('#D05426'),0.9)
    stack.Add(histo_dict['VBFH_bParticleNetTauAK8JetTags_probHtt'].GetPtr())
    histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'].SetFillColorAlpha(R.TColor.GetColor('#F4E85E'),0.9)
    stack.Add(histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'])
    histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'].SetFillColorAlpha(R.TColor.GetColor('#322E95'),0.9)
    stack.Add(histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'])

    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    stack.Draw('histo')
    stack.GetXaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
    stack.GetYaxis().SetTitle("AK8Jet Yields")

    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'].SetLineWidth(2)
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'].Scale(0.01)
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'].Draw('histo same')

    leg = R.TLegend(0.40,0.60,0.70,0.90)
    leg.AddEntry(histo_dict['ggFH_bParticleNetTauAK8JetTags_probHtt'].GetPtr(), "ggF H", "f")
    leg.AddEntry(histo_dict['VBFH_bParticleNetTauAK8JetTags_probHtt'].GetPtr(), "VBF H", "f")
    leg.AddEntry(histo_dict['DY_bParticleNetTauAK8JetTags_probHtt'], "DY", "f")
    leg.AddEntry(histo_dict['TT_bParticleNetTauAK8JetTags_probHtt'], "TT", "f")
    leg.AddEntry(histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt'].GetPtr(), "SM HH", "l")
    leg.Draw('same')
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'Plots/ParticleNetTauAK8JetTags_probHtt{suffix}.png')
    c.SaveAs(f'Plots/ParticleNetTauAK8JetTags_probHtt{suffix}.pdf')
    
    
    stack=R.THStack("stack"," ")
    histo_dict['ggFH_hps_tau1_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#731512'),0.9)
    stack.Add(histo_dict['ggFH_hps_tau1_DeepTauVSJets'].GetPtr())
    histo_dict['VBFH_hps_tau1_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#D05426'),0.9)
    stack.Add(histo_dict['VBFH_hps_tau1_DeepTauVSJets'].GetPtr())
    histo_dict['DY_hps_tau1_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#F4E85E'),0.9)
    stack.Add(histo_dict['DY_hps_tau1_DeepTauVSJets'])
    histo_dict['TT_hps_tau1_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#322E95'),0.9)
    stack.Add(histo_dict['TT_hps_tau1_DeepTauVSJets'])
    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    stack.Draw('histo')
    stack.GetXaxis().SetTitle("hps tau1 DeepTauVSJets")
    stack.GetYaxis().SetTitle("AK8Jet Yields")
    
    histo_dict['SMHH_hps_tau1_DeepTauVSJets'].SetLineWidth(2)
    histo_dict['SMHH_hps_tau1_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict['SMHH_hps_tau1_DeepTauVSJets'].Scale(0.01)
    histo_dict['SMHH_hps_tau1_DeepTauVSJets'].Draw('histo same')
    
    leg = R.TLegend(0.40,0.60,0.70,0.90)
    leg.AddEntry(histo_dict['ggFH_hps_tau1_DeepTauVSJets'].GetPtr(), "ggF H", "f")
    leg.AddEntry(histo_dict['VBFH_hps_tau1_DeepTauVSJets'].GetPtr(), "VBF H", "f")
    leg.AddEntry(histo_dict['DY_hps_tau1_DeepTauVSJets'], "DY", "f")
    leg.AddEntry(histo_dict['TT_hps_tau1_DeepTauVSJets'], "TT", "f")
    leg.AddEntry(histo_dict['SMHH_hps_tau1_DeepTauVSJets'].GetPtr(), "SM HH", "l")
    leg.Draw('same')
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'Plots/hps_tau1_DeepTauVSJets{suffix}.png')
    c.SaveAs(f'Plots/hps_tau1_DeepTauVSJets{suffix}.pdf')
    
    
    
    stack=R.THStack("stack"," ")
    histo_dict['ggFH_hps_tau2_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#731512'),0.9)
    stack.Add(histo_dict['ggFH_hps_tau2_DeepTauVSJets'].GetPtr())
    histo_dict['VBFH_hps_tau2_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#D05426'),0.9)
    stack.Add(histo_dict['VBFH_hps_tau2_DeepTauVSJets'].GetPtr())
    histo_dict['DY_hps_tau2_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#F4E85E'),0.9)
    stack.Add(histo_dict['DY_hps_tau2_DeepTauVSJets'])
    histo_dict['TT_hps_tau2_DeepTauVSJets'].SetFillColorAlpha(R.TColor.GetColor('#322E95'),0.9)
    stack.Add(histo_dict['TT_hps_tau2_DeepTauVSJets'])
    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    stack.Draw('histo')
    stack.GetXaxis().SetTitle("hps tau2 DeepTauVSJets")
    stack.GetYaxis().SetTitle("AK8Jet Yields")
    
    histo_dict['SMHH_hps_tau2_DeepTauVSJets'].SetLineWidth(2)
    histo_dict['SMHH_hps_tau2_DeepTauVSJets'].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict['SMHH_hps_tau2_DeepTauVSJets'].Scale(0.01)
    histo_dict['SMHH_hps_tau2_DeepTauVSJets'].Draw('histo same')
    
    leg = R.TLegend(0.40,0.60,0.70,0.90)
    leg.AddEntry(histo_dict['ggFH_hps_tau2_DeepTauVSJets'].GetPtr(), "ggF H", "f")
    leg.AddEntry(histo_dict['VBFH_hps_tau2_DeepTauVSJets'].GetPtr(), "VBF H", "f")
    leg.AddEntry(histo_dict['DY_hps_tau2_DeepTauVSJets'], "DY", "f")
    leg.AddEntry(histo_dict['TT_hps_tau2_DeepTauVSJets'], "TT", "f")
    leg.AddEntry(histo_dict['SMHH_hps_tau2_DeepTauVSJets'].GetPtr(), "SM HH", "l")
    leg.Draw('same')
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'Plots/hps_tau2_DeepTauVSJets{suffix}.png')
    c.SaveAs(f'Plots/hps_tau2_DeepTauVSJets{suffix}.pdf')



    stack=R.THStack("stack"," ")
    histo_dict['ggFH_ak8jets_Pt'].SetFillColorAlpha(R.TColor.GetColor('#731512'),0.9)
    stack.Add(histo_dict['ggFH_ak8jets_Pt'].GetPtr())
    histo_dict['VBFH_ak8jets_Pt'].SetFillColorAlpha(R.TColor.GetColor('#D05426'),0.9)
    stack.Add(histo_dict['VBFH_ak8jets_Pt'].GetPtr())
    histo_dict['DY_ak8jets_Pt'].SetFillColorAlpha(R.TColor.GetColor('#F4E85E'),0.9)
    stack.Add(histo_dict['DY_ak8jets_Pt'])
    histo_dict['TT_ak8jets_Pt'].SetFillColorAlpha(R.TColor.GetColor('#322E95'),0.9)
    stack.Add(histo_dict['TT_ak8jets_Pt'])

    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    stack.Draw('histo')
    stack.GetXaxis().SetTitle("AK8Jet Pt [GeV]")
    stack.GetYaxis().SetTitle("AK8Jet Yields")


    histo_dict['SMHH_ak8jets_Pt'].SetLineWidth(2)
    histo_dict['SMHH_ak8jets_Pt'].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict['SMHH_ak8jets_Pt'].Scale(0.01)
    histo_dict['SMHH_ak8jets_Pt'].Draw('histo same')

    leg = R.TLegend(0.60,0.60,0.90,0.90)
    leg.AddEntry(histo_dict['ggFH_ak8jets_Pt'].GetPtr(), "ggF H", "f")
    leg.AddEntry(histo_dict['VBFH_ak8jets_Pt'].GetPtr(), "VBF H", "f")
    leg.AddEntry(histo_dict['DY_ak8jets_Pt'], "DY", "f")
    leg.AddEntry(histo_dict['TT_ak8jets_Pt'], "TT", "f")
    leg.AddEntry(histo_dict['SMHH_ak8jets_Pt'].GetPtr(), "SM HH", "l")
    leg.Draw('same')
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'Plots/Pt{suffix}.png')
    c.SaveAs(f'Plots/Pt{suffix}.pdf')
    
model_dict = {}
if dimention == '2D':
    model_dict['ak8jets_SoftDropMass_vs_Pt'] = R.RDF.TH2DModel(" ", " ", 40, 0, 400, 80, 200, 1300)
    model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = R.RDF.TH2DModel(" ", " ", 80, 200, 1300, 50, 0, 1)
    model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = R.RDF.TH2DModel(" ", " ", 50, 0, 1, 40, 0, 400)
    
    histo_dict['SMHH_ak8jets_SoftDropMass_vs_Pt'] = \
        df_dict['SMHH'].Histo2D(model_dict['ak8jets_SoftDropMass_vs_Pt'], "ak8jets_SoftDropMass", "ak8jets_Pt")
    
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = \
        df_dict['SMHH'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Pt'], "ak8jets_Pt", "bParticleNetTauAK8JetTags_probHtt")
    
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = \
        df_dict['SMHH'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Mass'], "bParticleNetTauAK8JetTags_probHtt", "ak8jets_SoftDropMass")
    
    print("SM HH done.")

    for DY_proc in DY_list:
        histo_dict[f'{DY_proc}_ak8jets_SoftDropMass_vs_Pt'] = \
            df_dict[f'{DY_proc}'].Histo2D(model_dict['ak8jets_SoftDropMass_vs_Pt'], "ak8jets_SoftDropMass", "ak8jets_Pt")

        histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = \
            df_dict[f'{DY_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Pt'], "ak8jets_Pt", "bParticleNetTauAK8JetTags_probHtt")
        
        histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = \
            df_dict[f'{DY_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Mass'], "bParticleNetTauAK8JetTags_probHtt", "ak8jets_SoftDropMass")

    histo_dict['DY_ak8jets_SoftDropMass_vs_Pt'] = histo_dict['DY+Jets50To100_ak8jets_SoftDropMass_vs_Pt'].GetPtr()
    histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = histo_dict['DY+Jets50To100_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetPtr()
    histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = histo_dict['DY+Jets50To100_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetPtr()

    for DY_proc in DY_list[1:]:
        histo_dict['DY_ak8jets_SoftDropMass_vs_Pt'].Add(histo_dict[f'{DY_proc}_ak8jets_SoftDropMass_vs_Pt'].GetPtr())
        histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Add(histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetPtr())
        histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Add(histo_dict[f'{DY_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetPtr())
        
    print("DY+Jets done.")
    
    for SH_proc in SH_list:
        histo_dict[f'{SH_proc}_ak8jets_SoftDropMass_vs_Pt'] = \
            df_dict[f'{SH_proc}'].Histo2D(model_dict['ak8jets_SoftDropMass_vs_Pt'], "ak8jets_SoftDropMass", "ak8jets_Pt")

        histo_dict[f'{SH_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = \
            df_dict[f'{SH_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Pt'], "ak8jets_Pt", "bParticleNetTauAK8JetTags_probHtt")
        
        histo_dict[f'{SH_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = \
            df_dict[f'{SH_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Mass'], "bParticleNetTauAK8JetTags_probHtt", "ak8jets_SoftDropMass")
        
    print("Single Higgs done.")
    
    for TT_proc in TT_list:
        print(TT_proc)
        histo_dict[f'{TT_proc}_ak8jets_SoftDropMass_vs_Pt'] = \
            df_dict[f'{TT_proc}'].Histo2D(model_dict['ak8jets_SoftDropMass_vs_Pt'], "ak8jets_SoftDropMass", "ak8jets_Pt")

        histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = \
            df_dict[f'{TT_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Pt'], "ak8jets_Pt", "bParticleNetTauAK8JetTags_probHtt")
        
        histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = \
            df_dict[f'{TT_proc}'].Histo2D(model_dict['bParticleNetTauAK8JetTags_probHtt_vs_Mass'], "bParticleNetTauAK8JetTags_probHtt", "ak8jets_SoftDropMass")

        
    histo_dict['TT_ak8jets_SoftDropMass_vs_Pt'] = histo_dict['TTbarHad_ak8jets_SoftDropMass_vs_Pt'].GetPtr()
    histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = histo_dict['TTbarHad_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetPtr()
    histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = histo_dict['TTbarHad_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetPtr()

    for TT_proc in TT_list[1:]:
        print(TT_proc)
        histo_dict['TT_ak8jets_SoftDropMass_vs_Pt'].Add(histo_dict[f'{TT_proc}_ak8jets_SoftDropMass_vs_Pt'].GetPtr())
        histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Add(histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetPtr())
        histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Add(histo_dict[f'{TT_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetPtr())

    histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'] = histo_dict['DY_ak8jets_SoftDropMass_vs_Pt']
    histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'].Add(histo_dict['TT_ak8jets_SoftDropMass_vs_Pt'])
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'] = histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Pt']
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Add(histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Pt'])
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'] = histo_dict['DY_bParticleNetTauAK8JetTags_probHtt_vs_Mass']
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Add(histo_dict['TT_bParticleNetTauAK8JetTags_probHtt_vs_Mass'])
    
    for SH_proc in SH_list:
        histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'].Add(histo_dict[f'{SH_proc}_ak8jets_SoftDropMass_vs_Pt'].GetPtr())
        histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Add(histo_dict[f'{SH_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetPtr())
        histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Add(histo_dict[f'{SH_proc}_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetPtr())
        
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['SMHH_ak8jets_SoftDropMass_vs_Pt'].Draw('colz4')
    histo_dict['SMHH_ak8jets_SoftDropMass_vs_Pt'].GetXaxis().SetTitle("AK8Jet softdrop mass [GeV]")
    histo_dict['SMHH_ak8jets_SoftDropMass_vs_Pt'].GetYaxis().SetTitle("AK8Jet Pt [GeV]")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/SMHH_ak8jets_SoftDropMass_vs_Pt{suffix}.png')
    c.SaveAs(f'Plots/SMHH_ak8jets_SoftDropMass_vs_Pt{suffix}.pdf')
    
    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'].Draw('colz4')
    histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'].GetXaxis().SetTitle("AK8Jet softdrop mass [GeV]")
    histo_dict['Bkg_ak8jets_SoftDropMass_vs_Pt'].GetYaxis().SetTitle("AK8Jet Pt [GeV]")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/Bkg_ak8jets_SoftDropMass_vs_Pt{suffix}.png')
    c.SaveAs(f'Plots/Bkg_ak8jets_SoftDropMass_vs_Pt{suffix}.pdf')
    
    

    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Draw('colz4')
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetXaxis().SetTitle("AK8Jet Pt [GeV]")
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetYaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt{suffix}.png')
    c.SaveAs(f'Plots/SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Pt{suffix}.pdf')
    
    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].Draw('colz4')
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetXaxis().SetTitle("AK8Jet Pt [GeV]")
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt'].GetYaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt{suffix}.png')
    c.SaveAs(f'Plots/Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Pt{suffix}.pdf')
    
    

    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Draw('colz4')
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetXaxis().SetTitle("AK8Jet softdrop mass [GeV]")
    histo_dict['SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetYaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass{suffix}.png')
    c.SaveAs(f'Plots/SMHH_bParticleNetTauAK8JetTags_probHtt_vs_Mass{suffix}.pdf')
    
    
    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].Draw('colz4')
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetXaxis().SetTitle("AK8Jet softdrop mass [GeV]")
    histo_dict['Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass'].GetYaxis().SetTitle("ParticleNetTauAK8JetTags probHtt")
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy(0)
    c.SaveAs(f'Plots/Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass{suffix}.png')
    c.SaveAs(f'Plots/Bkg_bParticleNetTauAK8JetTags_probHtt_vs_Mass{suffix}.pdf')
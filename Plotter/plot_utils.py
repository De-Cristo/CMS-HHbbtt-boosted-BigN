import ROOT as R
import re
import argparse
from array import array
import os
R.EnableImplicitMT()

color_list = ['#731512', '#D05426', '#F4E85E', '#322E95']

# sample_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarSemi', 'TTbarDiLep']
sample_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarDiLep']

DY_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf']
SH_list = ['VBFH', 'ggFH']
# TT_list = ['TTbarHad', 'TTbarSemi', 'TTbarDiLep']
TT_list = ['TTbarHad', 'TTbarDiLep']


# sample_list = ['SMHH', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf','VBFH', 'ggFH','TTbarHad', 'TTbarSemi']

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

ak8_model_dict = {
                'ak8jets_SoftDropMass': R.RDF.TH1DModel(" ", " ", 40, 0, 400),
                'ak8jets_Mass': R.RDF.TH1DModel(" ", " ", 40, 0, 400),
                'bParticleNetTauAK8JetTags_probHtt': R.RDF.TH1DModel(" ", " ", 50, 0, 1),
                'ak8jets_probHttOverQCD': R.RDF.TH1DModel(" ", " ", 50, 0, 1),
                'ak8jets_probHtl': R.RDF.TH1DModel(" ", " ", 50, 0, 1),
                'ak8jets_probHttOverLepton': R.RDF.TH1DModel(" ", " ", 50, 0, 1),
                'ak8jets_probQCD0hf': R.RDF.TH1DModel(" ", " ", 50, 0, 1)
             }

ak8_quantity_dict = {
                'ak8jets_SoftDropMass': ["AK8Jet Soft Drop Mass [GeV]", "AK8Jet Yields", "SoftDropMass"],
                'ak8jets_Mass': ["AK8Jet PNet Corrected mass [GeV]", "AK8Jet Yields", "Mass"],
                'bParticleNetTauAK8JetTags_probHtt': ["ParticleNetTauAK8JetTags probHtt", "AK8Jet Yields", "probHtt"],
                'ak8jets_probHttOverQCD': ["ParticleNetTauAK8JetTags probHttOverQCD", "AK8Jet Yields", "probHttOverQCD"],
                'ak8jets_probHtl': ["ParticleNetTauAK8JetTags probHte+probHtm", "AK8Jet Yields", "probHtl"], 
                'ak8jets_probHttOverLepton': ["ParticleNetTauAK8JetTags probHttOverLepton", "AK8Jet Yields", "probHttOverLepton"],
                'ak8jets_probQCD0hf': ["ParticleNetTauAK8JetTags ak8jets_PNet_score", "AK8Jet Yields", "PNet_score"]
}

evt_model_dict = {
    'Hbb_9Xbb': R.RDF.TH1DModel(" ", " ", 25, 0, 10),
    'Htx_9Xtx': R.RDF.TH1DModel(" ", " ", 25, 0, 10),
    'Hbb_mass': R.RDF.TH1DModel(" ", " ", 40, 0, 550.),
    'Htx_mass': R.RDF.TH1DModel(" ", " ", 40, 0, 550.),
    'Hbb_pt': R.RDF.TH1DModel(" ", " ", 40, 0, 3000.),
    'Htx_pt': R.RDF.TH1DModel(" ", " ", 40, 0, 3000.),
    'Hbb_eta': R.RDF.TH1DModel(" ", " ", 40, -5, 5),
    'Htx_eta': R.RDF.TH1DModel(" ", " ", 40, -5, 5),
    'Hbb_phi': R.RDF.TH1DModel(" ", " ", 40, -4, 4),
    'Htx_phi': R.RDF.TH1DModel(" ", " ", 40, -4, 4),
}

evt_quantity_dict = {
    'Hbb_9Xbb': ["$9_{hbb}^{bb\ vs\ all}$", "Events", "Hbb_9Xbb", 0, 10.],
    'Htx_9Xtx': ["$9_{htx}^{tx\ vs\ all}$", "Events", "Htx_9Xtx", 0, 10.],
    'Hbb_mass': ["$M_{hbb}$", "Events", "Hbb_mass", 0, 550.],
    'Htx_mass': ["$M_{htx}$", "Events", "Htx_mass", 0, 550.],
    'Hbb_pt': ["$p_{T}^{hbb}$", "Events", "Hbb_pt", 0, 3000.],
    'Htx_pt': ["$p_{T}^{htx}$", "Events", "Htx_pt", 0, 3000.],
    'Hbb_eta': ["$\\eta^{hbb}$", "Events", "Hbb_eta", -5., 5.],
    'Htx_eta': ["$\\eta^{htx}$", "Events", "Htx_eta", -5., 5.],
    'Hbb_phi': ["$\\phi^{hbb}$", "Events", "Hbb_phi", -4., 4.],
    'Htx_phi': ["$\\phi^{htx}$", "Events", "Htx_phi", -4., 4.],    
}

evt_interested_variables = {'Hbb_9Xbb', 'Htx_9Xtx', 
                            'Hbb_mass', 'Htx_mass', 
                            'Hbb_pt', 'Htx_pt', 
                            'Hbb_eta', 'Htx_eta', 
                            'Hbb_phi', 'Htx_phi', 'Weight'}

process_order = ['SMHH', 'ggFH', 'VBFH', 'DY', 'TT']
quantity_lis = ['Hbb_9Xbb', 'Htx_9Xtx',
                'Hbb_mass', 'Htx_mass', 
                'Hbb_pt', 'Htx_pt', 
                'Hbb_eta', 'Htx_eta', 
                'Hbb_phi', 'Htx_phi']



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
    

def stacking_1D(histo_list, histo_dict, xmin, xlim, ylim, xtitle, ytitle, plotname, prefix, suffix):
    
    nhistos = len(histo_list)
    stack=R.THStack("stack"," ")
    for ihist in range(1, nhistos):
        histo_dict[histo_list[ihist]].SetFillColorAlpha(R.TColor.GetColor(color_list[ihist-1]),0.9)
        stack.Add(histo_dict[histo_list[ihist]])
        
    hpx = R.TH2F("hpx"," ",10, xmin, xlim, 10, 0.1, ylim)
    hpx.SetStats(R.kFALSE)

    c = R.TCanvas()
    R.gStyle.SetOptStat(0000)
    hpx.Draw()
    stack.Draw('histo same')
    hpx.GetXaxis().SetTitle(xtitle)
    hpx.GetYaxis().SetTitle(ytitle)

    histo_dict[histo_list[0]].SetLineWidth(2)
    histo_dict[histo_list[0]].SetLineColorAlpha(R.TColor.GetColor("#950008"),1.0)
    histo_dict[histo_list[0]].Scale(0.074)
    histo_dict[histo_list[0]].Draw('histo same')

    leg = R.TLegend(0.40,0.65,0.70,0.90)
    for key, items in histo_dict.items():
        if key in histo_list:
            if 'HH' in key: leg.AddEntry(histo_dict[key], 'SM HH', "l")
            elif 'ggF' in key: leg.AddEntry(histo_dict[key], 'ggF H', "f")
            elif 'VBF' in key: leg.AddEntry(histo_dict[key], 'VBF H', "f")
            elif 'DY' in key: leg.AddEntry(histo_dict[key], 'DY', "f")
            elif 'TT' in key: leg.AddEntry(histo_dict[key], 'TT', "f")
        else: continue
    leg.SetBorderSize(0)
    leg.SetFillColorAlpha(0,0.2)
    leg.Draw('same')
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    c.SetLogy()
    c.SaveAs(f'{prefix}{plotname}_{suffix}.png')
    c.SaveAs(f'{prefix}{plotname}_{suffix}.pdf')
    
    return 0
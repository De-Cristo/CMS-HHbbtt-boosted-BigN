import os,sys
import ROOT as R
import re
from array import array
import importlib
import more_itertools

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
    lowX=0.21
    lowY=0.70
    CMS  = R.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    CMS.SetTextFont(61)
    CMS.SetTextSize(0.08)
    CMS.SetBorderSize(   0 )
    CMS.SetFillStyle(    0 )
    CMS.SetTextAlign(   12 )
    CMS.SetTextColor(    1 )
    CMS.AddText("CMS")
    return CMS

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    Preliminary  = R.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    Preliminary.SetTextFont(52)
    Preliminary.SetTextSize(0.06)
    Preliminary.SetBorderSize(   0 )
    Preliminary.SetFillStyle(    0 )
    Preliminary.SetTextAlign(   12 )
    Preliminary.SetTextColor(    1 )
    Preliminary.AddText("Preliminary")
    return Preliminary

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


def histo_generator_comb(fileset, sample):
    batch_size = 1
    filelist_batches = list(more_itertools.chunked(fileset[sample], batch_size))
    print(sample + '>>>>>>>')
    filelist_args = []
    for i in range(len(filelist_batches)):
        filelist_args.append([filelist_batches[i],sample])
    result_list = []
    with tqdm(total=len(list(enumerate(filelist_batches)))) as pbar:
        for i, results in enumerate(Pool(round(args.MT*0.5)).imap_unordered(histo_generator, list(enumerate(filelist_args)))):
            result_list.append(results)
            pbar.update()
    
    for quantity, histo_ in result_list[0].items():
        histo_dict[sample+'_'+quantity] = histo_.Clone()
        
    for result in result_list[1:]:        
        for quantity, histo_ in result[1].items():
            histo_dict[sample+'_'+quantity].Add(histo_)
    return 0


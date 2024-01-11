import ROOT as R
import re
import argparse
from array import array
import os
from Plotter.plot_utils import \
color_list, sample_list, fileset, \
evt_model_dict, evt_quantity_dict, evt_interested_variables,\
DY_list, SH_list, TT_list, process_order, quantity_lis,\
stacking_1D

path = "/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/" + "MixBased_Out_20231221/"

# for process in process_list:
for process in sample_list:
    for file in os.listdir(path+process):
        if file.endswith(".root"):
            fileset[process].append(path+'/'+process+'/'+file)
            
print("root files are checked.")

df_evt_dict = {}
df_ak8_dict = {}
histo_evt_dict = {}
histo_ak8_dict = {}

jet_type = '_type3'
dimention = '1D'
prefix = "./Plots_2024Jan10/"
ylim = 1.1e6
event_cat_list = ['TT','TL','LT','LL','ALL']
event_cat = 'ALL'

event_channel_list = ['tt', 'tm', 'te']
event_channel = 'tm'

if not os.path.exists(prefix): os.mkdir(prefix)
else: print(f"The directory '{prefix}' already exists.")

for sample in sample_list:
    df_evt_dict[sample] = R.RDataFrame("Eventree", fileset[sample], evt_interested_variables)
    if event_cat == 'TT':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('Hbb_T_Htx_T==1').Filter('Hbb_Htx_distinct==1')
        ylim = 2.0e0
    elif event_cat == 'TL':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('Hbb_T_Htx_L==1').Filter('Hbb_Htx_distinct==1')
        ylim = 2.0e1
    elif event_cat == 'LT':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('Hbb_L_Htx_T==1').Filter('Hbb_Htx_distinct==1')
        ylim = 2.0e1
    elif event_cat == 'LL':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('Hbb_L_Htx_L==1').Filter('Hbb_Htx_distinct==1')
        ylim = 2.0e2
    elif event_cat == 'ALL':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('Hbb_Htx_distinct==1')
        ylim = 2.0e5
        
    if event_channel == 'tt':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('IsTauTau==1')
        # print(sample+': '+str(df_evt_dict[sample].Count().GetValue()))
        
    elif event_channel == 'tm':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('IsMuonTau==1')
    elif event_channel == 'te':
        df_evt_dict[sample] = df_evt_dict[sample].Filter('IsElectronTau==1')

def plot_1D():
    for quantity, model in evt_model_dict.items():
        print(quantity)
        
        SMHH = 'SMHH'
        histo_evt_dict[f'{SMHH}_{quantity}'] = df_evt_dict[SMHH].Histo1D(model, quantity, "Weight").GetPtr()
        print("SM HH done.")
        
        DY = 'DY'
        for DY_proc in DY_list:
            histo_evt_dict[f'{DY_proc}_{quantity}'] = df_evt_dict[f'{DY_proc}'].Histo1D(model, quantity, "Weight").GetPtr()
        histo_evt_dict[f'{DY}_{quantity}'] = histo_evt_dict[f'DY+Jets50To100_{quantity}']
        for DY_proc in DY_list[1:]:
            histo_evt_dict[f'{DY}_{quantity}'] = histo_evt_dict[f'{DY}_{quantity}'] + histo_evt_dict[f'{DY_proc}_{quantity}']
        print("DY+Jets done.")
        
        for SH_proc in SH_list:
            histo_evt_dict[f'{SH_proc}_{quantity}'] = df_evt_dict[f'{SH_proc}'].Histo1D(model, quantity, "Weight").GetPtr()
        print("Single Higgs done.")
        
        TT = 'TT'
        for TT_proc in TT_list:
            print(TT_proc)
            histo_evt_dict[f'{TT_proc}_{quantity}'] = df_evt_dict[f'{TT_proc}'].Histo1D(model, quantity, "Weight").GetPtr()
        histo_evt_dict[f'{TT}_{quantity}'] = histo_evt_dict[f'TTbarHad_{quantity}']
        for TT_proc in TT_list[1:]:
            histo_evt_dict[f'{TT}_{quantity}'] = histo_evt_dict[f'{TT}_{quantity}'] + histo_evt_dict[f'{TT_proc}_{quantity}']
        print("TTbar done.")
        
    print("Plotting...")
                
    for _quantity in quantity_lis:
        histo_list = [_process+'_'+_quantity for _process in process_order]

        plot_ind = stacking_1D(histo_list = histo_list, 
                               histo_dict = histo_evt_dict, 
                               xmin = evt_quantity_dict[_quantity][3],
                               xlim = evt_quantity_dict[_quantity][4], 
                               ylim = ylim,
                               xtitle = evt_quantity_dict[_quantity][0],
                               ytitle = evt_quantity_dict[_quantity][1],
                               plotname = evt_quantity_dict[_quantity][2],
                               prefix = prefix, 
                               suffix = event_cat+'_'+event_channel)
        
        
    return 0
    

if __name__ == '__main__':
    R.EnableImplicitMT()
    R.gROOT.SetBatch(True)

    if dimention == '1D': plot_1D()
    elif dimention == '2D': plot_2D()

exit(0)

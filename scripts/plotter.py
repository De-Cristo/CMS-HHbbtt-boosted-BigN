from configs.plot_config_bigNtuple import * # need modification if you want to change the config
R.gROOT.SetBatch(True)

parser = argparse.ArgumentParser(description="All the arguments to use the plotting tool.")
parser.add_argument('-m', '--MultiThread', dest='MT', type=int, default=1, help="The number of threads used in the process.")
parser.add_argument('-c', '--ConfigFile', dest='config', type=str, default=None, help="The configuration file to control the plotter.")
args = parser.parse_args()

def histo_generator(df_args): 
# build up the dataframe (read, define new variables, prune the branches)
    # print(df_args) (0, [['/gwdata/users/lzhang/private/bbtt_Ntuples/NonResonantHHbbtautauNtuples_hadd/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8.root'], 'SMHH'])
    df_ = R.RDataFrame(treeName, df_args[1][0], interested_variables) # converted root into RDF
    df_ = define_variables(df_, new_defined_variables)
    df_ = apply_filters(df_, filters)
    histo_ = {}
    for quantity in interest_quantities:
        my_list_ = list(interest_quantities[quantity][0])
        my_list_[0] = df_args[1][1]+'_'+quantity
        my_list_[1] = df_args[1][1]+'_'+quantity
        interest_quantities[quantity][0] = tuple(my_list_)
        histo_[quantity] = df_.Histo1D(interest_quantities[quantity][0], quantity, weight).GetPtr()
    return histo_

def plot_generator(plot_arg):
    quantity = plot_arg[0]
    setup = plot_arg[1]
    
    adapt = R.gROOT.GetColor(12)
    new_idx = R.gROOT.GetListOfColors().GetSize() + 1
    trans = R.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
    
    stack=R.THStack("stack","stack")
    for sample,color in stack_dict.items():
        histo_dict[sample+'_'+quantity].SetFillColorAlpha(R.TColor.GetColor(color),0.9)
        stack.Add(histo_dict[sample+'_'+quantity])
        
    histo_dict['SMHH'+'_'+quantity].Scale(0.05) # develop after play with signal   
    histo_dict['SMHH'+'_'+quantity].SetLineColor(2)
    histo_dict['SMHH'+'_'+quantity].SetLineWidth(3)
    
    histo_dict['fake_data'+'_'+quantity].GetXaxis().SetTitle(setup[2]) # develop after play with data   
    histo_dict['fake_data'+'_'+quantity].GetXaxis().SetTitleSize(0)
    # histo_dict['fake_data'+'_'+quantity].GetXaxis().SetNdivisions(505)
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetLabelFont(42)
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetLabelOffset(0.01)
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetLabelSize(0.06)
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetTitleSize(0.075)
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetTitleOffset(1.04)
    histo_dict['fake_data'+'_'+quantity].SetTitle("")
    histo_dict['fake_data'+'_'+quantity].GetYaxis().SetTitle(setup[1])
    histo_dict['fake_data'+'_'+quantity].SetMinimum(0.1)
    histo_dict['fake_data'+'_'+quantity].SetMarkerStyle(20)
    histo_dict['fake_data'+'_'+quantity].SetMarkerSize(1)
    histo_dict['fake_data'+'_'+quantity].SetLineColor(1)
    histo_dict['fake_data'+'_'+quantity].SetLineWidth(2)
    
    #blind
    # for k in range(1,histo_dict['fake_data'+'_'+quantity].GetSize()):
    #     histo_dict['fake_data'+'_'+quantity].SetBinContent(k,0.0)
        
    errorBand = histo_dict['DY+Jets'+'_'+quantity].Clone()
    errorBand.Add(histo_dict['TTbar'+'_'+quantity])
    errorBand.Add(histo_dict['ggFH'+'_'+quantity])
    errorBand.Add(histo_dict['VBFH'+'_'+quantity])
    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(new_idx)
    errorBand.SetFillStyle(3001)
    errorBand.SetLineWidth(1)
    
    c = R.TCanvas("canvas","",0,0,800,800)
    R.gStyle.SetOptStat(0)

    c.cd()
    pad1 = R.TPad("pad1","pad1",0,0.35,1,1)
    pad1.Draw()
    pad1.cd()
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(10)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.SetLeftMargin(0.18)
    pad1.SetRightMargin(0.05)
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameLineStyle(0)
    pad1.SetFrameBorderMode(0)
    pad1.SetFrameBorderSize(10)
    
    histo_dict['fake_data'+'_'+quantity].GetXaxis().SetLabelSize(0)
    # print(max(histo_dict['fake_data'+'_'+quantity].GetMaximum()*1.5,errorBand.GetMaximum()*1.5))
    # histo_dict['fake_data'+'_'+quantity].\
    #     SetMaximum(max(histo_dict['fake_data'+'_'+quantity].GetMaximum()*1.5,errorBand.GetMaximum()*1.5)) # For BigN its good
    # histo_dict['fake_data'+'_'+quantity].SetMaximum(100)
    # histo_dict['fake_data'+'_'+quantity].SetMinimum(0)
    histo_dict['fake_data'+'_'+quantity].Draw("e")
    stack.Draw("histsame")
    errorBand.Draw("e2same")
    histo_dict['fake_data'+'_'+quantity].Draw("esame")
    histo_dict['SMHH'+'_'+quantity].Draw("histsame")
    
    legende = make_legend()
    legende.AddEntry(histo_dict['fake_data'+'_'+quantity],"Observed","elp")
    legende.AddEntry(histo_dict['DY+Jets'+'_'+quantity],"Z#rightarrow ll","f")
    legende.AddEntry(histo_dict['TTbar'+'_'+quantity],"t#bar{t}","f")
    legende.AddEntry(histo_dict['ggFH'+'_'+quantity],"ggF,single-H","f")
    legende.AddEntry(histo_dict['VBFH'+'_'+quantity],"VBF,single-H","f")
    legende.AddEntry(histo_dict['SMHH'+'_'+quantity],"Signal","l")
    legende.AddEntry(errorBand,"Uncertainty","f")
    legende.Draw()
    
    l1=add_lumi('2018')
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    
    pad1.RedrawAxis()
    
    c.cd()
    pad2 = R.TPad("pad2","pad2",0,0,1,0.35);
    pad2.SetTopMargin(0.05);
    pad2.SetBottomMargin(0.35);
    pad2.SetLeftMargin(0.18);
    pad2.SetRightMargin(0.05);
    pad2.SetTickx(1)
    pad2.SetTicky(1)
    pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    
    h1=histo_dict['fake_data'+'_'+quantity].Clone()
    h1.SetMaximum(2.0) #FIXME(1.5)
    h1.SetMinimum(0.0) #FIXME(0.5)
    h1.SetMarkerStyle(20)
    h3=errorBand.Clone()
    hwoE=errorBand.Clone()
    for iii in range (1,hwoE.GetSize()-1):
        hwoE.SetBinError(iii,0)
    h3.Sumw2()
    h1.Sumw2()
    h1.SetStats(0)
    h1.Divide(hwoE)
    h3.Divide(hwoE)
    h1.GetXaxis().SetTitle(quantity)
    h1.GetXaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetTitle("Obs./Exp.")
    # h1.GetXaxis().SetNdivisions(505)
    h1.GetYaxis().SetNdivisions(5)

    h1.GetXaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleOffset(0.56)
    h1.GetXaxis().SetTitleOffset(1.04)
    h1.GetXaxis().SetLabelSize(0.11)
    h1.GetYaxis().SetLabelSize(0.11)
    h1.GetXaxis().SetTitleFont(42)
    h1.GetYaxis().SetTitleFont(42)
    h1.Draw("e0p")
    h3.Draw("e2same")
    
    c.cd()
    pad1.Draw()
    R.gPad.RedrawAxis()
    
    c.Modified()
    c.SaveAs(outputDir+"/"+'_'+quantity+".pdf")
    c.SaveAs(outputDir+"/"+'_'+quantity+".png")
    
    pad1.SetLogy(1)
    c.Modified()
    c.SaveAs(outputDir+"/"+'_'+quantity+"_Logy.pdf")
    c.SaveAs(outputDir+"/"+'_'+quantity+"_Logy.png")
    return 0


if __name__ == '__main__':
    
    # read config file: ## This is still an interesting way to import the config file although I don't use it...
    # confName = args.config.split('/')[-1].split('.')[-2]
    # print("Reading from " + confName)
    # __import__(confName) 
    # exec('from ' + confName + ' import *')

    R.EnableImplicitMT(args.MT) # Enable multi-thread running
    # fileset = build_default_fileset(input_Dir, args.regen, jsonFile) # automatically generate a json file include the root files
    # only read the json file existing. can be thought twice later.
    with open(jsonFile+'withWeight.json', 'r') as f:
        data = f.read()
        fileset = json.loads(data)
        
    print("Generating Histograms from root files through RDF ...")
    for sample in sample_list:
        histo_generator_comb(fileset, sample)

    # for quantity in interest_quantities: # remove when we use data
    #     histo_dict['fake_data'+'_'+quantity] = histo_dict['TTbar'+"_"+quantity] + histo_dict['DY+Jets'+"_"+quantity] + histo_dict['VBFH'+"_"+quantity] + histo_dict['ggFH'+"_"+quantity]
    print("Generating Histograms from root files throught RDF ... DONE.")

    hist_file = R.TFile("hist_all_0328.root","RECREATE")
    for name, hist in histo_dict.items():
        hist.Write()
    hist_file.Close()

    if os.path.isdir(outputDir):
        os.system('rm -rfv ' + outputDir)
        os.system('mkdir -p ' + outputDir)
    else:
        os.system('mkdir -p ' + outputDir)

    # develop something to open histo from root file
    hist_file = R.TFile("hist_all.root","READ")

    print(">>>>>>>> Plotting >>>>>>>>")
    with Pool(args.MT) as p:
        p.map(plot_generator, list(interest_quantities.items()))
    print(">>>>>>>> Done >>>>>>>>")

    os.system('cp -r ./php-plots/plot-viewer ./php-plots/index.php '+outputDir)
          
    exit(0)

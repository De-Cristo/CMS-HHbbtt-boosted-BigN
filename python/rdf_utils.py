import ROOT as R
from tqdm import tqdm
from multiprocessing import Pool,Process
import more_itertools
from configs.plot_config_bigNtuple import interested_variables, treeName, new_defined_variables, filters

def genInfoGether(fileset, process, MT):
    # format like this : fileset['Process'] = [[path2files],XS,lumi,sumOfweights] with sumofweights uncalculated
    batch_size = 1
    filelist_batches = list(more_itertools.chunked(fileset[process][0], batch_size))
    print(process + '>>>>>>> calculating sum of weights')
    filelist_args = []
    for i in range(len(filelist_batches)):
        filelist_args.append(filelist_batches[i][0])
    sumOfweights = 0.
    with tqdm(total=len(filelist_batches)) as pbar:
        for results in Pool(MT).imap_unordered(sumOfweights_calc, filelist_args):
            sumOfweights+=results
            pbar.update()
    return sumOfweights

def sumOfweights_calc(root_file):
    fin = R.TFile(root_file, "READ")
    weightHist = fin.Get('gentree/weight_distribution')
    return weightHist.GetBinContent(1)


def apply_filters(df_, filters):
    if len(filters) == 0:
        return df_
    else:
        for filter_ in filters:
            df_ = df_.Filter(filter_)
        return df_
    
def define_variables(df_, new_defined_variables):
    if len(new_defined_variables) == 0:
        return df_
    else:
        for _var,_def in new_defined_variables.items(): # update variables
            df_ = df_.Define(_var, _def)
        return df_
    
def snap_shots(arguments):
    # arguments = [infilename,outdir,process,XS,lumi,sumOfweights]
    inFileName = arguments[0]
    outFileName = '/'.join([arguments[1], arguments[2], inFileName.split('/')[-1]])
    XS = str(arguments[3])
    lumi = str(arguments[4])
    sumOfweights = str(arguments[5])
    df_ = R.RDataFrame(treeName, inFileName, interested_variables) # converted root into RDF
    df_ = define_variables(df_, new_defined_variables)
    df_ = df_.Define("true_weight","aMCatNLOweight*{0}*{1}/{2}".format(XS, lumi, sumOfweights))
    df_ = apply_filters(df_, filters)
    outBranchList = list(interested_variables)
    outBranchList.append('true_weight')
    for key in new_defined_variables:
        outBranchList.append(key)
    df_.Snapshot('slimmedtree', outFileName, outBranchList)
    return 0

def Fast_SnapShots(fileset, process, MT, outDir):
    # format like this : fileset['Process'] = [[path2files],XS,lumi,sumOfweights] with sumofweights calculated
    batch_size = 1
    filelist_batches = list(more_itertools.chunked(fileset[process][0], batch_size))
    print(process + '>>>>>>> slimming files, this will take a while, please be patient')
    
    filelist_args = []
    for i in range(len(filelist_batches)):
        filelist_args.append((filelist_batches[i][0],outDir,process,fileset[process][1],fileset[process][2],fileset[process][3]))
        
    with tqdm(total=len(filelist_batches)) as pbar:
        for results in Pool(MT).imap_unordered(snap_shots, filelist_args):
            pbar.update()
            
    return None
    
    
import glob
import json
from multiprocessing import Pool,Process
from tqdm import tqdm
import argparse
import os,sys

def get_all_file_paths(all_full_path_list, base_path):
    all_file_list = os.listdir(base_path)
    all_file_dir_list = []
    for file in all_file_list:
        file_path = os.path.join(base_path, file)
        if os.path.isdir(file_path):
            get_all_file_paths(all_full_path_list, file_path)
        elif os.path.isfile(file_path) and '.root' in file and file_path.replace(file, '') not in all_full_path_list:
            all_full_path_list.append(file_path.replace(file, ''))        
    return all_full_path_list

def build_default_fileset(base_path, regen, jsonName):
    filename = jsonName
    if os.path.exists(filename) and regen!=True:
        # print(f'{filename} existing, will use this file. Please update it with -re True')
        with open(filename, "r") as f:
            fileset = json.load(f)
            return fileset
    else:
        all_full_path_list = []
        get_all_file_paths(all_full_path_list, base_path)
        all_full_file_list = []

        for _path in all_full_path_list:
            _file_list = glob.glob(f'{_path}/*.root')
            for _file in _file_list:
                all_full_file_list.append(_file)

        fileset = {}
        # fileset['Process'] = [[path2files],XS,lumi,sumOfweights]
        from configs.plot_config_bigNtuple import lumi
        sumOfweights = 1 # calculated in each process
        # XS in picobarn
        fileset['TTbarHad'] = [[], 377.96, lumi, sumOfweights]
        fileset['TTbarSemi'] = [[], 365.34, lumi, sumOfweights]
        fileset['TTbarDiLep'] = [[], 88.29, lumi, sumOfweights]
        fileset['TTbarInc'] = [[], 88.29+365.34+377.96, lumi, sumOfweights]
        fileset['DY+Jets50To100'] = [[], 399, lumi, sumOfweights]
        fileset['DY+Jets100To250'] = [[], 94, lumi, sumOfweights]
        fileset['DY+Jets250To400'] = [[], 3.85, lumi, sumOfweights]
        fileset['DY+Jets400To650'] = [[], 0.506, lumi, sumOfweights]
        fileset['DY+Jets650ToInf'] = [[], 0.0473, lumi, sumOfweights]
        fileset['DY+JetspTBinned'] = [[], 399+94+3.85+0.506+0.0473, lumi, sumOfweights]
        fileset['DY+0J'] = [[], 5129, lumi, sumOfweights]
        fileset['DY+1J'] = [[], 953, lumi, sumOfweights]
        fileset['DY+2J'] = [[], 363, lumi, sumOfweights]
        fileset['DY+JetsBinned'] = [[], 5129+953+363, lumi, sumOfweights]
        fileset['SMHH'] = [[], 0.00134, lumi, sumOfweights]
        
        # XS from HXSWG
        bbttBr = 0.073
        fileset['VBFH'] = [[], 0.237, lumi, sumOfweights]
        fileset['ggFH'] = [[], 3.047, lumi, sumOfweights]
        
        # question: are these in femtobarn or picobarn???
        fileset['HHkl0'] = [[], 70.38 * bbttBr, lumi, sumOfweights]
        fileset['HHkl1'] = [[], 31.03 * bbttBr, lumi, sumOfweights] # not consistent with SMHH
        fileset['HHkl2p45'] = [[], 13.26 * bbttBr, lumi, sumOfweights]
        fileset['HHkl5p0'] = [[], 94.81 * bbttBr, lumi, sumOfweights]

        for _file in all_full_file_list:
            if 'TTTo2L2Nu' in _file:
                fileset['TTbarDiLep'][0].append(_file)
                fileset['TTbarInc'][0].append(_file)
            elif 'TTToHadronic' in _file:
                fileset['TTbarHad'][0].append(_file)
                fileset['TTbarInc'][0].append(_file)
            elif 'TTToSemiLeptonic' in _file:
                fileset['TTbarSemi'][0].append(_file)
                fileset['TTbarInc'][0].append(_file)
            elif 'DYJetsToLL_LHEFilterPtZ-50To100' in _file:
                fileset['DY+Jets50To100'][0].append(_file)
                fileset['DY+JetspTBinned'][0].append(_file)
            elif 'DYJetsToLL_LHEFilterPtZ-100To250' in _file:
                fileset['DY+Jets100To250'][0].append(_file)
                fileset['DY+JetspTBinned'][0].append(_file)
            elif 'DYJetsToLL_LHEFilterPtZ-250To400' in _file:
                fileset['DY+Jets250To400'][0].append(_file)
                fileset['DY+JetspTBinned'][0].append(_file)
            elif 'DYJetsToLL_LHEFilterPtZ-400To650' in _file:
                fileset['DY+Jets400To650'][0].append(_file)
                fileset['DY+JetspTBinned'][0].append(_file)
            elif 'DYJetsToLL_LHEFilterPtZ-650ToInf' in _file:
                fileset['DY+Jets650ToInf'][0].append(_file)
                fileset['DY+JetspTBinned'][0].append(_file)
            elif 'DYJetsToLL_' in _file and '0J' in _file:
                fileset['DY+0J'][0].append(_file)
                fileset['DY+JetsBinned'][0].append(_file)
            elif 'DYJetsToLL_' in _file and '1J' in _file:
                fileset['DY+1J'][0].append(_file)
                fileset['DY+JetsBinned'][0].append(_file)
            elif 'DYJetsToLL_' in _file and '2J' in _file:
                fileset['DY+2J'][0].append(_file)
                fileset['DY+JetsBinned'][0].append(_file)
            elif 'GluGluToHHTo2B2Tau' in _file and 'SM' in _file:
                fileset['SMHH'][0].append(_file)
            elif 'GluGluToHHTo2B2Tau' in _file and 'cHHH0' in _file:
                fileset['HHkl0'][0].append(_file)
            elif 'GluGluToHHTo2B2Tau' in _file and 'cHHH1' in _file:
                fileset['HHkl1'][0].append(_file)
            elif 'GluGluToHHTo2B2Tau' in _file and 'cHHH2p45' in _file:
                fileset['HHkl2p45'][0].append(_file)
            elif 'GluGluToHHTo2B2Tau' in _file and 'cHHH5p0' in _file:
                fileset['HHkl5p0'][0].append(_file)
            elif 'VBFH' in _file:
                fileset['VBFH'][0].append(_file)
            elif 'GluGluH' in _file:
                fileset['ggFH'][0].append(_file)
            #elif BSM
            #elif Data
            else:
                print(f'{_file} is not recoganized by any process, please check again.')

        with open(jsonName,"w") as f:
            json.dump(fileset,f)
            print(f'{filename} generated, will be used in this process.')
            return fileset
        
    return None
    

    
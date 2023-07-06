from read_inputs import build_default_fileset, argparse, json, os, sys
from rdf_utils import apply_filters, define_variables, R, genInfoGether, Fast_SnapShots
from plot_config_bigNtuple import * # need modification if you want to change the config
R.gROOT.SetBatch(True)
from shutil import rmtree

parser = argparse.ArgumentParser(description="All the arguments to use the plotting tool.")
parser.add_argument('-m', '--MultiThread', dest='MT', type=int, default=1, help="The number of threads used in the process.")
parser.add_argument('-re', '--reGenJson', dest='regen', type=bool, default=False, help="True if json file is need to be regenerated.")
parser.add_argument('-o', '--outputDir', dest='outputDir', type=str, default='./slimmed_ntuples/', help="The output directory for new root files.")
parser.add_argument('-his', '--Histo', dest='his', type=bool, default=False, help="True if histograms are already generated and no need to be regenerated.")
parser.add_argument('-s', '--Stage', dest='stage', type=int, default=1, help="1: Generate json contains the input root files")
args = parser.parse_args()


if __name__ == '__main__':
    R.EnableImplicitMT(args.MT) # Enable multi-thread running
    if args.stage == 1 or args.stage == 123: # automatically generate a json file include the root files and genweights info
        fileset = build_default_fileset(input_Dir, args.regen, jsonFile+'.json')
        # format like this : fileset['Process'] = [[path2files],XS,lumi,sumOfweights] with sumOfweights uncalculated
        for process in process_list:
            fileset[process][3] = genInfoGether(fileset, process, args.MT)
        # format like this : fileset['Process'] = [[path2files],XS,lumi,sumOfweights] with sumOfweights calculated
        with open(jsonFile+'withWeight.json',"w") as f:
            json.dump(fileset,f)
        
    if args.stage == 2 or args.stage == 123: # save slimmed trees into new root files
        with open(jsonFile+'withWeight.json', 'r') as f:
            data = f.read()
        fileset = json.loads(data)
        if not os.path.exists(args.outputDir):
            os.makedirs(args.outputDir)
            
        for process in process_list:
            if os.path.exists('/'.join([args.outputDir, process])):
                print('output directory exists(over writing) : ', '/'.join([args.outputDir, process]))
                rmtree('/'.join([args.outputDir, process]))
                # os.rmdir('/'.join([args.outputDir, process]))
                os.makedirs('/'.join([args.outputDir, process]))
            else:
                os.makedirs('/'.join([args.outputDir, process]))
                print('generating output directory : ', '/'.join([args.outputDir, process]))
                
            Fast_SnapShots(fileset, process, args.MT, args.outputDir)
    
    sys.exit(0)
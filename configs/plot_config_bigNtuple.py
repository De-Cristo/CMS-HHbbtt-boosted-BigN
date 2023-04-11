df_dict = {}
histo_dict = {}

input_Dir = '/gwteras/cms/store/user/lichengz/NonResonantHHbbtt/MC_2018_09Apr2023_PUB/'
outputDir = './BigNtuple_plots0410/'
jsonFile = './AutoMake_Run2_2018_MC_BigNtuple'
lumi = 59700 # in pb

# the processes that samples belong to
# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep', 'TTbarInc', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+JetspTBinned', 'DY+JetsBinned']
# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+0J', 'DY+1J', 'DY+2J']
process_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+0J', 'DY+1J', 'DY+2J','TTbarSemi', 'TTbarDiLep']

# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbar', 'DY+JetspTBinned']
# process_list = ['SMHH']

stack_dict = { # sample name and color codes(in hexadecimal)
    'VBFH': "#D05426",
    'ggFH': "#731512",
    'DY+JetspTBinned': "#F4E85E",
    'TTbar': "#322E95",
}

# Include necessary header
import os, sys
import ROOT as R
bigNtuple_header_path = "./interface/proc_big_Ntuple.h"
R.gInterpreter.Declare('#include "{}"'.format(bigNtuple_header_path))

# the variables that we are interested in from the large root files
interested_variables = {
    "lheVPt", "aMCatNLOweight","MC_weight",
    "genpart_pdg",
    "genpart_TauMothInd","ak8jets_px","ak8jets_py","ak8jets_pz","ak8jets_e","ak8jets_SoftDropMass",
    "bParticleNetTauAK8JetTags_probHtt","bParticleNetTauAK8JetTags_probHtm","bParticleNetTauAK8JetTags_probHte",
    "bParticleNetTauAK8JetTags_probHbb","bParticleNetTauAK8JetTags_probHcc","bParticleNetTauAK8JetTags_probHqq",
    "bParticleNetTauAK8JetTags_probHgg","bParticleNetTauAK8JetTags_probQCD2hf","bParticleNetTauAK8JetTags_probQCD1hf","bParticleNetTauAK8JetTags_probQCD0hf",
}

# the name and the definition of the new variables that can be calculated from basic vars.

new_defined_variables = {
    "ak8jets_pT" : "calc_ak8jets_pT(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e)",
    "leading_ak8jets_pT" : "calc_leading_ak8jet_pT(ak8jets_pT)",
    "HttOverAll" : "bParticleNetTauAK8JetTags_probHtt/(bParticleNetTauAK8JetTags_probHtt+bParticleNetTauAK8JetTags_probHtm+bParticleNetTauAK8JetTags_probHte+bParticleNetTauAK8JetTags_probHbb+bParticleNetTauAK8JetTags_probHcc+bParticleNetTauAK8JetTags_probHqq+bParticleNetTauAK8JetTags_probHgg+bParticleNetTauAK8JetTags_probQCD2hf+bParticleNetTauAK8JetTags_probQCD1hf+bParticleNetTauAK8JetTags_probQCD0hf)",
}

# the name of the tree.
treeName = "HTauTauTree/HTauTauTree"
gentreeName = "gentree"
weight = "1"

filters = ["cut_leading_ak8jets_pT(leading_ak8jets_pT)"]

# the quantities that we wanted to plot.
interest_quantities = { # variable name and binning
    
    # "NAME" : [(" ", "NAME", NBINS, LOWER EDGE, UPPER EDGE), "YLABEL", "XLABEL",],
    "ak8jets_pT" : [(" ", "ak8jets_pT", 50, 0, 3000), "ak8 jets yields", "ak8jets_pT"],
    "leading_ak8jets_pT" : [(" ", "leading_ak8jets_pT", 50, 0, 3000), "Event yields", "leading_ak8jets_pT"],
    "bParticleNetTauAK8JetTags_probHtt" : [(" ", "bParticleNetTauAK8JetTags_probHtt", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHtt"],
    "bParticleNetTauAK8JetTags_probHtm" : [(" ", "bParticleNetTauAK8JetTags_probHtm", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHtm"],
    "bParticleNetTauAK8JetTags_probHte" : [(" ", "bParticleNetTauAK8JetTags_probHte", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHte"],
    "bParticleNetTauAK8JetTags_probHbb" : [(" ", "bParticleNetTauAK8JetTags_probHbb", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHbb"],
    "bParticleNetTauAK8JetTags_probHcc" : [(" ", "bParticleNetTauAK8JetTags_probHcc", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHcc"],
    "bParticleNetTauAK8JetTags_probHqq" : [(" ", "bParticleNetTauAK8JetTags_probHqq", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHqq"],
    "bParticleNetTauAK8JetTags_probHgg" : [(" ", "bParticleNetTauAK8JetTags_probHgg", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probHgg"],
    "bParticleNetTauAK8JetTags_probQCD2hf" : [(" ", "bParticleNetTauAK8JetTags_probQCD2hf", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probQCD2hf"],
    "bParticleNetTauAK8JetTags_probQCD1hf" : [(" ", "bParticleNetTauAK8JetTags_probQCD1hf", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probQCD1hf"],
    "bParticleNetTauAK8JetTags_probQCD0hf" : [(" ", "bParticleNetTauAK8JetTags_probQCD0hf", 50, 0, 1), "ak8 jets yields", "ak8_PNet_probQCD0hf"],
    "ak8jets_SoftDropMass"              : [(" ", "ak8jets_SoftDropMass", 50, 0, 2000), "ak8 jets yields", "ak8_PNet_probHtt"],
    "HttOverAll"                        : [(" ", "HttOverAll", 50, 0, 1), "ak8 jets yields", "HttOverAll"],
    "lheVPt"                            : [(" ", "lheVPt", 50, 0, 2000), "Events yields", "lheVPt"],
}

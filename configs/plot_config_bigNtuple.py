df_dict = {}
histo_dict = {}

Location = '/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/'
input_Dir = '/gwteras/cms/store/user/lichengz/NonResonantHHbbtt/MC_2018_09Apr2023_PUB/'
# input_Dir = '/gwteras/cms/store/user/lichengz/NonResonantHHbbtt_anomolySig/MC_2018_09Apr2023_PRI/'
outputDir = Location+'/slimmed_ntuple_test/'
jsonFile = Location+'./AutoMake_Run2_2018_MC_BigNtuple'
# jsonFile = Location+'./AutoMake_Run2_2018_MC_BigNtuple_anomolySig'

lumi = 59700 # in pb

# the processes that samples belong to
# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep', 'TTbarInc', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+JetspTBinned', 'DY+JetsBinned']
# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbarHad', 'TTbarSemi', 'TTbarDiLep', 'DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+0J', 'DY+1J', 'DY+2J']
# process_list = ['DY+Jets50To100', 'DY+Jets100To250', 'DY+Jets250To400', 'DY+Jets400To650', 'DY+Jets650ToInf', 'DY+0J', 'DY+1J', 'DY+2J','TTbarSemi', 'TTbarDiLep']

# process_list = ['SMHH', 'VBFH', 'ggFH', 'TTbar', 'DY+JetspTBinned']
process_list = ['SMHH']
# process_list = ['SMHH','HHkl0', 'HHkl1', 'HHkl2p45', 'HHkl5p0']

stack_dict = { # sample name and color codes(in hexadecimal)
    'VBFH': "#D05426",
    'ggFH': "#731512",
    'DY+JetspTBinned': "#F4E85E",
    'TTbar': "#322E95",
}

overlay_dict = { # sample name and color codes(in hexadecimal)
    'SMHH' : "#950008",
    'HHkl0': "#D05426",
    'HHkl1': "#731512",
    'HHkl2p45': "#F4E85E",
    'HHkl5p0': "#322E95",
}

# Include necessary header
import os, sys
import ROOT as R

# R.gInterpreter.AddIncludePath('/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/interface/')
# bigNtuple_header_path = "proc_big_Ntuple.h"
# R.gInterpreter.Declare('#include "{}"'.format(bigNtuple_header_path))

bigNtuple_header_path = "./interface/proc_big_Ntuple.h"
R.gInterpreter.Declare('#include "{}"'.format(bigNtuple_header_path))

# ak8_interest_variables = ['ak8jets_SoftDropMass', 
#                       'bParticleNetTauAK8JetTags_probHtt','bParticleNetTauAK8JetTags_probHtm','bParticleNetTauAK8JetTags_probHte',
#                       'bParticleNetTauAK8JetTags_probHbb','bParticleNetTauAK8JetTags_probHcc', 'bParticleNetTauAK8JetTags_probHqq','bParticleNetTauAK8JetTags_probHgg',
#                       'bParticleNetTauAK8JetTags_probQCD0hf','bParticleNetTauAK8JetTags_probQCD1hf','bParticleNetTauAK8JetTags_probQCD2hf',
#                       'bParticleNetTauAK8JetTags_masscorr',
#                      ]

ak8_interest_variables = ['ak8jets_SoftDropMass', 'bParticleNetTauAK8JetTags_masscorr'
                     ]

lepton_interest_variables = ['dxy', 'dz']

event_interest_variables = ['triggerbit']

helper_variables = ['ak8jets_px','ak8jets_py','ak8jets_pz','ak8jets_e','ak8jets_SoftDropMass','bParticleNetTauAK8JetTags_masscorr',
                    'genpart_px', 'genpart_py', 'genpart_pz', 'genpart_e', 'genpart_pdg', 'genpart_flags', 'genpart_TauGenDecayMode',
                    'genjet_px', 'genjet_py', 'genjet_pz', 'genjet_e', 'genjet_partonFlavour', 'genjet_hadronFlavour',
                    'genpart_HMothInd', 'genpart_ZMothInd', 'genpart_TauMothInd', 'genpart_WMothInd', 'genpart_bMothInd',
                    'daughters_byDeepTau2017v2p1VSjetraw',
                    
                    'PDGIdDaughters', 'daughters_isTauMatched', 'daughters_px', 'daughters_py', 'daughters_pz', 'daughters_e',
                    'daughters_muonID', 'daughters_typeOfMuon', 'daughters_iseleWP80', 'daughters_iseleWP90', 'dxy', 'dz',
                    'daughters_iseleWPLoose', 'daughters_iseleNoIsoWP90',
                    
                    'aMCatNLOweight', 'triggerbit', 
                    
                    'bParticleNetTauAK8JetTags_probHtt','bParticleNetTauAK8JetTags_probHtm','bParticleNetTauAK8JetTags_probHte',
                    'bParticleNetTauAK8JetTags_probHbb','bParticleNetTauAK8JetTags_probHcc', 'bParticleNetTauAK8JetTags_probHqq','bParticleNetTauAK8JetTags_probHgg',
                    'bParticleNetTauAK8JetTags_probQCD0hf','bParticleNetTauAK8JetTags_probQCD1hf','bParticleNetTauAK8JetTags_probQCD2hf',                     
                  ]

'''
    GenInfoVector  --> [h_status, tau_status, b_status,
                  HbbE, HbbPt, HbbEta, HbbPhi, HbbM,
                  HtautauE, HtautauPt, HtautauEta, HtautauPhi, HtautauM,
                  Hb1E, Hb1Pt, Hb1Eta, Hb1Phi,
                  Hb2E, Hb2Pt, Hb2Eta, Hb2Phi,
                  Htau1E, Htau1Pt, Htau1Eta, Htau1Phi,
                  Htau2E, Htau2Pt, Htau2Eta, Htau2Phi,
                  HHE, HHPt, HHEta, HHPhi, HHM
                  ]
'''

# the name of the tree.
treeName = "HTauTauTree/HTauTauTree"
gentreeName = "gentree"
weight = "1"

filters = ["cut_leading_ak8jets_pT(leading_ak8jets_pT)"]

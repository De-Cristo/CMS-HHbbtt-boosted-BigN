import ROOT as R
R.gInterpreter.AddIncludePath('/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/include/')
R.gInterpreter.Declare('#include "proc_big_Ntuple.hh"')
R.gSystem.Load('/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/lib/proc_big_Ntuple.so')
big_ntuple = R.Big_Ntuple()

print(big_ntuple.cut_leading_ak8jets_pT(300.))

df = R.RDataFrame('HTauTauTree/HTauTauTree','/gwteras/cms/store/user/lichengz/NonResonantHHbbtt/MC_2018_09Apr2023_PUB/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8_MC_2018_09Apr2023_PUB_1/230408_232001/0000/HTauTauAnalysis_1.root')

# print(df.Count().GetValue())
calc_func = lambda px, py, pz, e: big_ntuple.calc_ak8jets_pT(px, py, pz, e)
# df = df.Define('ak8jets_pT', lambda px, py, pz, e: big_ntuple.calc_ak8jets_pT(px, py, pz, e), ['ak8jets_px', 'ak8jets_py', 'ak8jets_pz', 'ak8jets_e'])
df = df.Define('ak8jets_pT', 'calc_ak8jets_pT(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e)')

# df = df.Filter('Big_Ntuple::cut_leading_ak8jets_pT(ak8jets_px)')
print(df.Count().GetValue())



# # Call member functions
# ak8jets_px = R.std.vector('float')()
# ak8jets_py = R.std.vector('float')()
# ak8jets_pz = R.std.vector('float')()
# ak8jets_e = R.std.vector('float')()

# # Fill the vectors with some values
# ak8jets_px.push_back(100.0)
# ak8jets_py.push_back(200.0)
# ak8jets_pz.push_back(300.0)
# ak8jets_e.push_back(400.0)

# ak8jets_pT = big_ntuple.calc_ak8jets_pT(ak8jets_px, ak8jets_py, ak8jets_pz, ak8jets_e)
# ak8jets_pT.push_back(251.0)
# print(ak8jets_pT)

# trigger = big_ntuple.cut_leading_ak8jets_pT(ak8jets_pT[0])
# print(trigger)
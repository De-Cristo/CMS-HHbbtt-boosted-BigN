#!/bin/bash

python scripts/analyzer.py -m 100 -s 1 -re True

python scripts/analyzer.py -m 100 -s 2 -o slimmed_ntuple_test

python scripts/analyzer.py -m 100 -s 123 -o slimmed_ntuple_test

hadd TTbarSemi/HTauTauAnalysis_0.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_1-*.root &

hadd TTbarSemi/HTauTauAnalysis_1.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_1.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_10*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_11*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_12*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_13*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_14*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_15*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_16*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_17*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_18*.root ../AK8based_Out_618/TTbarHad/HTauTauAnalysis_19*.root &

hadd TTbarSemi/HTauTauAnalysis_2.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_2*.root &
hadd TTbarSemi/HTauTauAnalysis_3.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_3*.root &
hadd TTbarSemi/HTauTauAnalysis_4.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_4*.root &
hadd TTbarSemi/HTauTauAnalysis_5.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_5*.root &
hadd TTbarSemi/HTauTauAnalysis_6.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_6*.root &
hadd TTbarSemi/HTauTauAnalysis_7.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_7*.root &
hadd TTbarSemi/HTauTauAnalysis_8.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_8*.root &
hadd TTbarSemi/HTauTauAnalysis_9.root ../AK8based_Out_618/TTbarSemi/HTauTauAnalysis_9*.root &


#ifndef PROC_BIG_NTUPLE_HH
#define PROC_BIG_NTUPLE_HH

#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "TCanvas.h"
#include "TH1D.h"
#include "TLatex.h"
#include "Math/Vector4D.h"
#include "TStyle.h"
 
using namespace ROOT;
using namespace ROOT::VecOps;
using RNode = ROOT::RDF::RNode;

class Big_Ntuple{
    public:
        Big_Ntuple();
        ~Big_Ntuple();
        RVecF calc_ak8jets_pT(RVecF ak8jets_px, RVecF ak8jets_py, RVecF ak8jets_pz, RVecF ak8jets_e);
        float calc_leading_ak8jet_pT(RVecF ak8jets_pT);
        bool cut_leading_ak8jets_pT(float leading_ak8jet_pT);
    private:
        float leading_ak8jets_pT_min = 250.;
    
};

#endif
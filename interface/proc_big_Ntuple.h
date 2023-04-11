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

RVecF calc_ak8jets_pT(RVecF ak8jets_px, RVecF ak8jets_py, RVecF ak8jets_pz, RVecF ak8jets_e)
{
    auto length_ = ak8jets_px.size();
    RVecF ak8jets_pT(length_);
    for (int i = 0; i < length_ ; i++) {
        ROOT::Math::PxPyPzEVector ak8jet(ak8jets_px[i], ak8jets_py[i], ak8jets_pz[i], ak8jets_e[i]);
        ak8jets_pT[i] = ak8jet.Pt();
    }
   return ak8jets_pT;
}

float calc_leading_ak8jet_pT(RVecF ak8jets_pT)
{
    auto ak8jets_pT_sorted = Reverse(Sort(ak8jets_pT));
    return ak8jets_pT_sorted[0];
}

bool cut_leading_ak8jets_pT(float leading_ak8jet_pT)
{
    if (leading_ak8jet_pT > 250) {
        return true;
    }
    return false;
}


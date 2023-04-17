#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "TCanvas.h"
#include "TH1D.h"
#include "TLatex.h"
#include "Math/Vector4D.h"
#include "TStyle.h"

using namespace std;
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

bool CheckBit (int number, int bitpos)
{
  bool res = number & (1 << bitpos);
  return res;
}

RVecF HiggsGenInfoVector(
    ULong64_t EventNumber,
    RVecF genpart_px, 
    RVecF genpart_py, 
    RVecF genpart_pz,
    RVecF genpart_e, 
    RVecF genpart_flags,
    RVecF genpart_pdg,
    RVecF genpart_TauMothInd,
    RVecF genpart_HMothInd,
    RVecF genpart_TauGenDecayMode,
    RVecF genpart_HZDecayMode
    )
{
    RVecF GenInfo(34);
    float h_status = -999.; // 0. 
    float tau_status = -999.; // 1. 
    float b_status = -999.; // 2. 
    
    float HbbE = -999.; // 3.
    float HbbPt = -999.; // 4.
    float HbbEta = -999.; // 5.
    float HbbPhi = -999.; // 6.
    float HbbM = -999.; // 7.
    
    float HtautauE = -999.; // 8.
    float HtautauPt = -999.; // 9.
    float HtautauEta = -999.; // 10.
    float HtautauPhi = -999.; // 11.
    float HtautauM = -999.; // 12.
    
    float Hb1E = -999.; // 13.
    float Hb1Pt = -999.; // 14.
    float Hb1Eta = -999.; // 15.
    float Hb1Phi = -999.; // 16.
    
    float Hb2E = -999.; // 17.
    float Hb2Pt = -999.; // 18.
    float Hb2Eta = -999.; // 19.
    float Hb2Phi = -999.; // 20.
    
    float Htau1E = -999.; // 21.
    float Htau1Pt = -999.; // 22.
    float Htau1Eta = -999.; // 23.
    float Htau1Phi = -999.; // 24.
    
    float Htau2E = -999.; // 25.
    float Htau2Pt = -999.; // 26.
    float Htau2Eta = -999.; // 27.
    float Htau2Phi = -999.; // 28.
    
    float HHE = -999.; // 29.
    float HHPt = -999.; // 30.
    float HHEta = -999.; // 31.
    float HHPhi = -999.; // 32.
    float HHM = -999.; // 33.
    /*
    GenInfo  --> [h_status, tau_status, b_status,
                  HbbE, HbbPt, HbbEta, HbbPhi, HbbM,
                  HtautauE, HtautauPt, HtautauEta, HtautauPhi, HtautauM,
                  Hb1E, Hb1Pt, Hb1Eta, Hb1Phi,
                  Hb2E, Hb2Pt, Hb2Eta, Hb2Phi,
                  Htau1E, Htau1Pt, Htau1Eta, Htau1Phi,
                  Htau2E, Htau2Pt, Htau2Eta, Htau2Phi,
                  HHE, HHPt, HHEta, HHPhi, HHM
                  ]
                  
    the following are check in Higgs -> b -> tau order (that is what quit and keep means)
    h_status == -999. find 0 Higgs and other
    h_status == -1. did not find 2 Higgs (first Higgs). fill default.
    h_status == -2. did not find 2 Higgs (last Higgs). fill default.
    h_status == 0. find 2 Higgs. correct
    h_status == 1. find only 1 Higgs (to 2tau).
    h_status == 2. find only 1 Higgs (to 2b).
    h_status == 3. find more than 2 Higgs (first Higgs). quit.
    h_status == 4. find more than 2 Higgs (last Higgs) keep.
    
    b_status == -999. find 0 Bs and other
    b_status == 0. find 2 Bs from Higgs. correct
    b_status == 1. find only 1 B (from Higgs). fill default.
    b_status == 3. find more than 2 Bs (from Higgs). keep.
    
    tau_status == -999. find 0 Taus and other
    tau_status == 0. find 2 taus from Higgs. correct
    tau_status == 1. find only 1 tau (from Higgs). fill default.
    tau_status == 3. find more than 2 taus (from Higgs). keep.
    tau_status == -999.+n find n taus not from Higgs or tau->tau chain.
    
    */
    
    int idx1hs_b = -1;     // bjet-1 index     // FRA DEBUG
    int idx2hs_b = -1;     // bjet-2 index
    TLorentzVector vGenB1; // bjet-1 tlv
    TLorentzVector vGenB2; // bjet-2 tlv
    int idx1hs_tau = -1;
    int idx2hs_tau = -1;
    TLorentzVector vGenTau1;
    TLorentzVector vGenTau2;
    
    TLorentzVector vHtautau, vHbb, vHH; // boost? vHtautau.Boost(-vSum.BoostVector());
    // float ct1 = -999; // not used until boost
    
    // loop to find Higgs
    int idx1 = -1;
    int idx2 = -1;
    int idx1last = -1;
    int idx2last = -1;
    
    for (unsigned int igen = 0; igen < genpart_px.size(); igen++)
    {        
        bool isFirst     = CheckBit (genpart_flags[igen], 12) ; // 12 = isFirstCopy
        bool isLast      = CheckBit (genpart_flags[igen], 13) ; // 13 = isLastCopy        
        // bool isDirectPromptTauDecayProduct = CheckBit (genpart_flags[igen], 5) ; //  5 = isDirectPromptTauDecayProduct
        bool isTauHadronicDecay = (genpart_TauGenDecayMode[igen] == 2); // -1 = not tau, 0 = mu, 1 = ele, 2 = had
        bool isHardProcess = CheckBit (genpart_flags[igen], 7) ; //  7 = isHardProcess, for b coming from H
        int pdg = genpart_pdg[igen];
        
        if (abs(pdg) == 25){
            if (isFirst){
                if (idx1 >= 0 && idx2 >= 0){h_status = 3.; continue;} // more than 2 H (first) identified
                (idx1 == -1) ? (idx1 = igen) : (idx2 = igen) ;
            }
            if (isLast){
                if (idx1last >= 0 && idx2last >= 0){h_status = 4.;} // more than 2 H (last) identified
                // no need to skip the event in this case -- dec mode just for studies
                (idx1last == -1) ? (idx1last = igen) : (idx2last = igen) ;
            }
        }
        
        if ( abs(pdg) == 5 && isHardProcess){
            // is it necessary to check it is from Higgs and Higgs -> Higgs chain?
            if (idx1hs_b == -1){idx1hs_b = igen;} else if (idx2hs_b == -1){idx2hs_b = igen;} else{b_status = 3.;}
        }
        

//         int hmothIdx = genpart_HMothInd[igen];
//         int taumothIdx = genpart_TauMothInd[igen];
//         bool mothIsHardScattH = false;
//         if ( (abs(pdg) == 15) && isTauHadronicDecay && isLast) {
//              /* NB: I need trace the last tau to the first tau and proof that it is from Higgs, 
//                 otherwise I get a nonphysics "tauh" by the tauh builder function 
//                 from the tau->tau "decay" in pythia or taus not from hard process Higgs */
//             if (taumothIdx > -1){
//                 // tau is from tau->tau decay
//                 auto taumothIdx_last = taumothIdx;
//                 cout << "evt: " << EventNumber << " I am diving into the tau->tau chain while " << endl;
//                 int _i = 0;
//                 while (taumothIdx > -1){
//                     taumothIdx_last = taumothIdx;
//                     taumothIdx = genpart_TauMothInd[taumothIdx];
//                     _i++;
//                     if (_i%100 == 1){cout << "evt: " << EventNumber << " Help! " << endl;}
//                 }
//                 cout << "evt: " << EventNumber << " OK! I'm out " << endl;
//                 hmothIdx = genpart_HMothInd[taumothIdx_last];
//                 auto hmothIdx_last = hmothIdx; // Higgs also have this Higgs->Higgs chain?
//                 while (hmothIdx > -1){
//                     hmothIdx_last = hmothIdx;
//                     hmothIdx = genpart_HMothInd[hmothIdx];
//                 }
//                 hmothIdx = hmothIdx_last;
//                 if ( CheckBit (genpart_flags[hmothIdx], 7) ){
//                     mothIsHardScattH = true;
//                     if (idx1hs_tau == -1){idx1hs_tau = igen;} else if (idx2hs_tau == -1){idx2hs_tau = igen;} else{tau_status = 3.; continue;}
//                 }
//             }else if (hmothIdx > -1){
//                 tau is from Higgs decay
//                 auto hmothIdx_last = hmothIdx;
//                 while (hmothIdx > -1){
//                     hmothIdx_last = hmothIdx;
//                     hmothIdx = genpart_HMothInd[hmothIdx];
//                 }
//                 hmothIdx = hmothIdx_last;
//                 if ( CheckBit (genpart_flags[hmothIdx], 7) ){
//                     mothIsHardScattH = true;
//                     if (idx1hs_tau == -1){idx1hs_tau = igen;} else if (idx2hs_tau == -1){idx2hs_tau = igen;} else{tau_status = 3.; continue;}
//                 }
//             }else{tau_status = tau_status+1;} // find a tau not from Higgs or tau->tau
//         }

        int hmothIdx = genpart_HMothInd[igen];
        int taumothIdx = genpart_TauMothInd[igen];
        bool mothIsHardScattH = false;
        if ( (abs(pdg) == 15) && isTauHadronicDecay && isFirst) {
            if (hmothIdx>-1){
                if (idx1hs_tau == -1){idx1hs_tau = igen;} else if (idx2hs_tau == -1){idx2hs_tau = igen;} else{tau_status = 3.; continue;}
            }
        }
        
     
    }



    
    if (idx1 == -1 || idx2 == -1){
        cout << "** ERROR: couldn't find 2 H (first): evt = " << EventNumber << endl;
        h_status = -1;
    }else{
        
        if (idx1last != -1 && idx2last != -1){ 
            h_status = 0.; //good event!
            // this is not critical if not found
            // store gen decay mode of the two H identified
            auto H1_genDecMode = genpart_HZDecayMode[idx1last];
            auto H2_genDecMode = genpart_HZDecayMode[idx2last];
            // get tau decaying one and the other will be b decaying one (CHECK THIS) confusing...
            // from https://github.com/De-Cristo/KLUBAnalysis/blob/AprFool_Licheng_MIB/test/skimNtuple2018_HHbtag.cpp#L1368
            // from https://github.com/De-Cristo/LLRHiggsTauTau/blob/106X_HH_UL/NtupleProducer/interface/GenHelper.h#L21
            int idxTauDecayed = (H1_genDecMode != 8 ? idx1last : idx2last);
            int idxBDecayed = (H1_genDecMode != 8 ? idx2last : idx1last);
            
            if (idx1hs_tau != -1 && idx2hs_tau != -1){
                tau_status = 0.;
                vGenTau1.SetPxPyPzE(genpart_px[idx1hs_tau], genpart_py[idx1hs_tau], genpart_pz[idx1hs_tau], genpart_e[idx1hs_tau]);
                vGenTau2.SetPxPyPzE(genpart_px[idx2hs_tau], genpart_py[idx2hs_tau], genpart_pz[idx2hs_tau], genpart_e[idx2hs_tau]);
                auto vGenTau = vGenTau2;
                if (vGenTau1.Pt() < vGenTau2.M()){vGenTau2 = vGenTau1; vGenTau1 = vGenTau;} else{;}
                                
                Htau1E = vGenTau1.E();
                Htau2E = vGenTau2.E();
                Htau1Pt = vGenTau1.Pt();
                Htau2Pt = vGenTau2.Pt();
                Htau1Phi = vGenTau1.Phi();
                Htau2Phi = vGenTau2.Phi();
                Htau1Eta = vGenTau1.Eta();
                Htau2Eta = vGenTau2.Eta();
                
            }else if((idx1hs_tau == -1 || idx2hs_tau == -1) && idx1hs_tau+idx2hs_tau != -2){ tau_status = 1.;}else{;}

            if (idx1hs_b != -1 && idx2hs_b != -1){
                b_status = 0.;
                vGenB1.SetPxPyPzE(genpart_px[idx1hs_b], genpart_py[idx1hs_b], genpart_pz[idx1hs_b], genpart_e[idx1hs_b]);
                vGenB2.SetPxPyPzE(genpart_px[idx2hs_b], genpart_py[idx2hs_b], genpart_pz[idx2hs_b], genpart_e[idx2hs_b]);
                auto vGenB = vGenB2;
                if (vGenB1.Pt() < vGenB2.M()){vGenB2 = vGenB1; vGenB1 = vGenB;} else{;}
                Hb1E = vGenB1.E();
                Hb2E = vGenB2.E();
                Hb1Pt = vGenB1.Pt();
                Hb2Pt = vGenB2.Pt();
                Hb1Phi = vGenB1.Phi();
                Hb2Phi = vGenB2.Phi();
                Hb1Eta = vGenB1.Eta();
                Hb2Eta = vGenB2.Eta();

            }else if((idx1hs_b == -1 || idx2hs_b == -1) && idx1hs_b+idx2hs_b == -1){ b_status = 1.;}else{;}

            vHtautau.SetPxPyPzE(genpart_px[idxTauDecayed], genpart_py[idxTauDecayed], genpart_pz[idxTauDecayed], genpart_e[idxTauDecayed]);
            vHbb.SetPxPyPzE(genpart_px[idxBDecayed], genpart_py[idxBDecayed], genpart_pz[idxBDecayed], genpart_e[idxBDecayed]);
            
            HtautauE = vHtautau.E();
            HbbE = vHbb.E();
            HtautauPt = vHtautau.Pt();
            HbbPt = vHbb.Pt();
            HtautauPhi = vHtautau.Phi();
            HbbPhi = vHbb.Phi();
            HtautauEta = vHtautau.Eta();
            HbbEta = vHbb.Eta();
            HtautauM = vHtautau.M();
            HbbM = vHbb.M();
            
            vHH = vHtautau + vHbb;
            HHE = vHH.E();
            HHPt = vHH.Pt();
            HHPhi = vHH.Phi();
            HHEta = vHH.Eta();
            HHM = vHH.M();            
            
        }else{h_status = -2.; cout << "** ERROR: couldn't find 2 H (last)" << endl;} 
        // before here we could have check the missed higgs is bb or tautau.    
    }
    
    GenInfo[0] = h_status; // 0.
    GenInfo[1] = tau_status; // 1.
    GenInfo[2] = b_status; // 2.
    
    GenInfo[3] = HbbE; // 3.
    GenInfo[4] = HbbPt; //4.
    GenInfo[5] = HbbEta; //5.
    GenInfo[6] = HbbPhi; //6.
    GenInfo[7] = HbbM; //7.
    
    GenInfo[8] = HtautauE; //8.
    GenInfo[9] = HtautauPt; //9.
    GenInfo[10] = HtautauEta; //10.
    GenInfo[11] = HtautauPhi; //11.
    GenInfo[12] = HtautauM; //12.
    
    GenInfo[13] = Hb1E; //13.
    GenInfo[14] = Hb1Pt; //14.
    GenInfo[15] = Hb1Eta; //15.
    GenInfo[16] = Hb1Phi; //16.
    
    GenInfo[17] = Hb2E; //17.
    GenInfo[18] = Hb2Pt; //18.
    GenInfo[19] = Hb2Eta; //19.
    GenInfo[20] = Hb2Phi; //20.
    
    GenInfo[21] = Htau1E; //21.
    GenInfo[22] = Htau1Pt; //22.
    GenInfo[23] = Htau1Eta; //23.
    GenInfo[24] = Htau1Phi; //24.
    
    GenInfo[25] = Htau2E; //25.
    GenInfo[26] = Htau2Pt; //26.
    GenInfo[27] = Htau2Eta; //27.
    GenInfo[28] = Htau2Phi; //28.
    
    GenInfo[29] = HHE; //29.
    GenInfo[30] = HHPt; //30.
    GenInfo[31] = HHPhi; //31.
    GenInfo[23] = HHEta; //32.
    GenInfo[33] = HHM; //33.
    
    return GenInfo;
}

float HiggsGenInfoTransformer(RVecF HiggsGenInfoVector, int v_idx)
{
    return HiggsGenInfoVector[v_idx];
}
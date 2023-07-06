//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Feb 22 22:36:51 2023 by ROOT version 6.26/10
// from TTree HTauTauTree/HTauTauTree
// found on file: /gwteras/cms/store/user/lichengz/NonResonantHHbbtautauNtuples/MC_2018_21Feb2023/2_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_MC_2018_21Feb2023_2/230221_234753/0001//HTauTauAnalysis_1-1000.root
//////////////////////////////////////////////////////////

#ifndef BigN_h
#define BigN_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"
#include "vector"
#include "vector"
#include "vector"
#include "TString.h"

class BigN {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   ULong64_t       EventNumber;
   Int_t           RunNumber;
   Int_t           lumi;
   Int_t           year;
   Float_t         prefiringweight;
   Float_t         prefiringweightup;
   Float_t         prefiringweightdown;
   Long64_t        triggerbit;
   Int_t           metfilterbit;
   Float_t         met;
   Float_t         met_er;
   Float_t         met_er_phi;
   Float_t         metphi;
   vector<float>   *daughters_IetaIeta;
   vector<float>   *daughters_full5x5_IetaIeta;
   vector<float>   *daughters_hOverE;
   vector<float>   *daughters_deltaEtaSuperClusterTrackAtVtx;
   vector<float>   *daughters_deltaPhiSuperClusterTrackAtVtx;
   vector<float>   *daughters_IoEmIoP;
   vector<float>   *daughters_IoEmIoP_ttH;
   Float_t         PFMETCov00;
   Float_t         PFMETCov01;
   Float_t         PFMETCov10;
   Float_t         PFMETCov11;
   Float_t         PFMETsignif;
   Float_t         PUPPImet;
   Float_t         PUPPImetphi;
   Float_t         PUPPImetShifted;
   Float_t         PUPPImetShiftedphi;
   Float_t         PuppiMETCov00;
   Float_t         PuppiMETCov01;
   Float_t         PuppiMETCov10;
   Float_t         PuppiMETCov11;
   Float_t         PuppiMETsignif;
   Float_t         DeepMETresponseTune_pt;
   Float_t         DeepMETresponseTune_phi;
   Float_t         DeepMETresolutionTune_pt;
   Float_t         DeepMETresolutionTune_phi;
   Float_t         ShiftedDeepMETresponseTune_pt;
   Float_t         ShiftedDeepMETresponseTune_phi;
   Float_t         ShiftedDeepMETresolutionTune_pt;
   Float_t         ShiftedDeepMETresolutionTune_phi;
   Int_t           npv;
   Float_t         npu;
   Float_t         rho;
   vector<float>   *mothers_px;
   vector<float>   *mothers_py;
   vector<float>   *mothers_pz;
   vector<float>   *mothers_e;
   vector<Long64_t> *mothers_trgSeparateMatch;
   vector<float>   *daughters_px;
   vector<float>   *daughters_py;
   vector<float>   *daughters_pz;
   vector<float>   *daughters_e;
   vector<int>     *daughters_charge;
   vector<float>   *L1_tauEt;
   vector<float>   *L1_tauEta;
   vector<float>   *L1_tauPhi;
   vector<short>   *L1_tauIso;
   vector<float>   *L1_jetEt;
   vector<float>   *L1_jetEta;
   vector<float>   *L1_jetPhi;
   vector<float>   *daughters_highestEt_L1IsoTauMatched;
   vector<int>     *daughters_hasTES;
   vector<float>   *daughters_px_TauUp;
   vector<float>   *daughters_py_TauUp;
   vector<float>   *daughters_pz_TauUp;
   vector<float>   *daughters_e_TauUp;
   vector<float>   *daughters_px_TauDown;
   vector<float>   *daughters_py_TauDown;
   vector<float>   *daughters_pz_TauDown;
   vector<float>   *daughters_e_TauDown;
   vector<float>   *daughters_TESshiftDM0;
   vector<float>   *daughters_TESshiftDM1;
   vector<float>   *daughters_TESshiftDM10;
   vector<float>   *daughters_TESshiftDM11;
   vector<int>     *daughters_hasEES;
   vector<float>   *daughters_px_EleUp;
   vector<float>   *daughters_py_EleUp;
   vector<float>   *daughters_pz_EleUp;
   vector<float>   *daughters_e_EleUp;
   vector<float>   *daughters_px_EleDown;
   vector<float>   *daughters_py_EleDown;
   vector<float>   *daughters_pz_EleDown;
   vector<float>   *daughters_e_EleDown;
   vector<float>   *daughters_EESshiftDM0up;
   vector<float>   *daughters_EESshiftDM0dw;
   vector<float>   *daughters_EESshiftDM1up;
   vector<float>   *daughters_EESshiftDM1dw;
   vector<float>   *daughters_MESshiftup;
   vector<float>   *daughters_MESshiftdw;
   vector<int>     *daughters_isTauMatched;
   Int_t           PUNumInteractions;
   vector<int>     *daughters_genindex;
   Float_t         MC_weight;
   Float_t         MC_weight_scale_muF0p5;
   Float_t         MC_weight_scale_muF2;
   Float_t         MC_weight_scale_muR0p5;
   Float_t         MC_weight_scale_muR2;
   Float_t         MC_weight_PSWeight0;
   Float_t         MC_weight_PSWeight1;
   Float_t         MC_weight_PSWeight2;
   Float_t         MC_weight_PSWeight3;
   Float_t         lheHt;
   Int_t           lheNOutPartons;
   Int_t           lheNOutB;
   Int_t           lheNOutC;
   Float_t         lheVPt;
   Float_t         aMCatNLOweight;
   vector<float>   *genpart_px;
   vector<float>   *genpart_py;
   vector<float>   *genpart_pz;
   vector<float>   *genpart_e;
   vector<int>     *genpart_pdg;
   vector<int>     *genpart_status;
   vector<int>     *genpart_HMothInd;
   vector<int>     *genpart_MSSMHMothInd;
   vector<int>     *genpart_TopMothInd;
   vector<int>     *genpart_TauMothInd;
   vector<int>     *genpart_ZMothInd;
   vector<int>     *genpart_WMothInd;
   vector<int>     *genpart_bMothInd;
   vector<int>     *genpart_HZDecayMode;
   vector<int>     *genpart_TopDecayMode;
   vector<int>     *genpart_WDecayMode;
   vector<int>     *genpart_TauGenDecayMode;
   vector<int>     *genpart_TauGenDetailedDecayMode;
   vector<int>     *genpart_flags;
   vector<float>   *genjet_px;
   vector<float>   *genjet_py;
   vector<float>   *genjet_pz;
   vector<float>   *genjet_e;
   vector<int>     *genjet_partonFlavour;
   vector<int>     *genjet_hadronFlavour;
   Int_t           NUP;
   vector<float>   *SVfitMass;
   vector<float>   *SVfitMassUnc;
   vector<float>   *SVfitTransverseMass;
   vector<float>   *SVfitTransverseMassUnc;
   vector<float>   *SVfit_pt;
   vector<float>   *SVfit_ptUnc;
   vector<float>   *SVfit_eta;
   vector<float>   *SVfit_etaUnc;
   vector<float>   *SVfit_phi;
   vector<float>   *SVfit_phiUnc;
   vector<float>   *SVfit_fitMETRho;
   vector<float>   *SVfit_fitMETPhi;
   vector<bool>    *isOSCand;
   Float_t         PUPPImetShiftedX;
   Float_t         PUPPImetShiftedY;
   vector<float>   *METx;
   vector<float>   *METy;
   vector<float>   *METx_UP_JES;
   vector<float>   *METy_UP_JES;
   vector<float>   *METx_DOWN_JES;
   vector<float>   *METy_DOWN_JES;
   vector<float>   *METx_UP_TES;
   vector<float>   *METy_UP_TES;
   vector<float>   *METx_DOWN_TES;
   vector<float>   *METy_DOWN_TES;
   vector<float>   *METx_UP_EES;
   vector<float>   *METy_UP_EES;
   vector<float>   *METx_DOWN_EES;
   vector<float>   *METy_DOWN_EES;
   vector<float>   *uncorrMETx;
   vector<float>   *uncorrMETy;
   vector<float>   *MET_cov00;
   vector<float>   *MET_cov01;
   vector<float>   *MET_cov10;
   vector<float>   *MET_cov11;
   vector<float>   *MET_significance;
   vector<float>   *mT_Dau1;
   vector<float>   *mT_Dau2;
   vector<int>     *PDGIdDaughters;
   vector<int>     *indexDau1;
   vector<int>     *indexDau2;
   vector<int>     *particleType;
   vector<int>     *daughters_muonID;
   vector<int>     *daughters_typeOfMuon;
   vector<float>   *dxy;
   vector<float>   *dz;
   vector<float>   *dxy_innerTrack;
   vector<float>   *dz_innerTrack;
   vector<float>   *daughters_rel_error_trackpt;
   vector<float>   *SIP;
   vector<bool>    *daughters_iseleWPLoose;
   vector<bool>    *daughters_iseleWP80;
   vector<bool>    *daughters_iseleWP90;
   vector<bool>    *daughters_iseleNoIsoWPLoose;
   vector<bool>    *daughters_iseleNoIsoWP80;
   vector<bool>    *daughters_iseleNoIsoWP90;
   vector<float>   *daughters_eleMVAnt;
   vector<float>   *daughters_eleMVA_HZZ;
   vector<bool>    *daughters_iseleChargeConsistent;
   vector<float>   *daughters_ecalTrkEnergyPostCorr;
   vector<float>   *daughters_ecalTrkEnergyErrPostCorr;
   vector<float>   *daughters_energyScaleUp;
   vector<float>   *daughters_energyScaleDown;
   vector<float>   *daughters_energySigmaUp;
   vector<float>   *daughters_energySigmaDown;
   vector<int>     *decayMode;
   vector<int>     *genmatch;
   vector<Long64_t> *tauID;
   vector<float>   *combreliso;
   vector<float>   *combreliso03;
   vector<float>   *daughters_depositR03_tracker;
   vector<float>   *daughters_depositR03_ecal;
   vector<float>   *daughters_depositR03_hcal;
   vector<int>     *daughters_decayModeFindingOldDMs;
   vector<int>     *daughters_decayModeFindingNewDMs;
   vector<float>   *daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits;
   vector<float>   *daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017;
   vector<float>   *daughters_byDeepTau2017v2p1VSjetraw;
   vector<float>   *daughters_byDeepTau2017v2p1VSeraw;
   vector<float>   *daughters_byDeepTau2017v2p1VSmuraw;
   vector<int>     *daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017;
   vector<float>   *daughters_chargedIsoPtSum;
   vector<float>   *daughters_neutralIsoPtSum;
   vector<float>   *daughters_puCorrPtSum;
   vector<int>     *daughters_numChargedParticlesSignalCone;
   vector<int>     *daughters_numNeutralHadronsSignalCone;
   vector<int>     *daughters_numPhotonsSignalCone;
   vector<int>     *daughters_daughters_numParticlesSignalCone;
   vector<int>     *daughters_numChargedParticlesIsoCone;
   vector<int>     *daughters_numNeutralHadronsIsoCone;
   vector<int>     *daughters_numPhotonsIsoCone;
   vector<int>     *daughters_numParticlesIsoCone;
   vector<float>   *daughters_leadChargedParticlePt;
   vector<float>   *daughters_trackRefPt;
   vector<Long64_t> *daughters_trgMatched;
   vector<Long64_t> *daughters_FilterFired;
   vector<Long64_t> *daughters_isGoodTriggerType;
   vector<Long64_t> *daughters_L3FilterFired;
   vector<Long64_t> *daughters_L3FilterFiredLast;
   vector<float>   *daughters_HLTpt;
   vector<int>     *daughters_jetNDauChargedMVASel;
   vector<float>   *daughters_miniRelIsoCharged;
   vector<float>   *daughters_miniRelIsoNeutral;
   vector<float>   *daughters_jetPtRel;
   vector<float>   *daughters_jetPtRatio;
   vector<float>   *daughters_jetBTagCSV;
   vector<float>   *daughters_jetBTagDeepCSV;
   vector<float>   *daughters_jetBTagDeepFlavor;
   Int_t           JetsNumber;
   vector<Long64_t> *jets_VBFleadFilterMatch;
   vector<Long64_t> *jets_VBFsubleadFilterMatch;
   vector<float>   *jets_px;
   vector<float>   *jets_py;
   vector<float>   *jets_pz;
   vector<float>   *jets_e;
   vector<float>   *jets_area;
   vector<float>   *jets_mT;
   vector<int>     *jets_Flavour;
   vector<int>     *jets_HadronFlavour;
   vector<int>     *jets_genjetIndex;
   vector<float>   *jets_PUJetID;
   vector<int>     *jets_PUJetID_WP;
   vector<float>   *jets_PUJetIDupdated;
   vector<int>     *jets_PUJetIDupdated_WP;
   vector<float>   *jets_vtxPt;
   vector<float>   *jets_vtxMass;
   vector<float>   *jets_vtx3dL;
   vector<float>   *jets_vtxNtrk;
   vector<float>   *jets_vtx3deL;
   vector<float>   *jets_leadTrackPt;
   vector<float>   *jets_leptonPtRel;
   vector<float>   *jets_leptonPt;
   vector<float>   *jets_leptonDeltaR;
   vector<float>   *jets_chEmEF;
   vector<float>   *jets_chHEF;
   vector<float>   *jets_nEmEF;
   vector<float>   *jets_nHEF;
   vector<float>   *jets_MUF;
   vector<int>     *jets_neMult;
   vector<int>     *jets_chMult;
   vector<float>   *bDiscriminator;
   vector<float>   *bCSVscore;
   vector<float>   *pfCombinedMVAV2BJetTags;
   vector<float>   *bDeepCSV_probb;
   vector<float>   *bDeepCSV_probbb;
   vector<float>   *bDeepCSV_probudsg;
   vector<float>   *bDeepCSV_probc;
   vector<float>   *bDeepCSV_probcc;
   vector<float>   *bDeepFlavor_probb;
   vector<float>   *bDeepFlavor_probbb;
   vector<float>   *bDeepFlavor_problepb;
   vector<float>   *bDeepFlavor_probc;
   vector<float>   *bDeepFlavor_probuds;
   vector<float>   *bDeepFlavor_probg;
   vector<float>   *bParticleNetAK4JetTags_probbb;
   vector<float>   *bParticleNetAK4JetTags_probpu;
   vector<float>   *bParticleNetAK4JetTags_probcc;
   vector<float>   *bParticleNetAK4JetTags_probundef;
   vector<float>   *bParticleNetAK4JetTags_probc;
   vector<float>   *bParticleNetAK4JetTags_probb;
   vector<float>   *bParticleNetAK4JetTags_probuds;
   vector<float>   *bParticleNetAK4JetTags_probg;
   vector<float>   *jets_bjetRegCorr;
   vector<float>   *jets_bjetRegRes;
   vector<float>   *bParticleNetTauAK4JetTags_probmu;
   vector<float>   *bParticleNetTauAK4JetTags_probele;
   vector<float>   *bParticleNetTauAK4JetTags_probtaup1h0p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaup1h1p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaup1h2p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaup3h0p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaup3h1p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaum1h0p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaum1h1p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaum1h2p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaum3h0p;
   vector<float>   *bParticleNetTauAK4JetTags_probtaum3h1p;
   vector<float>   *bParticleNetTauAK4JetTags_probb;
   vector<float>   *bParticleNetTauAK4JetTags_probc;
   vector<float>   *bParticleNetTauAK4JetTags_probuds;
   vector<float>   *bParticleNetTauAK4JetTags_probg;
   vector<float>   *bParticleNetTauAK4JetTags_ptcorr;
   vector<float>   *bParticleNetTauAK4JetTags_ptreshigh;
   vector<float>   *bParticleNetTauAK4JetTags_ptreslow;
   vector<int>     *PFjetID;
   vector<float>   *jetRawf;
   vector<float>   *jets_JER;
   TString         *susyModel;
   vector<float>   *ak8jets_px;
   vector<float>   *ak8jets_py;
   vector<float>   *ak8jets_pz;
   vector<float>   *ak8jets_e;
   vector<float>   *ak8jets_SoftDropMass;
   vector<float>   *ak8jets_PrunedMass;
   vector<float>   *ak8jets_TrimmedMass;
   vector<float>   *ak8jets_FilteredMass;
   vector<float>   *ak8jets_tau1;
   vector<float>   *ak8jets_tau2;
   vector<float>   *ak8jets_tau3;
   vector<float>   *ak8jets_tau4;
   vector<float>   *ak8jets_CSV;
   vector<float>   *ak8jets_deepCSV_probb;
   vector<float>   *ak8jets_deepCSV_probbb;
   vector<float>   *ak8jets_deepFlavor_probb;
   vector<float>   *ak8jets_deepFlavor_probbb;
   vector<float>   *ak8jets_deepFlavor_problepb;
   vector<float>   *ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb;
   vector<float>   *ak8jets_deepDoubleBvLJetTags_probHbb;
   vector<float>   *ak8jets_deepBoostedJetTags_probHbb;
   vector<float>   *ak8jets_particleNetJetTags_probHbb;
   vector<float>   *ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD;
   vector<int>     *ak8jets_nsubjets;
   vector<float>   *bParticleNetTauAK8JetTags_probHtt;
   vector<float>   *bParticleNetTauAK8JetTags_probHtm;
   vector<float>   *bParticleNetTauAK8JetTags_probHte;
   vector<float>   *bParticleNetTauAK8JetTags_probHbb;
   vector<float>   *bParticleNetTauAK8JetTags_probHcc;
   vector<float>   *bParticleNetTauAK8JetTags_probHqq;
   vector<float>   *bParticleNetTauAK8JetTags_probHgg;
   vector<float>   *bParticleNetTauAK8JetTags_probQCD2hf;
   vector<float>   *bParticleNetTauAK8JetTags_probQCD1hf;
   vector<float>   *bParticleNetTauAK8JetTags_probQCD0hf;
   vector<float>   *bParticleNetTauAK8JetTags_masscorr;
   vector<float>   *subjets_px;
   vector<float>   *subjets_py;
   vector<float>   *subjets_pz;
   vector<float>   *subjets_e;
   vector<float>   *subjets_CSV;
   vector<float>   *subjets_deepCSV_probb;
   vector<float>   *subjets_deepCSV_probbb;
   vector<float>   *subjets_deepFlavor_probb;
   vector<float>   *subjets_deepFlavor_probbb;
   vector<float>   *subjets_deepFlavor_problepb;
   vector<int>     *subjets_ak8MotherIdx;
   Float_t         pvGen_x;
   Float_t         pvGen_y;
   Float_t         pvGen_z;

   // List of branches
   TBranch        *b_EventNumber;   //!
   TBranch        *b_RunNumber;   //!
   TBranch        *b_lumi;   //!
   TBranch        *b_year;   //!
   TBranch        *b_prefiringweight;   //!
   TBranch        *b_prefiringweightup;   //!
   TBranch        *b_prefiringweightdown;   //!
   TBranch        *b_triggerbit;   //!
   TBranch        *b_metfilterbit;   //!
   TBranch        *b_met;   //!
   TBranch        *b_met_er;   //!
   TBranch        *b_met_er_phi;   //!
   TBranch        *b_metphi;   //!
   TBranch        *b_daughters_IetaIeta;   //!
   TBranch        *b_daughters_full5x5_IetaIeta;   //!
   TBranch        *b_daughters_hOverE;   //!
   TBranch        *b_daughters_deltaEtaSuperClusterTrackAtVtx;   //!
   TBranch        *b_daughters_deltaPhiSuperClusterTrackAtVtx;   //!
   TBranch        *b_daughters_IoEmIoP;   //!
   TBranch        *b_daughters_IoEmIoP_ttH;   //!
   TBranch        *b_PFMETCov00;   //!
   TBranch        *b_PFMETCov01;   //!
   TBranch        *b_PFMETCov10;   //!
   TBranch        *b_PFMETCov11;   //!
   TBranch        *b_PFMETsignif;   //!
   TBranch        *b_PUPPImet;   //!
   TBranch        *b_PUPPImetphi;   //!
   TBranch        *b_PUPPImetShifted;   //!
   TBranch        *b_PUPPImetShiftedphi;   //!
   TBranch        *b_PuppiMETCov00;   //!
   TBranch        *b_PuppiMETCov01;   //!
   TBranch        *b_PuppiMETCov10;   //!
   TBranch        *b_PuppiMETCov11;   //!
   TBranch        *b_PuppiMETsignif;   //!
   TBranch        *b_DeepMETresponseTune_pt;   //!
   TBranch        *b_DeepMETresponseTune_phi;   //!
   TBranch        *b_DeepMETresolutionTune_pt;   //!
   TBranch        *b_DeepMETresolutionTune_phi;   //!
   TBranch        *b_ShiftedDeepMETresponseTune_pt;   //!
   TBranch        *b_ShiftedDeepMETresponseTune_phi;   //!
   TBranch        *b_ShiftedDeepMETresolutionTune_pt;   //!
   TBranch        *b_ShiftedDeepMETresolutionTune_phi;   //!
   TBranch        *b_npv;   //!
   TBranch        *b_npu;   //!
   TBranch        *b_rho;   //!
   TBranch        *b_mothers_px;   //!
   TBranch        *b_mothers_py;   //!
   TBranch        *b_mothers_pz;   //!
   TBranch        *b_mothers_e;   //!
   TBranch        *b_mothers_trgSeparateMatch;   //!
   TBranch        *b_daughters_px;   //!
   TBranch        *b_daughters_py;   //!
   TBranch        *b_daughters_pz;   //!
   TBranch        *b_daughters_e;   //!
   TBranch        *b_daughters_charge;   //!
   TBranch        *b_L1_tauEt;   //!
   TBranch        *b_L1_tauEta;   //!
   TBranch        *b_L1_tauPhi;   //!
   TBranch        *b_L1_tauIso;   //!
   TBranch        *b_L1_jetEt;   //!
   TBranch        *b_L1_jetEta;   //!
   TBranch        *b_L1_jetPhi;   //!
   TBranch        *b_daughters_highestEt_L1IsoTauMatched;   //!
   TBranch        *b_daughters_hasTES;   //!
   TBranch        *b_daughters_px_TauUp;   //!
   TBranch        *b_daughters_py_TauUp;   //!
   TBranch        *b_daughters_pz_TauUp;   //!
   TBranch        *b_daughters_e_TauUp;   //!
   TBranch        *b_daughters_px_TauDown;   //!
   TBranch        *b_daughters_py_TauDown;   //!
   TBranch        *b_daughters_pz_TauDown;   //!
   TBranch        *b_daughters_e_TauDown;   //!
   TBranch        *b_daughters_TESshiftDM0;   //!
   TBranch        *b_daughters_TESshiftDM1;   //!
   TBranch        *b_daughters_TESshiftDM10;   //!
   TBranch        *b_daughters_TESshiftDM11;   //!
   TBranch        *b_daughters_hasEES;   //!
   TBranch        *b_daughters_px_EleUp;   //!
   TBranch        *b_daughters_py_EleUp;   //!
   TBranch        *b_daughters_pz_EleUp;   //!
   TBranch        *b_daughters_e_EleUp;   //!
   TBranch        *b_daughters_px_EleDown;   //!
   TBranch        *b_daughters_py_EleDown;   //!
   TBranch        *b_daughters_pz_EleDown;   //!
   TBranch        *b_daughters_e_EleDown;   //!
   TBranch        *b_daughters_EESshiftDM0up;   //!
   TBranch        *b_daughters_EESshiftDM0dw;   //!
   TBranch        *b_daughters_EESshiftDM1up;   //!
   TBranch        *b_daughters_EESshiftDM1dw;   //!
   TBranch        *b_daughters_MESshiftup;   //!
   TBranch        *b_daughters_MESshiftdw;   //!
   TBranch        *b_daughters_isTauMatched;   //!
   TBranch        *b_PUNumInteractions;   //!
   TBranch        *b_daughters_genindex;   //!
   TBranch        *b_MC_weight;   //!
   TBranch        *b_MC_weight_scale_muF0p5;   //!
   TBranch        *b_MC_weight_scale_muF2;   //!
   TBranch        *b_MC_weight_scale_muR0p5;   //!
   TBranch        *b_MC_weight_scale_muR2;   //!
   TBranch        *b_MC_weight_PSWeight0;   //!
   TBranch        *b_MC_weight_PSWeight1;   //!
   TBranch        *b_MC_weight_PSWeight2;   //!
   TBranch        *b_MC_weight_PSWeight3;   //!
   TBranch        *b_lheHt;   //!
   TBranch        *b_lheNOutPartons;   //!
   TBranch        *b_lheNOutB;   //!
   TBranch        *b_lheNOutC;   //!
   TBranch        *b_lheVPt;   //!
   TBranch        *b_aMCatNLOweight;   //!
   TBranch        *b_genpart_px;   //!
   TBranch        *b_genpart_py;   //!
   TBranch        *b_genpart_pz;   //!
   TBranch        *b_genpart_e;   //!
   TBranch        *b_genpart_pdg;   //!
   TBranch        *b_genpart_status;   //!
   TBranch        *b_genpart_HMothInd;   //!
   TBranch        *b_genpart_MSSMHMothInd;   //!
   TBranch        *b_genpart_TopMothInd;   //!
   TBranch        *b_genpart_TauMothInd;   //!
   TBranch        *b_genpart_ZMothInd;   //!
   TBranch        *b_genpart_WMothInd;   //!
   TBranch        *b_genpart_bMothInd;   //!
   TBranch        *b_genpart_HZDecayMode;   //!
   TBranch        *b_genpart_TopDecayMode;   //!
   TBranch        *b_genpart_WDecayMode;   //!
   TBranch        *b_genpart_TauGenDecayMode;   //!
   TBranch        *b_genpart_TauGenDetailedDecayMode;   //!
   TBranch        *b_genpart_flags;   //!
   TBranch        *b_genjet_px;   //!
   TBranch        *b_genjet_py;   //!
   TBranch        *b_genjet_pz;   //!
   TBranch        *b_genjet_e;   //!
   TBranch        *b_genjet_partonFlavour;   //!
   TBranch        *b_genjet_hadronFlavour;   //!
   TBranch        *b_NUP;   //!
   TBranch        *b_SVfitMass;   //!
   TBranch        *b_SVfitMassUnc;   //!
   TBranch        *b_SVfitTransverseMass;   //!
   TBranch        *b_SVfitTransverseMassUnc;   //!
   TBranch        *b_SVfit_pt;   //!
   TBranch        *b_SVfit_ptUnc;   //!
   TBranch        *b_SVfit_eta;   //!
   TBranch        *b_SVfit_etaUnc;   //!
   TBranch        *b_SVfit_phi;   //!
   TBranch        *b_SVfit_phiUnc;   //!
   TBranch        *b_SVfit_fitMETRho;   //!
   TBranch        *b_SVfit_fitMETPhi;   //!
   TBranch        *b_isOSCand;   //!
   TBranch        *b_PUPPImetShiftedX;   //!
   TBranch        *b_PUPPImetShiftedY;   //!
   TBranch        *b_METx;   //!
   TBranch        *b_METy;   //!
   TBranch        *b_METx_UP_JES;   //!
   TBranch        *b_METy_UP_JES;   //!
   TBranch        *b_METx_DOWN_JES;   //!
   TBranch        *b_METy_DOWN_JES;   //!
   TBranch        *b_METx_UP_TES;   //!
   TBranch        *b_METy_UP_TES;   //!
   TBranch        *b_METx_DOWN_TES;   //!
   TBranch        *b_METy_DOWN_TES;   //!
   TBranch        *b_METx_UP_EES;   //!
   TBranch        *b_METy_UP_EES;   //!
   TBranch        *b_METx_DOWN_EES;   //!
   TBranch        *b_METy_DOWN_EES;   //!
   TBranch        *b_uncorrMETx;   //!
   TBranch        *b_uncorrMETy;   //!
   TBranch        *b_MET_cov00;   //!
   TBranch        *b_MET_cov01;   //!
   TBranch        *b_MET_cov10;   //!
   TBranch        *b_MET_cov11;   //!
   TBranch        *b_MET_significance;   //!
   TBranch        *b_mT_Dau1;   //!
   TBranch        *b_mT_Dau2;   //!
   TBranch        *b_PDGIdDaughters;   //!
   TBranch        *b_indexDau1;   //!
   TBranch        *b_indexDau2;   //!
   TBranch        *b_particleType;   //!
   TBranch        *b_daughters_muonID;   //!
   TBranch        *b_daughters_typeOfMuon;   //!
   TBranch        *b_dxy;   //!
   TBranch        *b_dz;   //!
   TBranch        *b_dxy_innerTrack;   //!
   TBranch        *b_dz_innerTrack;   //!
   TBranch        *b_daughters_rel_error_trackpt;   //!
   TBranch        *b_SIP;   //!
   TBranch        *b_daughters_iseleWPLoose;   //!
   TBranch        *b_daughters_iseleWP80;   //!
   TBranch        *b_daughters_iseleWP90;   //!
   TBranch        *b_daughters_iseleNoIsoWPLoose;   //!
   TBranch        *b_daughters_iseleNoIsoWP80;   //!
   TBranch        *b_daughters_iseleNoIsoWP90;   //!
   TBranch        *b_daughters_eleMVAnt;   //!
   TBranch        *b_daughters_eleMVA_HZZ;   //!
   TBranch        *b_daughters_iseleChargeConsistent;   //!
   TBranch        *b_daughters_ecalTrkEnergyPostCorr;   //!
   TBranch        *b_daughters_ecalTrkEnergyErrPostCorr;   //!
   TBranch        *b_daughters_energyScaleUp;   //!
   TBranch        *b_daughters_energyScaleDown;   //!
   TBranch        *b_daughters_energySigmaUp;   //!
   TBranch        *b_daughters_energySigmaDown;   //!
   TBranch        *b_decayMode;   //!
   TBranch        *b_genmatch;   //!
   TBranch        *b_tauID;   //!
   TBranch        *b_combreliso;   //!
   TBranch        *b_combreliso03;   //!
   TBranch        *b_daughters_depositR03_tracker;   //!
   TBranch        *b_daughters_depositR03_ecal;   //!
   TBranch        *b_daughters_depositR03_hcal;   //!
   TBranch        *b_daughters_decayModeFindingOldDMs;   //!
   TBranch        *b_daughters_decayModeFindingNewDMs;   //!
   TBranch        *b_daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits;   //!
   TBranch        *b_daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017;   //!
   TBranch        *b_daughters_byDeepTau2017v2p1VSjetraw;   //!
   TBranch        *b_daughters_byDeepTau2017v2p1VSeraw;   //!
   TBranch        *b_daughters_byDeepTau2017v2p1VSmuraw;   //!
   TBranch        *b_daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017;   //!
   TBranch        *b_daughters_chargedIsoPtSum;   //!
   TBranch        *b_daughters_neutralIsoPtSum;   //!
   TBranch        *b_daughters_puCorrPtSum;   //!
   TBranch        *b_daughters_numChargedParticlesSignalCone;   //!
   TBranch        *b_daughters_numNeutralHadronsSignalCone;   //!
   TBranch        *b_daughters_numPhotonsSignalCone;   //!
   TBranch        *b_daughters_daughters_numParticlesSignalCone;   //!
   TBranch        *b_daughters_numChargedParticlesIsoCone;   //!
   TBranch        *b_daughters_numNeutralHadronsIsoCone;   //!
   TBranch        *b_daughters_numPhotonsIsoCone;   //!
   TBranch        *b_daughters_numParticlesIsoCone;   //!
   TBranch        *b_daughters_leadChargedParticlePt;   //!
   TBranch        *b_daughters_trackRefPt;   //!
   TBranch        *b_daughters_trgMatched;   //!
   TBranch        *b_daughters_FilterFired;   //!
   TBranch        *b_daughters_isGoodTriggerType;   //!
   TBranch        *b_daughters_L3FilterFired;   //!
   TBranch        *b_daughters_L3FilterFiredLast;   //!
   TBranch        *b_daughters_HLTpt;   //!
   TBranch        *b_daughters_jetNDauChargedMVASel;   //!
   TBranch        *b_daughters_miniRelIsoCharged;   //!
   TBranch        *b_daughters_miniRelIsoNeutral;   //!
   TBranch        *b_daughters_jetPtRel;   //!
   TBranch        *b_daughters_jetPtRatio;   //!
   TBranch        *b_daughters_jetBTagCSV;   //!
   TBranch        *b_daughters_jetBTagDeepCSV;   //!
   TBranch        *b_daughters_jetBTagDeepFlavor;   //!
   TBranch        *b_JetsNumber;   //!
   TBranch        *b_jets_VBFleadFilterMatch;   //!
   TBranch        *b_jets_VBFsubleadFilterMatch;   //!
   TBranch        *b_jets_px;   //!
   TBranch        *b_jets_py;   //!
   TBranch        *b_jets_pz;   //!
   TBranch        *b_jets_e;   //!
   TBranch        *b_jets_area;   //!
   TBranch        *b_jets_mT;   //!
   TBranch        *b_jets_Flavour;   //!
   TBranch        *b_jets_HadronFlavour;   //!
   TBranch        *b_jets_genjetIndex;   //!
   TBranch        *b_jets_PUJetID;   //!
   TBranch        *b_jets_PUJetID_WP;   //!
   TBranch        *b_jets_PUJetIDupdated;   //!
   TBranch        *b_jets_PUJetIDupdated_WP;   //!
   TBranch        *b_jets_vtxPt;   //!
   TBranch        *b_jets_vtxMass;   //!
   TBranch        *b_jets_vtx3dL;   //!
   TBranch        *b_jets_vtxNtrk;   //!
   TBranch        *b_jets_vtx3deL;   //!
   TBranch        *b_jets_leadTrackPt;   //!
   TBranch        *b_jets_leptonPtRel;   //!
   TBranch        *b_jets_leptonPt;   //!
   TBranch        *b_jets_leptonDeltaR;   //!
   TBranch        *b_jets_chEmEF;   //!
   TBranch        *b_jets_chHEF;   //!
   TBranch        *b_jets_nEmEF;   //!
   TBranch        *b_jets_nHEF;   //!
   TBranch        *b_jets_MUF;   //!
   TBranch        *b_jets_neMult;   //!
   TBranch        *b_jets_chMult;   //!
   TBranch        *b_bDiscriminator;   //!
   TBranch        *b_bCSVscore;   //!
   TBranch        *b_pfCombinedMVAV2BJetTags;   //!
   TBranch        *b_bDeepCSV_probb;   //!
   TBranch        *b_bDeepCSV_probbb;   //!
   TBranch        *b_bDeepCSV_probudsg;   //!
   TBranch        *b_bDeepCSV_probc;   //!
   TBranch        *b_bDeepCSV_probcc;   //!
   TBranch        *b_bDeepFlavor_probb;   //!
   TBranch        *b_bDeepFlavor_probbb;   //!
   TBranch        *b_bDeepFlavor_problepb;   //!
   TBranch        *b_bDeepFlavor_probc;   //!
   TBranch        *b_bDeepFlavor_probuds;   //!
   TBranch        *b_bDeepFlavor_probg;   //!
   TBranch        *b_bParticleNetAK4JetTags_probbb;   //!
   TBranch        *b_bParticleNetAK4JetTags_probpu;   //!
   TBranch        *b_bParticleNetAK4JetTags_probcc;   //!
   TBranch        *b_bParticleNetAK4JetTags_probundef;   //!
   TBranch        *b_bParticleNetAK4JetTags_probc;   //!
   TBranch        *b_bParticleNetAK4JetTags_probb;   //!
   TBranch        *b_bParticleNetAK4JetTags_probuds;   //!
   TBranch        *b_bParticleNetAK4JetTags_probg;   //!
   TBranch        *b_jets_bjetRegCorr;   //!
   TBranch        *b_jets_bjetRegRes;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probmu;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probele;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaup1h0p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaup1h1p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaup1h2p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaup3h0p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaup3h1p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaum1h0p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaum1h1p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaum1h2p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaum3h0p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probtaum3h1p;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probb;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probc;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probuds;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_probg;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_ptcorr;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_ptreshigh;   //!
   TBranch        *b_bParticleNetTauAK4JetTags_ptreslow;   //!
   TBranch        *b_PFjetID;   //!
   TBranch        *b_jetRawf;   //!
   TBranch        *b_jets_JER;   //!
   TBranch        *b_susyModel;   //!
   TBranch        *b_ak8jets_px;   //!
   TBranch        *b_ak8jets_py;   //!
   TBranch        *b_ak8jets_pz;   //!
   TBranch        *b_ak8jets_e;   //!
   TBranch        *b_ak8jets_SoftDropMass;   //!
   TBranch        *b_ak8jets_PrunedMass;   //!
   TBranch        *b_ak8jets_TrimmedMass;   //!
   TBranch        *b_ak8jets_FilteredMass;   //!
   TBranch        *b_ak8jets_tau1;   //!
   TBranch        *b_ak8jets_tau2;   //!
   TBranch        *b_ak8jets_tau3;   //!
   TBranch        *b_ak8jets_tau4;   //!
   TBranch        *b_ak8jets_CSV;   //!
   TBranch        *b_ak8jets_deepCSV_probb;   //!
   TBranch        *b_ak8jets_deepCSV_probbb;   //!
   TBranch        *b_ak8jets_deepFlavor_probb;   //!
   TBranch        *b_ak8jets_deepFlavor_probbb;   //!
   TBranch        *b_ak8jets_deepFlavor_problepb;   //!
   TBranch        *b_ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb;   //!
   TBranch        *b_ak8jets_deepDoubleBvLJetTags_probHbb;   //!
   TBranch        *b_ak8jets_deepBoostedJetTags_probHbb;   //!
   TBranch        *b_ak8jets_particleNetJetTags_probHbb;   //!
   TBranch        *b_ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD;   //!
   TBranch        *b_ak8jets_nsubjets;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHtt;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHtm;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHte;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHbb;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHcc;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHqq;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probHgg;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probQCD2hf;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probQCD1hf;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_probQCD0hf;   //!
   TBranch        *b_bParticleNetTauAK8JetTags_masscorr;   //!
   TBranch        *b_subjets_px;   //!
   TBranch        *b_subjets_py;   //!
   TBranch        *b_subjets_pz;   //!
   TBranch        *b_subjets_e;   //!
   TBranch        *b_subjets_CSV;   //!
   TBranch        *b_subjets_deepCSV_probb;   //!
   TBranch        *b_subjets_deepCSV_probbb;   //!
   TBranch        *b_subjets_deepFlavor_probb;   //!
   TBranch        *b_subjets_deepFlavor_probbb;   //!
   TBranch        *b_subjets_deepFlavor_problepb;   //!
   TBranch        *b_subjets_ak8MotherIdx;   //!
   TBranch        *b_pvGen_x;   //!
   TBranch        *b_pvGen_y;   //!
   TBranch        *b_pvGen_z;   //!

   BigN(TTree *tree=0);
   virtual ~BigN();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef BigN_cxx
BigN::BigN(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/gwteras/cms/store/user/lichengz/NonResonantHHbbtautauNtuples/MC_2018_21Feb2023/2_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_MC_2018_21Feb2023_2/230221_234753/0001//HTauTauAnalysis_1-1000.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/gwteras/cms/store/user/lichengz/NonResonantHHbbtautauNtuples/MC_2018_21Feb2023/2_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_MC_2018_21Feb2023_2/230221_234753/0001//HTauTauAnalysis_1-1000.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/gwteras/cms/store/user/lichengz/NonResonantHHbbtautauNtuples/MC_2018_21Feb2023/2_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_MC_2018_21Feb2023_2/230221_234753/0001//HTauTauAnalysis_1-1000.root:/HTauTauTree");
      dir->GetObject("HTauTauTree",tree);

   }
   Init(tree);
}

BigN::~BigN()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t BigN::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t BigN::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void BigN::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   daughters_IetaIeta = 0;
   daughters_full5x5_IetaIeta = 0;
   daughters_hOverE = 0;
   daughters_deltaEtaSuperClusterTrackAtVtx = 0;
   daughters_deltaPhiSuperClusterTrackAtVtx = 0;
   daughters_IoEmIoP = 0;
   daughters_IoEmIoP_ttH = 0;
   mothers_px = 0;
   mothers_py = 0;
   mothers_pz = 0;
   mothers_e = 0;
   mothers_trgSeparateMatch = 0;
   daughters_px = 0;
   daughters_py = 0;
   daughters_pz = 0;
   daughters_e = 0;
   daughters_charge = 0;
   L1_tauEt = 0;
   L1_tauEta = 0;
   L1_tauPhi = 0;
   L1_tauIso = 0;
   L1_jetEt = 0;
   L1_jetEta = 0;
   L1_jetPhi = 0;
   daughters_highestEt_L1IsoTauMatched = 0;
   daughters_hasTES = 0;
   daughters_px_TauUp = 0;
   daughters_py_TauUp = 0;
   daughters_pz_TauUp = 0;
   daughters_e_TauUp = 0;
   daughters_px_TauDown = 0;
   daughters_py_TauDown = 0;
   daughters_pz_TauDown = 0;
   daughters_e_TauDown = 0;
   daughters_TESshiftDM0 = 0;
   daughters_TESshiftDM1 = 0;
   daughters_TESshiftDM10 = 0;
   daughters_TESshiftDM11 = 0;
   daughters_hasEES = 0;
   daughters_px_EleUp = 0;
   daughters_py_EleUp = 0;
   daughters_pz_EleUp = 0;
   daughters_e_EleUp = 0;
   daughters_px_EleDown = 0;
   daughters_py_EleDown = 0;
   daughters_pz_EleDown = 0;
   daughters_e_EleDown = 0;
   daughters_EESshiftDM0up = 0;
   daughters_EESshiftDM0dw = 0;
   daughters_EESshiftDM1up = 0;
   daughters_EESshiftDM1dw = 0;
   daughters_MESshiftup = 0;
   daughters_MESshiftdw = 0;
   daughters_isTauMatched = 0;
   daughters_genindex = 0;
   genpart_px = 0;
   genpart_py = 0;
   genpart_pz = 0;
   genpart_e = 0;
   genpart_pdg = 0;
   genpart_status = 0;
   genpart_HMothInd = 0;
   genpart_MSSMHMothInd = 0;
   genpart_TopMothInd = 0;
   genpart_TauMothInd = 0;
   genpart_ZMothInd = 0;
   genpart_WMothInd = 0;
   genpart_bMothInd = 0;
   genpart_HZDecayMode = 0;
   genpart_TopDecayMode = 0;
   genpart_WDecayMode = 0;
   genpart_TauGenDecayMode = 0;
   genpart_TauGenDetailedDecayMode = 0;
   genpart_flags = 0;
   genjet_px = 0;
   genjet_py = 0;
   genjet_pz = 0;
   genjet_e = 0;
   genjet_partonFlavour = 0;
   genjet_hadronFlavour = 0;
   SVfitMass = 0;
   SVfitMassUnc = 0;
   SVfitTransverseMass = 0;
   SVfitTransverseMassUnc = 0;
   SVfit_pt = 0;
   SVfit_ptUnc = 0;
   SVfit_eta = 0;
   SVfit_etaUnc = 0;
   SVfit_phi = 0;
   SVfit_phiUnc = 0;
   SVfit_fitMETRho = 0;
   SVfit_fitMETPhi = 0;
   isOSCand = 0;
   METx = 0;
   METy = 0;
   METx_UP_JES = 0;
   METy_UP_JES = 0;
   METx_DOWN_JES = 0;
   METy_DOWN_JES = 0;
   METx_UP_TES = 0;
   METy_UP_TES = 0;
   METx_DOWN_TES = 0;
   METy_DOWN_TES = 0;
   METx_UP_EES = 0;
   METy_UP_EES = 0;
   METx_DOWN_EES = 0;
   METy_DOWN_EES = 0;
   uncorrMETx = 0;
   uncorrMETy = 0;
   MET_cov00 = 0;
   MET_cov01 = 0;
   MET_cov10 = 0;
   MET_cov11 = 0;
   MET_significance = 0;
   mT_Dau1 = 0;
   mT_Dau2 = 0;
   PDGIdDaughters = 0;
   indexDau1 = 0;
   indexDau2 = 0;
   particleType = 0;
   daughters_muonID = 0;
   daughters_typeOfMuon = 0;
   dxy = 0;
   dz = 0;
   dxy_innerTrack = 0;
   dz_innerTrack = 0;
   daughters_rel_error_trackpt = 0;
   SIP = 0;
   daughters_iseleWPLoose = 0;
   daughters_iseleWP80 = 0;
   daughters_iseleWP90 = 0;
   daughters_iseleNoIsoWPLoose = 0;
   daughters_iseleNoIsoWP80 = 0;
   daughters_iseleNoIsoWP90 = 0;
   daughters_eleMVAnt = 0;
   daughters_eleMVA_HZZ = 0;
   daughters_iseleChargeConsistent = 0;
   daughters_ecalTrkEnergyPostCorr = 0;
   daughters_ecalTrkEnergyErrPostCorr = 0;
   daughters_energyScaleUp = 0;
   daughters_energyScaleDown = 0;
   daughters_energySigmaUp = 0;
   daughters_energySigmaDown = 0;
   decayMode = 0;
   genmatch = 0;
   tauID = 0;
   combreliso = 0;
   combreliso03 = 0;
   daughters_depositR03_tracker = 0;
   daughters_depositR03_ecal = 0;
   daughters_depositR03_hcal = 0;
   daughters_decayModeFindingOldDMs = 0;
   daughters_decayModeFindingNewDMs = 0;
   daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits = 0;
   daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017 = 0;
   daughters_byDeepTau2017v2p1VSjetraw = 0;
   daughters_byDeepTau2017v2p1VSeraw = 0;
   daughters_byDeepTau2017v2p1VSmuraw = 0;
   daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = 0;
   daughters_chargedIsoPtSum = 0;
   daughters_neutralIsoPtSum = 0;
   daughters_puCorrPtSum = 0;
   daughters_numChargedParticlesSignalCone = 0;
   daughters_numNeutralHadronsSignalCone = 0;
   daughters_numPhotonsSignalCone = 0;
   daughters_daughters_numParticlesSignalCone = 0;
   daughters_numChargedParticlesIsoCone = 0;
   daughters_numNeutralHadronsIsoCone = 0;
   daughters_numPhotonsIsoCone = 0;
   daughters_numParticlesIsoCone = 0;
   daughters_leadChargedParticlePt = 0;
   daughters_trackRefPt = 0;
   daughters_trgMatched = 0;
   daughters_FilterFired = 0;
   daughters_isGoodTriggerType = 0;
   daughters_L3FilterFired = 0;
   daughters_L3FilterFiredLast = 0;
   daughters_HLTpt = 0;
   daughters_jetNDauChargedMVASel = 0;
   daughters_miniRelIsoCharged = 0;
   daughters_miniRelIsoNeutral = 0;
   daughters_jetPtRel = 0;
   daughters_jetPtRatio = 0;
   daughters_jetBTagCSV = 0;
   daughters_jetBTagDeepCSV = 0;
   daughters_jetBTagDeepFlavor = 0;
   jets_VBFleadFilterMatch = 0;
   jets_VBFsubleadFilterMatch = 0;
   jets_px = 0;
   jets_py = 0;
   jets_pz = 0;
   jets_e = 0;
   jets_area = 0;
   jets_mT = 0;
   jets_Flavour = 0;
   jets_HadronFlavour = 0;
   jets_genjetIndex = 0;
   jets_PUJetID = 0;
   jets_PUJetID_WP = 0;
   jets_PUJetIDupdated = 0;
   jets_PUJetIDupdated_WP = 0;
   jets_vtxPt = 0;
   jets_vtxMass = 0;
   jets_vtx3dL = 0;
   jets_vtxNtrk = 0;
   jets_vtx3deL = 0;
   jets_leadTrackPt = 0;
   jets_leptonPtRel = 0;
   jets_leptonPt = 0;
   jets_leptonDeltaR = 0;
   jets_chEmEF = 0;
   jets_chHEF = 0;
   jets_nEmEF = 0;
   jets_nHEF = 0;
   jets_MUF = 0;
   jets_neMult = 0;
   jets_chMult = 0;
   bDiscriminator = 0;
   bCSVscore = 0;
   pfCombinedMVAV2BJetTags = 0;
   bDeepCSV_probb = 0;
   bDeepCSV_probbb = 0;
   bDeepCSV_probudsg = 0;
   bDeepCSV_probc = 0;
   bDeepCSV_probcc = 0;
   bDeepFlavor_probb = 0;
   bDeepFlavor_probbb = 0;
   bDeepFlavor_problepb = 0;
   bDeepFlavor_probc = 0;
   bDeepFlavor_probuds = 0;
   bDeepFlavor_probg = 0;
   bParticleNetAK4JetTags_probbb = 0;
   bParticleNetAK4JetTags_probpu = 0;
   bParticleNetAK4JetTags_probcc = 0;
   bParticleNetAK4JetTags_probundef = 0;
   bParticleNetAK4JetTags_probc = 0;
   bParticleNetAK4JetTags_probb = 0;
   bParticleNetAK4JetTags_probuds = 0;
   bParticleNetAK4JetTags_probg = 0;
   jets_bjetRegCorr = 0;
   jets_bjetRegRes = 0;
   bParticleNetTauAK4JetTags_probmu = 0;
   bParticleNetTauAK4JetTags_probele = 0;
   bParticleNetTauAK4JetTags_probtaup1h0p = 0;
   bParticleNetTauAK4JetTags_probtaup1h1p = 0;
   bParticleNetTauAK4JetTags_probtaup1h2p = 0;
   bParticleNetTauAK4JetTags_probtaup3h0p = 0;
   bParticleNetTauAK4JetTags_probtaup3h1p = 0;
   bParticleNetTauAK4JetTags_probtaum1h0p = 0;
   bParticleNetTauAK4JetTags_probtaum1h1p = 0;
   bParticleNetTauAK4JetTags_probtaum1h2p = 0;
   bParticleNetTauAK4JetTags_probtaum3h0p = 0;
   bParticleNetTauAK4JetTags_probtaum3h1p = 0;
   bParticleNetTauAK4JetTags_probb = 0;
   bParticleNetTauAK4JetTags_probc = 0;
   bParticleNetTauAK4JetTags_probuds = 0;
   bParticleNetTauAK4JetTags_probg = 0;
   bParticleNetTauAK4JetTags_ptcorr = 0;
   bParticleNetTauAK4JetTags_ptreshigh = 0;
   bParticleNetTauAK4JetTags_ptreslow = 0;
   PFjetID = 0;
   jetRawf = 0;
   jets_JER = 0;
   susyModel = 0;
   ak8jets_px = 0;
   ak8jets_py = 0;
   ak8jets_pz = 0;
   ak8jets_e = 0;
   ak8jets_SoftDropMass = 0;
   ak8jets_PrunedMass = 0;
   ak8jets_TrimmedMass = 0;
   ak8jets_FilteredMass = 0;
   ak8jets_tau1 = 0;
   ak8jets_tau2 = 0;
   ak8jets_tau3 = 0;
   ak8jets_tau4 = 0;
   ak8jets_CSV = 0;
   ak8jets_deepCSV_probb = 0;
   ak8jets_deepCSV_probbb = 0;
   ak8jets_deepFlavor_probb = 0;
   ak8jets_deepFlavor_probbb = 0;
   ak8jets_deepFlavor_problepb = 0;
   ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb = 0;
   ak8jets_deepDoubleBvLJetTags_probHbb = 0;
   ak8jets_deepBoostedJetTags_probHbb = 0;
   ak8jets_particleNetJetTags_probHbb = 0;
   ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD = 0;
   ak8jets_nsubjets = 0;
   bParticleNetTauAK8JetTags_probHtt = 0;
   bParticleNetTauAK8JetTags_probHtm = 0;
   bParticleNetTauAK8JetTags_probHte = 0;
   bParticleNetTauAK8JetTags_probHbb = 0;
   bParticleNetTauAK8JetTags_probHcc = 0;
   bParticleNetTauAK8JetTags_probHqq = 0;
   bParticleNetTauAK8JetTags_probHgg = 0;
   bParticleNetTauAK8JetTags_probQCD2hf = 0;
   bParticleNetTauAK8JetTags_probQCD1hf = 0;
   bParticleNetTauAK8JetTags_probQCD0hf = 0;
   bParticleNetTauAK8JetTags_masscorr = 0;
   subjets_px = 0;
   subjets_py = 0;
   subjets_pz = 0;
   subjets_e = 0;
   subjets_CSV = 0;
   subjets_deepCSV_probb = 0;
   subjets_deepCSV_probbb = 0;
   subjets_deepFlavor_probb = 0;
   subjets_deepFlavor_probbb = 0;
   subjets_deepFlavor_problepb = 0;
   subjets_ak8MotherIdx = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("EventNumber", &EventNumber, &b_EventNumber);
   fChain->SetBranchAddress("RunNumber", &RunNumber, &b_RunNumber);
   fChain->SetBranchAddress("lumi", &lumi, &b_lumi);
   fChain->SetBranchAddress("year", &year, &b_year);
   fChain->SetBranchAddress("prefiringweight", &prefiringweight, &b_prefiringweight);
   fChain->SetBranchAddress("prefiringweightup", &prefiringweightup, &b_prefiringweightup);
   fChain->SetBranchAddress("prefiringweightdown", &prefiringweightdown, &b_prefiringweightdown);
   fChain->SetBranchAddress("triggerbit", &triggerbit, &b_triggerbit);
   fChain->SetBranchAddress("metfilterbit", &metfilterbit, &b_metfilterbit);
   fChain->SetBranchAddress("met", &met, &b_met);
   fChain->SetBranchAddress("met_er", &met_er, &b_met_er);
   fChain->SetBranchAddress("met_er_phi", &met_er_phi, &b_met_er_phi);
   fChain->SetBranchAddress("metphi", &metphi, &b_metphi);
   fChain->SetBranchAddress("daughters_IetaIeta", &daughters_IetaIeta, &b_daughters_IetaIeta);
   fChain->SetBranchAddress("daughters_full5x5_IetaIeta", &daughters_full5x5_IetaIeta, &b_daughters_full5x5_IetaIeta);
   fChain->SetBranchAddress("daughters_hOverE", &daughters_hOverE, &b_daughters_hOverE);
   fChain->SetBranchAddress("daughters_deltaEtaSuperClusterTrackAtVtx", &daughters_deltaEtaSuperClusterTrackAtVtx, &b_daughters_deltaEtaSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("daughters_deltaPhiSuperClusterTrackAtVtx", &daughters_deltaPhiSuperClusterTrackAtVtx, &b_daughters_deltaPhiSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("daughters_IoEmIoP", &daughters_IoEmIoP, &b_daughters_IoEmIoP);
   fChain->SetBranchAddress("daughters_IoEmIoP_ttH", &daughters_IoEmIoP_ttH, &b_daughters_IoEmIoP_ttH);
   fChain->SetBranchAddress("PFMETCov00", &PFMETCov00, &b_PFMETCov00);
   fChain->SetBranchAddress("PFMETCov01", &PFMETCov01, &b_PFMETCov01);
   fChain->SetBranchAddress("PFMETCov10", &PFMETCov10, &b_PFMETCov10);
   fChain->SetBranchAddress("PFMETCov11", &PFMETCov11, &b_PFMETCov11);
   fChain->SetBranchAddress("PFMETsignif", &PFMETsignif, &b_PFMETsignif);
   fChain->SetBranchAddress("PUPPImet", &PUPPImet, &b_PUPPImet);
   fChain->SetBranchAddress("PUPPImetphi", &PUPPImetphi, &b_PUPPImetphi);
   fChain->SetBranchAddress("PUPPImetShifted", &PUPPImetShifted, &b_PUPPImetShifted);
   fChain->SetBranchAddress("PUPPImetShiftedphi", &PUPPImetShiftedphi, &b_PUPPImetShiftedphi);
   fChain->SetBranchAddress("PuppiMETCov00", &PuppiMETCov00, &b_PuppiMETCov00);
   fChain->SetBranchAddress("PuppiMETCov01", &PuppiMETCov01, &b_PuppiMETCov01);
   fChain->SetBranchAddress("PuppiMETCov10", &PuppiMETCov10, &b_PuppiMETCov10);
   fChain->SetBranchAddress("PuppiMETCov11", &PuppiMETCov11, &b_PuppiMETCov11);
   fChain->SetBranchAddress("PuppiMETsignif", &PuppiMETsignif, &b_PuppiMETsignif);
   fChain->SetBranchAddress("DeepMETresponseTune_pt", &DeepMETresponseTune_pt, &b_DeepMETresponseTune_pt);
   fChain->SetBranchAddress("DeepMETresponseTune_phi", &DeepMETresponseTune_phi, &b_DeepMETresponseTune_phi);
   fChain->SetBranchAddress("DeepMETresolutionTune_pt", &DeepMETresolutionTune_pt, &b_DeepMETresolutionTune_pt);
   fChain->SetBranchAddress("DeepMETresolutionTune_phi", &DeepMETresolutionTune_phi, &b_DeepMETresolutionTune_phi);
   fChain->SetBranchAddress("ShiftedDeepMETresponseTune_pt", &ShiftedDeepMETresponseTune_pt, &b_ShiftedDeepMETresponseTune_pt);
   fChain->SetBranchAddress("ShiftedDeepMETresponseTune_phi", &ShiftedDeepMETresponseTune_phi, &b_ShiftedDeepMETresponseTune_phi);
   fChain->SetBranchAddress("ShiftedDeepMETresolutionTune_pt", &ShiftedDeepMETresolutionTune_pt, &b_ShiftedDeepMETresolutionTune_pt);
   fChain->SetBranchAddress("ShiftedDeepMETresolutionTune_phi", &ShiftedDeepMETresolutionTune_phi, &b_ShiftedDeepMETresolutionTune_phi);
   fChain->SetBranchAddress("npv", &npv, &b_npv);
   fChain->SetBranchAddress("npu", &npu, &b_npu);
   fChain->SetBranchAddress("rho", &rho, &b_rho);
   fChain->SetBranchAddress("mothers_px", &mothers_px, &b_mothers_px);
   fChain->SetBranchAddress("mothers_py", &mothers_py, &b_mothers_py);
   fChain->SetBranchAddress("mothers_pz", &mothers_pz, &b_mothers_pz);
   fChain->SetBranchAddress("mothers_e", &mothers_e, &b_mothers_e);
   fChain->SetBranchAddress("mothers_trgSeparateMatch", &mothers_trgSeparateMatch, &b_mothers_trgSeparateMatch);
   fChain->SetBranchAddress("daughters_px", &daughters_px, &b_daughters_px);
   fChain->SetBranchAddress("daughters_py", &daughters_py, &b_daughters_py);
   fChain->SetBranchAddress("daughters_pz", &daughters_pz, &b_daughters_pz);
   fChain->SetBranchAddress("daughters_e", &daughters_e, &b_daughters_e);
   fChain->SetBranchAddress("daughters_charge", &daughters_charge, &b_daughters_charge);
   fChain->SetBranchAddress("L1_tauEt", &L1_tauEt, &b_L1_tauEt);
   fChain->SetBranchAddress("L1_tauEta", &L1_tauEta, &b_L1_tauEta);
   fChain->SetBranchAddress("L1_tauPhi", &L1_tauPhi, &b_L1_tauPhi);
   fChain->SetBranchAddress("L1_tauIso", &L1_tauIso, &b_L1_tauIso);
   fChain->SetBranchAddress("L1_jetEt", &L1_jetEt, &b_L1_jetEt);
   fChain->SetBranchAddress("L1_jetEta", &L1_jetEta, &b_L1_jetEta);
   fChain->SetBranchAddress("L1_jetPhi", &L1_jetPhi, &b_L1_jetPhi);
   fChain->SetBranchAddress("daughters_highestEt_L1IsoTauMatched", &daughters_highestEt_L1IsoTauMatched, &b_daughters_highestEt_L1IsoTauMatched);
   fChain->SetBranchAddress("daughters_hasTES", &daughters_hasTES, &b_daughters_hasTES);
   fChain->SetBranchAddress("daughters_px_TauUp", &daughters_px_TauUp, &b_daughters_px_TauUp);
   fChain->SetBranchAddress("daughters_py_TauUp", &daughters_py_TauUp, &b_daughters_py_TauUp);
   fChain->SetBranchAddress("daughters_pz_TauUp", &daughters_pz_TauUp, &b_daughters_pz_TauUp);
   fChain->SetBranchAddress("daughters_e_TauUp", &daughters_e_TauUp, &b_daughters_e_TauUp);
   fChain->SetBranchAddress("daughters_px_TauDown", &daughters_px_TauDown, &b_daughters_px_TauDown);
   fChain->SetBranchAddress("daughters_py_TauDown", &daughters_py_TauDown, &b_daughters_py_TauDown);
   fChain->SetBranchAddress("daughters_pz_TauDown", &daughters_pz_TauDown, &b_daughters_pz_TauDown);
   fChain->SetBranchAddress("daughters_e_TauDown", &daughters_e_TauDown, &b_daughters_e_TauDown);
   fChain->SetBranchAddress("daughters_TESshiftDM0", &daughters_TESshiftDM0, &b_daughters_TESshiftDM0);
   fChain->SetBranchAddress("daughters_TESshiftDM1", &daughters_TESshiftDM1, &b_daughters_TESshiftDM1);
   fChain->SetBranchAddress("daughters_TESshiftDM10", &daughters_TESshiftDM10, &b_daughters_TESshiftDM10);
   fChain->SetBranchAddress("daughters_TESshiftDM11", &daughters_TESshiftDM11, &b_daughters_TESshiftDM11);
   fChain->SetBranchAddress("daughters_hasEES", &daughters_hasEES, &b_daughters_hasEES);
   fChain->SetBranchAddress("daughters_px_EleUp", &daughters_px_EleUp, &b_daughters_px_EleUp);
   fChain->SetBranchAddress("daughters_py_EleUp", &daughters_py_EleUp, &b_daughters_py_EleUp);
   fChain->SetBranchAddress("daughters_pz_EleUp", &daughters_pz_EleUp, &b_daughters_pz_EleUp);
   fChain->SetBranchAddress("daughters_e_EleUp", &daughters_e_EleUp, &b_daughters_e_EleUp);
   fChain->SetBranchAddress("daughters_px_EleDown", &daughters_px_EleDown, &b_daughters_px_EleDown);
   fChain->SetBranchAddress("daughters_py_EleDown", &daughters_py_EleDown, &b_daughters_py_EleDown);
   fChain->SetBranchAddress("daughters_pz_EleDown", &daughters_pz_EleDown, &b_daughters_pz_EleDown);
   fChain->SetBranchAddress("daughters_e_EleDown", &daughters_e_EleDown, &b_daughters_e_EleDown);
   fChain->SetBranchAddress("daughters_EESshiftDM0up", &daughters_EESshiftDM0up, &b_daughters_EESshiftDM0up);
   fChain->SetBranchAddress("daughters_EESshiftDM0dw", &daughters_EESshiftDM0dw, &b_daughters_EESshiftDM0dw);
   fChain->SetBranchAddress("daughters_EESshiftDM1up", &daughters_EESshiftDM1up, &b_daughters_EESshiftDM1up);
   fChain->SetBranchAddress("daughters_EESshiftDM1dw", &daughters_EESshiftDM1dw, &b_daughters_EESshiftDM1dw);
   fChain->SetBranchAddress("daughters_MESshiftup", &daughters_MESshiftup, &b_daughters_MESshiftup);
   fChain->SetBranchAddress("daughters_MESshiftdw", &daughters_MESshiftdw, &b_daughters_MESshiftdw);
   fChain->SetBranchAddress("daughters_isTauMatched", &daughters_isTauMatched, &b_daughters_isTauMatched);
   fChain->SetBranchAddress("PUNumInteractions", &PUNumInteractions, &b_PUNumInteractions);
   fChain->SetBranchAddress("daughters_genindex", &daughters_genindex, &b_daughters_genindex);
   fChain->SetBranchAddress("MC_weight", &MC_weight, &b_MC_weight);
   fChain->SetBranchAddress("MC_weight_scale_muF0p5", &MC_weight_scale_muF0p5, &b_MC_weight_scale_muF0p5);
   fChain->SetBranchAddress("MC_weight_scale_muF2", &MC_weight_scale_muF2, &b_MC_weight_scale_muF2);
   fChain->SetBranchAddress("MC_weight_scale_muR0p5", &MC_weight_scale_muR0p5, &b_MC_weight_scale_muR0p5);
   fChain->SetBranchAddress("MC_weight_scale_muR2", &MC_weight_scale_muR2, &b_MC_weight_scale_muR2);
   fChain->SetBranchAddress("MC_weight_PSWeight0", &MC_weight_PSWeight0, &b_MC_weight_PSWeight0);
   fChain->SetBranchAddress("MC_weight_PSWeight1", &MC_weight_PSWeight1, &b_MC_weight_PSWeight1);
   fChain->SetBranchAddress("MC_weight_PSWeight2", &MC_weight_PSWeight2, &b_MC_weight_PSWeight2);
   fChain->SetBranchAddress("MC_weight_PSWeight3", &MC_weight_PSWeight3, &b_MC_weight_PSWeight3);
   fChain->SetBranchAddress("lheHt", &lheHt, &b_lheHt);
   fChain->SetBranchAddress("lheNOutPartons", &lheNOutPartons, &b_lheNOutPartons);
   fChain->SetBranchAddress("lheNOutB", &lheNOutB, &b_lheNOutB);
   fChain->SetBranchAddress("lheNOutC", &lheNOutC, &b_lheNOutC);
   fChain->SetBranchAddress("lheVPt", &lheVPt, &b_lheVPt);
   fChain->SetBranchAddress("aMCatNLOweight", &aMCatNLOweight, &b_aMCatNLOweight);
   fChain->SetBranchAddress("genpart_px", &genpart_px, &b_genpart_px);
   fChain->SetBranchAddress("genpart_py", &genpart_py, &b_genpart_py);
   fChain->SetBranchAddress("genpart_pz", &genpart_pz, &b_genpart_pz);
   fChain->SetBranchAddress("genpart_e", &genpart_e, &b_genpart_e);
   fChain->SetBranchAddress("genpart_pdg", &genpart_pdg, &b_genpart_pdg);
   fChain->SetBranchAddress("genpart_status", &genpart_status, &b_genpart_status);
   fChain->SetBranchAddress("genpart_HMothInd", &genpart_HMothInd, &b_genpart_HMothInd);
   fChain->SetBranchAddress("genpart_MSSMHMothInd", &genpart_MSSMHMothInd, &b_genpart_MSSMHMothInd);
   fChain->SetBranchAddress("genpart_TopMothInd", &genpart_TopMothInd, &b_genpart_TopMothInd);
   fChain->SetBranchAddress("genpart_TauMothInd", &genpart_TauMothInd, &b_genpart_TauMothInd);
   fChain->SetBranchAddress("genpart_ZMothInd", &genpart_ZMothInd, &b_genpart_ZMothInd);
   fChain->SetBranchAddress("genpart_WMothInd", &genpart_WMothInd, &b_genpart_WMothInd);
   fChain->SetBranchAddress("genpart_bMothInd", &genpart_bMothInd, &b_genpart_bMothInd);
   fChain->SetBranchAddress("genpart_HZDecayMode", &genpart_HZDecayMode, &b_genpart_HZDecayMode);
   fChain->SetBranchAddress("genpart_TopDecayMode", &genpart_TopDecayMode, &b_genpart_TopDecayMode);
   fChain->SetBranchAddress("genpart_WDecayMode", &genpart_WDecayMode, &b_genpart_WDecayMode);
   fChain->SetBranchAddress("genpart_TauGenDecayMode", &genpart_TauGenDecayMode, &b_genpart_TauGenDecayMode);
   fChain->SetBranchAddress("genpart_TauGenDetailedDecayMode", &genpart_TauGenDetailedDecayMode, &b_genpart_TauGenDetailedDecayMode);
   fChain->SetBranchAddress("genpart_flags", &genpart_flags, &b_genpart_flags);
   fChain->SetBranchAddress("genjet_px", &genjet_px, &b_genjet_px);
   fChain->SetBranchAddress("genjet_py", &genjet_py, &b_genjet_py);
   fChain->SetBranchAddress("genjet_pz", &genjet_pz, &b_genjet_pz);
   fChain->SetBranchAddress("genjet_e", &genjet_e, &b_genjet_e);
   fChain->SetBranchAddress("genjet_partonFlavour", &genjet_partonFlavour, &b_genjet_partonFlavour);
   fChain->SetBranchAddress("genjet_hadronFlavour", &genjet_hadronFlavour, &b_genjet_hadronFlavour);
   fChain->SetBranchAddress("NUP", &NUP, &b_NUP);
   fChain->SetBranchAddress("SVfitMass", &SVfitMass, &b_SVfitMass);
   fChain->SetBranchAddress("SVfitMassUnc", &SVfitMassUnc, &b_SVfitMassUnc);
   fChain->SetBranchAddress("SVfitTransverseMass", &SVfitTransverseMass, &b_SVfitTransverseMass);
   fChain->SetBranchAddress("SVfitTransverseMassUnc", &SVfitTransverseMassUnc, &b_SVfitTransverseMassUnc);
   fChain->SetBranchAddress("SVfit_pt", &SVfit_pt, &b_SVfit_pt);
   fChain->SetBranchAddress("SVfit_ptUnc", &SVfit_ptUnc, &b_SVfit_ptUnc);
   fChain->SetBranchAddress("SVfit_eta", &SVfit_eta, &b_SVfit_eta);
   fChain->SetBranchAddress("SVfit_etaUnc", &SVfit_etaUnc, &b_SVfit_etaUnc);
   fChain->SetBranchAddress("SVfit_phi", &SVfit_phi, &b_SVfit_phi);
   fChain->SetBranchAddress("SVfit_phiUnc", &SVfit_phiUnc, &b_SVfit_phiUnc);
   fChain->SetBranchAddress("SVfit_fitMETRho", &SVfit_fitMETRho, &b_SVfit_fitMETRho);
   fChain->SetBranchAddress("SVfit_fitMETPhi", &SVfit_fitMETPhi, &b_SVfit_fitMETPhi);
   fChain->SetBranchAddress("isOSCand", &isOSCand, &b_isOSCand);
   fChain->SetBranchAddress("PUPPImetShiftedX", &PUPPImetShiftedX, &b_PUPPImetShiftedX);
   fChain->SetBranchAddress("PUPPImetShiftedY", &PUPPImetShiftedY, &b_PUPPImetShiftedY);
   fChain->SetBranchAddress("METx", &METx, &b_METx);
   fChain->SetBranchAddress("METy", &METy, &b_METy);
   fChain->SetBranchAddress("METx_UP_JES", &METx_UP_JES, &b_METx_UP_JES);
   fChain->SetBranchAddress("METy_UP_JES", &METy_UP_JES, &b_METy_UP_JES);
   fChain->SetBranchAddress("METx_DOWN_JES", &METx_DOWN_JES, &b_METx_DOWN_JES);
   fChain->SetBranchAddress("METy_DOWN_JES", &METy_DOWN_JES, &b_METy_DOWN_JES);
   fChain->SetBranchAddress("METx_UP_TES", &METx_UP_TES, &b_METx_UP_TES);
   fChain->SetBranchAddress("METy_UP_TES", &METy_UP_TES, &b_METy_UP_TES);
   fChain->SetBranchAddress("METx_DOWN_TES", &METx_DOWN_TES, &b_METx_DOWN_TES);
   fChain->SetBranchAddress("METy_DOWN_TES", &METy_DOWN_TES, &b_METy_DOWN_TES);
   fChain->SetBranchAddress("METx_UP_EES", &METx_UP_EES, &b_METx_UP_EES);
   fChain->SetBranchAddress("METy_UP_EES", &METy_UP_EES, &b_METy_UP_EES);
   fChain->SetBranchAddress("METx_DOWN_EES", &METx_DOWN_EES, &b_METx_DOWN_EES);
   fChain->SetBranchAddress("METy_DOWN_EES", &METy_DOWN_EES, &b_METy_DOWN_EES);
   fChain->SetBranchAddress("uncorrMETx", &uncorrMETx, &b_uncorrMETx);
   fChain->SetBranchAddress("uncorrMETy", &uncorrMETy, &b_uncorrMETy);
   fChain->SetBranchAddress("MET_cov00", &MET_cov00, &b_MET_cov00);
   fChain->SetBranchAddress("MET_cov01", &MET_cov01, &b_MET_cov01);
   fChain->SetBranchAddress("MET_cov10", &MET_cov10, &b_MET_cov10);
   fChain->SetBranchAddress("MET_cov11", &MET_cov11, &b_MET_cov11);
   fChain->SetBranchAddress("MET_significance", &MET_significance, &b_MET_significance);
   fChain->SetBranchAddress("mT_Dau1", &mT_Dau1, &b_mT_Dau1);
   fChain->SetBranchAddress("mT_Dau2", &mT_Dau2, &b_mT_Dau2);
   fChain->SetBranchAddress("PDGIdDaughters", &PDGIdDaughters, &b_PDGIdDaughters);
   fChain->SetBranchAddress("indexDau1", &indexDau1, &b_indexDau1);
   fChain->SetBranchAddress("indexDau2", &indexDau2, &b_indexDau2);
   fChain->SetBranchAddress("particleType", &particleType, &b_particleType);
   fChain->SetBranchAddress("daughters_muonID", &daughters_muonID, &b_daughters_muonID);
   fChain->SetBranchAddress("daughters_typeOfMuon", &daughters_typeOfMuon, &b_daughters_typeOfMuon);
   fChain->SetBranchAddress("dxy", &dxy, &b_dxy);
   fChain->SetBranchAddress("dz", &dz, &b_dz);
   fChain->SetBranchAddress("dxy_innerTrack", &dxy_innerTrack, &b_dxy_innerTrack);
   fChain->SetBranchAddress("dz_innerTrack", &dz_innerTrack, &b_dz_innerTrack);
   fChain->SetBranchAddress("daughters_rel_error_trackpt", &daughters_rel_error_trackpt, &b_daughters_rel_error_trackpt);
   fChain->SetBranchAddress("SIP", &SIP, &b_SIP);
   fChain->SetBranchAddress("daughters_iseleWPLoose", &daughters_iseleWPLoose, &b_daughters_iseleWPLoose);
   fChain->SetBranchAddress("daughters_iseleWP80", &daughters_iseleWP80, &b_daughters_iseleWP80);
   fChain->SetBranchAddress("daughters_iseleWP90", &daughters_iseleWP90, &b_daughters_iseleWP90);
   fChain->SetBranchAddress("daughters_iseleNoIsoWPLoose", &daughters_iseleNoIsoWPLoose, &b_daughters_iseleNoIsoWPLoose);
   fChain->SetBranchAddress("daughters_iseleNoIsoWP80", &daughters_iseleNoIsoWP80, &b_daughters_iseleNoIsoWP80);
   fChain->SetBranchAddress("daughters_iseleNoIsoWP90", &daughters_iseleNoIsoWP90, &b_daughters_iseleNoIsoWP90);
   fChain->SetBranchAddress("daughters_eleMVAnt", &daughters_eleMVAnt, &b_daughters_eleMVAnt);
   fChain->SetBranchAddress("daughters_eleMVA_HZZ", &daughters_eleMVA_HZZ, &b_daughters_eleMVA_HZZ);
   fChain->SetBranchAddress("daughters_iseleChargeConsistent", &daughters_iseleChargeConsistent, &b_daughters_iseleChargeConsistent);
   fChain->SetBranchAddress("daughters_ecalTrkEnergyPostCorr", &daughters_ecalTrkEnergyPostCorr, &b_daughters_ecalTrkEnergyPostCorr);
   fChain->SetBranchAddress("daughters_ecalTrkEnergyErrPostCorr", &daughters_ecalTrkEnergyErrPostCorr, &b_daughters_ecalTrkEnergyErrPostCorr);
   fChain->SetBranchAddress("daughters_energyScaleUp", &daughters_energyScaleUp, &b_daughters_energyScaleUp);
   fChain->SetBranchAddress("daughters_energyScaleDown", &daughters_energyScaleDown, &b_daughters_energyScaleDown);
   fChain->SetBranchAddress("daughters_energySigmaUp", &daughters_energySigmaUp, &b_daughters_energySigmaUp);
   fChain->SetBranchAddress("daughters_energySigmaDown", &daughters_energySigmaDown, &b_daughters_energySigmaDown);
   fChain->SetBranchAddress("decayMode", &decayMode, &b_decayMode);
   fChain->SetBranchAddress("genmatch", &genmatch, &b_genmatch);
   fChain->SetBranchAddress("tauID", &tauID, &b_tauID);
   fChain->SetBranchAddress("combreliso", &combreliso, &b_combreliso);
   fChain->SetBranchAddress("combreliso03", &combreliso03, &b_combreliso03);
   fChain->SetBranchAddress("daughters_depositR03_tracker", &daughters_depositR03_tracker, &b_daughters_depositR03_tracker);
   fChain->SetBranchAddress("daughters_depositR03_ecal", &daughters_depositR03_ecal, &b_daughters_depositR03_ecal);
   fChain->SetBranchAddress("daughters_depositR03_hcal", &daughters_depositR03_hcal, &b_daughters_depositR03_hcal);
   fChain->SetBranchAddress("daughters_decayModeFindingOldDMs", &daughters_decayModeFindingOldDMs, &b_daughters_decayModeFindingOldDMs);
   fChain->SetBranchAddress("daughters_decayModeFindingNewDMs", &daughters_decayModeFindingNewDMs, &b_daughters_decayModeFindingNewDMs);
   fChain->SetBranchAddress("daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits", &daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits, &b_daughters_byCombinedIsolationDeltaBetaCorrRaw3Hits);
   fChain->SetBranchAddress("daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017", &daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017, &b_daughters_byIsolationMVArun2017v2DBoldDMwLTraw2017);
   fChain->SetBranchAddress("daughters_byDeepTau2017v2p1VSjetraw", &daughters_byDeepTau2017v2p1VSjetraw, &b_daughters_byDeepTau2017v2p1VSjetraw);
   fChain->SetBranchAddress("daughters_byDeepTau2017v2p1VSeraw", &daughters_byDeepTau2017v2p1VSeraw, &b_daughters_byDeepTau2017v2p1VSeraw);
   fChain->SetBranchAddress("daughters_byDeepTau2017v2p1VSmuraw", &daughters_byDeepTau2017v2p1VSmuraw, &b_daughters_byDeepTau2017v2p1VSmuraw);
   fChain->SetBranchAddress("daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017", &daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017, &b_daughters_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017);
   fChain->SetBranchAddress("daughters_chargedIsoPtSum", &daughters_chargedIsoPtSum, &b_daughters_chargedIsoPtSum);
   fChain->SetBranchAddress("daughters_neutralIsoPtSum", &daughters_neutralIsoPtSum, &b_daughters_neutralIsoPtSum);
   fChain->SetBranchAddress("daughters_puCorrPtSum", &daughters_puCorrPtSum, &b_daughters_puCorrPtSum);
   fChain->SetBranchAddress("daughters_numChargedParticlesSignalCone", &daughters_numChargedParticlesSignalCone, &b_daughters_numChargedParticlesSignalCone);
   fChain->SetBranchAddress("daughters_numNeutralHadronsSignalCone", &daughters_numNeutralHadronsSignalCone, &b_daughters_numNeutralHadronsSignalCone);
   fChain->SetBranchAddress("daughters_numPhotonsSignalCone", &daughters_numPhotonsSignalCone, &b_daughters_numPhotonsSignalCone);
   fChain->SetBranchAddress("daughters_daughters_numParticlesSignalCone", &daughters_daughters_numParticlesSignalCone, &b_daughters_daughters_numParticlesSignalCone);
   fChain->SetBranchAddress("daughters_numChargedParticlesIsoCone", &daughters_numChargedParticlesIsoCone, &b_daughters_numChargedParticlesIsoCone);
   fChain->SetBranchAddress("daughters_numNeutralHadronsIsoCone", &daughters_numNeutralHadronsIsoCone, &b_daughters_numNeutralHadronsIsoCone);
   fChain->SetBranchAddress("daughters_numPhotonsIsoCone", &daughters_numPhotonsIsoCone, &b_daughters_numPhotonsIsoCone);
   fChain->SetBranchAddress("daughters_numParticlesIsoCone", &daughters_numParticlesIsoCone, &b_daughters_numParticlesIsoCone);
   fChain->SetBranchAddress("daughters_leadChargedParticlePt", &daughters_leadChargedParticlePt, &b_daughters_leadChargedParticlePt);
   fChain->SetBranchAddress("daughters_trackRefPt", &daughters_trackRefPt, &b_daughters_trackRefPt);
   fChain->SetBranchAddress("daughters_trgMatched", &daughters_trgMatched, &b_daughters_trgMatched);
   fChain->SetBranchAddress("daughters_FilterFired", &daughters_FilterFired, &b_daughters_FilterFired);
   fChain->SetBranchAddress("daughters_isGoodTriggerType", &daughters_isGoodTriggerType, &b_daughters_isGoodTriggerType);
   fChain->SetBranchAddress("daughters_L3FilterFired", &daughters_L3FilterFired, &b_daughters_L3FilterFired);
   fChain->SetBranchAddress("daughters_L3FilterFiredLast", &daughters_L3FilterFiredLast, &b_daughters_L3FilterFiredLast);
   fChain->SetBranchAddress("daughters_HLTpt", &daughters_HLTpt, &b_daughters_HLTpt);
   fChain->SetBranchAddress("daughters_jetNDauChargedMVASel", &daughters_jetNDauChargedMVASel, &b_daughters_jetNDauChargedMVASel);
   fChain->SetBranchAddress("daughters_miniRelIsoCharged", &daughters_miniRelIsoCharged, &b_daughters_miniRelIsoCharged);
   fChain->SetBranchAddress("daughters_miniRelIsoNeutral", &daughters_miniRelIsoNeutral, &b_daughters_miniRelIsoNeutral);
   fChain->SetBranchAddress("daughters_jetPtRel", &daughters_jetPtRel, &b_daughters_jetPtRel);
   fChain->SetBranchAddress("daughters_jetPtRatio", &daughters_jetPtRatio, &b_daughters_jetPtRatio);
   fChain->SetBranchAddress("daughters_jetBTagCSV", &daughters_jetBTagCSV, &b_daughters_jetBTagCSV);
   fChain->SetBranchAddress("daughters_jetBTagDeepCSV", &daughters_jetBTagDeepCSV, &b_daughters_jetBTagDeepCSV);
   fChain->SetBranchAddress("daughters_jetBTagDeepFlavor", &daughters_jetBTagDeepFlavor, &b_daughters_jetBTagDeepFlavor);
   fChain->SetBranchAddress("JetsNumber", &JetsNumber, &b_JetsNumber);
   fChain->SetBranchAddress("jets_VBFleadFilterMatch", &jets_VBFleadFilterMatch, &b_jets_VBFleadFilterMatch);
   fChain->SetBranchAddress("jets_VBFsubleadFilterMatch", &jets_VBFsubleadFilterMatch, &b_jets_VBFsubleadFilterMatch);
   fChain->SetBranchAddress("jets_px", &jets_px, &b_jets_px);
   fChain->SetBranchAddress("jets_py", &jets_py, &b_jets_py);
   fChain->SetBranchAddress("jets_pz", &jets_pz, &b_jets_pz);
   fChain->SetBranchAddress("jets_e", &jets_e, &b_jets_e);
   fChain->SetBranchAddress("jets_area", &jets_area, &b_jets_area);
   fChain->SetBranchAddress("jets_mT", &jets_mT, &b_jets_mT);
   fChain->SetBranchAddress("jets_Flavour", &jets_Flavour, &b_jets_Flavour);
   fChain->SetBranchAddress("jets_HadronFlavour", &jets_HadronFlavour, &b_jets_HadronFlavour);
   fChain->SetBranchAddress("jets_genjetIndex", &jets_genjetIndex, &b_jets_genjetIndex);
   fChain->SetBranchAddress("jets_PUJetID", &jets_PUJetID, &b_jets_PUJetID);
   fChain->SetBranchAddress("jets_PUJetID_WP", &jets_PUJetID_WP, &b_jets_PUJetID_WP);
   fChain->SetBranchAddress("jets_PUJetIDupdated", &jets_PUJetIDupdated, &b_jets_PUJetIDupdated);
   fChain->SetBranchAddress("jets_PUJetIDupdated_WP", &jets_PUJetIDupdated_WP, &b_jets_PUJetIDupdated_WP);
   fChain->SetBranchAddress("jets_vtxPt", &jets_vtxPt, &b_jets_vtxPt);
   fChain->SetBranchAddress("jets_vtxMass", &jets_vtxMass, &b_jets_vtxMass);
   fChain->SetBranchAddress("jets_vtx3dL", &jets_vtx3dL, &b_jets_vtx3dL);
   fChain->SetBranchAddress("jets_vtxNtrk", &jets_vtxNtrk, &b_jets_vtxNtrk);
   fChain->SetBranchAddress("jets_vtx3deL", &jets_vtx3deL, &b_jets_vtx3deL);
   fChain->SetBranchAddress("jets_leadTrackPt", &jets_leadTrackPt, &b_jets_leadTrackPt);
   fChain->SetBranchAddress("jets_leptonPtRel", &jets_leptonPtRel, &b_jets_leptonPtRel);
   fChain->SetBranchAddress("jets_leptonPt", &jets_leptonPt, &b_jets_leptonPt);
   fChain->SetBranchAddress("jets_leptonDeltaR", &jets_leptonDeltaR, &b_jets_leptonDeltaR);
   fChain->SetBranchAddress("jets_chEmEF", &jets_chEmEF, &b_jets_chEmEF);
   fChain->SetBranchAddress("jets_chHEF", &jets_chHEF, &b_jets_chHEF);
   fChain->SetBranchAddress("jets_nEmEF", &jets_nEmEF, &b_jets_nEmEF);
   fChain->SetBranchAddress("jets_nHEF", &jets_nHEF, &b_jets_nHEF);
   fChain->SetBranchAddress("jets_MUF", &jets_MUF, &b_jets_MUF);
   fChain->SetBranchAddress("jets_neMult", &jets_neMult, &b_jets_neMult);
   fChain->SetBranchAddress("jets_chMult", &jets_chMult, &b_jets_chMult);
   fChain->SetBranchAddress("bDiscriminator", &bDiscriminator, &b_bDiscriminator);
   fChain->SetBranchAddress("bCSVscore", &bCSVscore, &b_bCSVscore);
   fChain->SetBranchAddress("pfCombinedMVAV2BJetTags", &pfCombinedMVAV2BJetTags, &b_pfCombinedMVAV2BJetTags);
   fChain->SetBranchAddress("bDeepCSV_probb", &bDeepCSV_probb, &b_bDeepCSV_probb);
   fChain->SetBranchAddress("bDeepCSV_probbb", &bDeepCSV_probbb, &b_bDeepCSV_probbb);
   fChain->SetBranchAddress("bDeepCSV_probudsg", &bDeepCSV_probudsg, &b_bDeepCSV_probudsg);
   fChain->SetBranchAddress("bDeepCSV_probc", &bDeepCSV_probc, &b_bDeepCSV_probc);
   fChain->SetBranchAddress("bDeepCSV_probcc", &bDeepCSV_probcc, &b_bDeepCSV_probcc);
   fChain->SetBranchAddress("bDeepFlavor_probb", &bDeepFlavor_probb, &b_bDeepFlavor_probb);
   fChain->SetBranchAddress("bDeepFlavor_probbb", &bDeepFlavor_probbb, &b_bDeepFlavor_probbb);
   fChain->SetBranchAddress("bDeepFlavor_problepb", &bDeepFlavor_problepb, &b_bDeepFlavor_problepb);
   fChain->SetBranchAddress("bDeepFlavor_probc", &bDeepFlavor_probc, &b_bDeepFlavor_probc);
   fChain->SetBranchAddress("bDeepFlavor_probuds", &bDeepFlavor_probuds, &b_bDeepFlavor_probuds);
   fChain->SetBranchAddress("bDeepFlavor_probg", &bDeepFlavor_probg, &b_bDeepFlavor_probg);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probbb", &bParticleNetAK4JetTags_probbb, &b_bParticleNetAK4JetTags_probbb);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probpu", &bParticleNetAK4JetTags_probpu, &b_bParticleNetAK4JetTags_probpu);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probcc", &bParticleNetAK4JetTags_probcc, &b_bParticleNetAK4JetTags_probcc);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probundef", &bParticleNetAK4JetTags_probundef, &b_bParticleNetAK4JetTags_probundef);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probc", &bParticleNetAK4JetTags_probc, &b_bParticleNetAK4JetTags_probc);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probb", &bParticleNetAK4JetTags_probb, &b_bParticleNetAK4JetTags_probb);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probuds", &bParticleNetAK4JetTags_probuds, &b_bParticleNetAK4JetTags_probuds);
   fChain->SetBranchAddress("bParticleNetAK4JetTags_probg", &bParticleNetAK4JetTags_probg, &b_bParticleNetAK4JetTags_probg);
   fChain->SetBranchAddress("jets_bjetRegCorr", &jets_bjetRegCorr, &b_jets_bjetRegCorr);
   fChain->SetBranchAddress("jets_bjetRegRes", &jets_bjetRegRes, &b_jets_bjetRegRes);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probmu", &bParticleNetTauAK4JetTags_probmu, &b_bParticleNetTauAK4JetTags_probmu);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probele", &bParticleNetTauAK4JetTags_probele, &b_bParticleNetTauAK4JetTags_probele);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaup1h0p", &bParticleNetTauAK4JetTags_probtaup1h0p, &b_bParticleNetTauAK4JetTags_probtaup1h0p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaup1h1p", &bParticleNetTauAK4JetTags_probtaup1h1p, &b_bParticleNetTauAK4JetTags_probtaup1h1p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaup1h2p", &bParticleNetTauAK4JetTags_probtaup1h2p, &b_bParticleNetTauAK4JetTags_probtaup1h2p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaup3h0p", &bParticleNetTauAK4JetTags_probtaup3h0p, &b_bParticleNetTauAK4JetTags_probtaup3h0p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaup3h1p", &bParticleNetTauAK4JetTags_probtaup3h1p, &b_bParticleNetTauAK4JetTags_probtaup3h1p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaum1h0p", &bParticleNetTauAK4JetTags_probtaum1h0p, &b_bParticleNetTauAK4JetTags_probtaum1h0p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaum1h1p", &bParticleNetTauAK4JetTags_probtaum1h1p, &b_bParticleNetTauAK4JetTags_probtaum1h1p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaum1h2p", &bParticleNetTauAK4JetTags_probtaum1h2p, &b_bParticleNetTauAK4JetTags_probtaum1h2p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaum3h0p", &bParticleNetTauAK4JetTags_probtaum3h0p, &b_bParticleNetTauAK4JetTags_probtaum3h0p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probtaum3h1p", &bParticleNetTauAK4JetTags_probtaum3h1p, &b_bParticleNetTauAK4JetTags_probtaum3h1p);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probb", &bParticleNetTauAK4JetTags_probb, &b_bParticleNetTauAK4JetTags_probb);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probc", &bParticleNetTauAK4JetTags_probc, &b_bParticleNetTauAK4JetTags_probc);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probuds", &bParticleNetTauAK4JetTags_probuds, &b_bParticleNetTauAK4JetTags_probuds);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_probg", &bParticleNetTauAK4JetTags_probg, &b_bParticleNetTauAK4JetTags_probg);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_ptcorr", &bParticleNetTauAK4JetTags_ptcorr, &b_bParticleNetTauAK4JetTags_ptcorr);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_ptreshigh", &bParticleNetTauAK4JetTags_ptreshigh, &b_bParticleNetTauAK4JetTags_ptreshigh);
   fChain->SetBranchAddress("bParticleNetTauAK4JetTags_ptreslow", &bParticleNetTauAK4JetTags_ptreslow, &b_bParticleNetTauAK4JetTags_ptreslow);
   fChain->SetBranchAddress("PFjetID", &PFjetID, &b_PFjetID);
   fChain->SetBranchAddress("jetRawf", &jetRawf, &b_jetRawf);
   fChain->SetBranchAddress("jets_JER", &jets_JER, &b_jets_JER);
   fChain->SetBranchAddress("susyModel", &susyModel, &b_susyModel);
   fChain->SetBranchAddress("ak8jets_px", &ak8jets_px, &b_ak8jets_px);
   fChain->SetBranchAddress("ak8jets_py", &ak8jets_py, &b_ak8jets_py);
   fChain->SetBranchAddress("ak8jets_pz", &ak8jets_pz, &b_ak8jets_pz);
   fChain->SetBranchAddress("ak8jets_e", &ak8jets_e, &b_ak8jets_e);
   fChain->SetBranchAddress("ak8jets_SoftDropMass", &ak8jets_SoftDropMass, &b_ak8jets_SoftDropMass);
   fChain->SetBranchAddress("ak8jets_PrunedMass", &ak8jets_PrunedMass, &b_ak8jets_PrunedMass);
   fChain->SetBranchAddress("ak8jets_TrimmedMass", &ak8jets_TrimmedMass, &b_ak8jets_TrimmedMass);
   fChain->SetBranchAddress("ak8jets_FilteredMass", &ak8jets_FilteredMass, &b_ak8jets_FilteredMass);
   fChain->SetBranchAddress("ak8jets_tau1", &ak8jets_tau1, &b_ak8jets_tau1);
   fChain->SetBranchAddress("ak8jets_tau2", &ak8jets_tau2, &b_ak8jets_tau2);
   fChain->SetBranchAddress("ak8jets_tau3", &ak8jets_tau3, &b_ak8jets_tau3);
   fChain->SetBranchAddress("ak8jets_tau4", &ak8jets_tau4, &b_ak8jets_tau4);
   fChain->SetBranchAddress("ak8jets_CSV", &ak8jets_CSV, &b_ak8jets_CSV);
   fChain->SetBranchAddress("ak8jets_deepCSV_probb", &ak8jets_deepCSV_probb, &b_ak8jets_deepCSV_probb);
   fChain->SetBranchAddress("ak8jets_deepCSV_probbb", &ak8jets_deepCSV_probbb, &b_ak8jets_deepCSV_probbb);
   fChain->SetBranchAddress("ak8jets_deepFlavor_probb", &ak8jets_deepFlavor_probb, &b_ak8jets_deepFlavor_probb);
   fChain->SetBranchAddress("ak8jets_deepFlavor_probbb", &ak8jets_deepFlavor_probbb, &b_ak8jets_deepFlavor_probbb);
   fChain->SetBranchAddress("ak8jets_deepFlavor_problepb", &ak8jets_deepFlavor_problepb, &b_ak8jets_deepFlavor_problepb);
   fChain->SetBranchAddress("ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb", &ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb, &b_ak8jets_massIndependentDeepDoubleBvLJetTags_probHbb);
   fChain->SetBranchAddress("ak8jets_deepDoubleBvLJetTags_probHbb", &ak8jets_deepDoubleBvLJetTags_probHbb, &b_ak8jets_deepDoubleBvLJetTags_probHbb);
   fChain->SetBranchAddress("ak8jets_deepBoostedJetTags_probHbb", &ak8jets_deepBoostedJetTags_probHbb, &b_ak8jets_deepBoostedJetTags_probHbb);
   fChain->SetBranchAddress("ak8jets_particleNetJetTags_probHbb", &ak8jets_particleNetJetTags_probHbb, &b_ak8jets_particleNetJetTags_probHbb);
   fChain->SetBranchAddress("ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD", &ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD, &b_ak8jets_particleNetDiscriminatorsJetTags_HbbvsQCD);
   fChain->SetBranchAddress("ak8jets_nsubjets", &ak8jets_nsubjets, &b_ak8jets_nsubjets);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHtt", &bParticleNetTauAK8JetTags_probHtt, &b_bParticleNetTauAK8JetTags_probHtt);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHtm", &bParticleNetTauAK8JetTags_probHtm, &b_bParticleNetTauAK8JetTags_probHtm);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHte", &bParticleNetTauAK8JetTags_probHte, &b_bParticleNetTauAK8JetTags_probHte);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHbb", &bParticleNetTauAK8JetTags_probHbb, &b_bParticleNetTauAK8JetTags_probHbb);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHcc", &bParticleNetTauAK8JetTags_probHcc, &b_bParticleNetTauAK8JetTags_probHcc);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHqq", &bParticleNetTauAK8JetTags_probHqq, &b_bParticleNetTauAK8JetTags_probHqq);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probHgg", &bParticleNetTauAK8JetTags_probHgg, &b_bParticleNetTauAK8JetTags_probHgg);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probQCD2hf", &bParticleNetTauAK8JetTags_probQCD2hf, &b_bParticleNetTauAK8JetTags_probQCD2hf);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probQCD1hf", &bParticleNetTauAK8JetTags_probQCD1hf, &b_bParticleNetTauAK8JetTags_probQCD1hf);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_probQCD0hf", &bParticleNetTauAK8JetTags_probQCD0hf, &b_bParticleNetTauAK8JetTags_probQCD0hf);
   fChain->SetBranchAddress("bParticleNetTauAK8JetTags_masscorr", &bParticleNetTauAK8JetTags_masscorr, &b_bParticleNetTauAK8JetTags_masscorr);
   fChain->SetBranchAddress("subjets_px", &subjets_px, &b_subjets_px);
   fChain->SetBranchAddress("subjets_py", &subjets_py, &b_subjets_py);
   fChain->SetBranchAddress("subjets_pz", &subjets_pz, &b_subjets_pz);
   fChain->SetBranchAddress("subjets_e", &subjets_e, &b_subjets_e);
   fChain->SetBranchAddress("subjets_CSV", &subjets_CSV, &b_subjets_CSV);
   fChain->SetBranchAddress("subjets_deepCSV_probb", &subjets_deepCSV_probb, &b_subjets_deepCSV_probb);
   fChain->SetBranchAddress("subjets_deepCSV_probbb", &subjets_deepCSV_probbb, &b_subjets_deepCSV_probbb);
   fChain->SetBranchAddress("subjets_deepFlavor_probb", &subjets_deepFlavor_probb, &b_subjets_deepFlavor_probb);
   fChain->SetBranchAddress("subjets_deepFlavor_probbb", &subjets_deepFlavor_probbb, &b_subjets_deepFlavor_probbb);
   fChain->SetBranchAddress("subjets_deepFlavor_problepb", &subjets_deepFlavor_problepb, &b_subjets_deepFlavor_problepb);
   fChain->SetBranchAddress("subjets_ak8MotherIdx", &subjets_ak8MotherIdx, &b_subjets_ak8MotherIdx);
   fChain->SetBranchAddress("pvGen_x", &pvGen_x, &b_pvGen_x);
   fChain->SetBranchAddress("pvGen_y", &pvGen_y, &b_pvGen_y);
   fChain->SetBranchAddress("pvGen_z", &pvGen_z, &b_pvGen_z);
   Notify();
}

Bool_t BigN::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void BigN::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t BigN::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef BigN_cxx

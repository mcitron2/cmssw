// -*- C++ -*-
//
// Package:    PATMHTProducer
// Class:      PATMHTProducer
// 
/**\class PATMHTProducer 

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Xin Shi & Freya Blekman, Cornell University
//         Created:  Fri Sep 12 17:58:29 CEST 2008
// $Id: PATMHTProducer.h,v 1.4 2010/01/11 13:36:48 hegner Exp $
//
//

#ifndef PhysicsTools_PatAlgos_PATMHTProducer_h
#define PhysicsTools_PatAlgos_PATMHTProducer_h



// system include files
#include <memory>

// user include files

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "FWCore/Utilities/interface/InputTag.h" 
#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/PatCandidates/interface/MHT.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"


#include "RecoMET/METAlgorithms/interface/SigInputObj.h"
#include "RecoMET/METAlgorithms/interface/SignAlgoResolutions.h"
#include "RecoMET/METAlgorithms/interface/significanceAlgo.h"


#include "TF1.h"
#include "TMath.h"

//
// class declaration
//

namespace pat {
  class PATMHTProducer : public edm::EDProducer {
  public:
    explicit PATMHTProducer(const edm::ParameterSet&);
    ~PATMHTProducer();
    
  private:
    virtual void beginJob() ;
    virtual void beginRun(const edm::EventSetup&) ;
    virtual void produce(edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;
    
    double getJets(edm::Event&, const edm::EventSetup&);
    double getElectrons(edm::Event&, const edm::EventSetup&);
    double getMuons(edm::Event&, const edm::EventSetup&);
    void   getTowers(edm::Event&, const edm::EventSetup&);
    
    
    // ----------member data ---------------------------
    
    double verbose_;
    
    // input tags.
    edm::InputTag mhtLabel_;
    edm::InputTag jetLabel_;
    edm::InputTag eleLabel_;
    edm::InputTag muoLabel_;
    edm::InputTag tauLabel_;
    edm::InputTag phoLabel_;
  
    std::vector<metsig::SigInputObj> physobjvector_ ;

    double uncertaintyScaleFactor_; // scale factor for the uncertainty parameters.
    bool    controlledUncertainty_; // use controlled uncertainty parameters.

 
    //--- test the uncertainty parameters ---//

    class uncertaintyFunctions{
    public:
      TF1 *etUncertainty;
      TF1 *phiUncertainty;
    };

    void setUncertaintyParameters();// fills the following uncertaintyFunctions objects:
    uncertaintyFunctions ecalEBUncertainty;
    uncertaintyFunctions ecalEEUncertainty;
    uncertaintyFunctions hcalHBUncertainty;
    uncertaintyFunctions hcalHEUncertainty;
    uncertaintyFunctions hcalHOUncertainty;
    uncertaintyFunctions hcalHFUncertainty;

    uncertaintyFunctions jetUncertainty;
    uncertaintyFunctions jetCorrUncertainty;
    uncertaintyFunctions eleUncertainty;
    uncertaintyFunctions muonUncertainty;
    uncertaintyFunctions muonCorrUncertainty;

    //--- tags and parameters ---//

    bool useCaloTowers_;
    bool useJets_;
    bool useElectrons_;
    bool useMuons_;
    std::set<CaloTowerDetId> s_clusteredTowers; 

    bool noHF_;

    double jetPtMin_;
    double jetEtaMax_;
    double jetEMfracMax_;

    double elePtMin_;
    double eleEtaMax_;

    double muonPtMin_;
    double muonEtaMax_;
    double muonTrackD0Max_;
    double muonTrackDzMax_;
    int muonNHitsMin_;
    double muonDPtMax_;
    double muonChiSqMax_;

    //  double uncertaintyScaleFactor_; // scale factor for the uncertainty parameters.

    double jetEtUncertaintyParameter0_ ; 
    double jetEtUncertaintyParameter1_ ; 
    double jetEtUncertaintyParameter2_ ; 

    double jetPhiUncertaintyParameter0_ ; 
    double jetPhiUncertaintyParameter1_ ; 
    double jetPhiUncertaintyParameter2_ ; 

    double eleEtUncertaintyParameter0_ ; 
    double elePhiUncertaintyParameter0_ ; 

    double muonEtUncertaintyParameter0_ ; 
    double muonPhiUncertaintyParameter0_ ; 

    edm::InputTag CaloJetAlgorithmTag_; 
    edm::InputTag CorJetAlgorithmTag_;
    std::string   JetCorrectionService_;
    edm::InputTag MuonTag_;
    edm::InputTag ElectronTag_;
    edm::InputTag CaloTowerTag_;
    std::string metCollectionLabel_;
    std::string significanceLabel_;

    //--- For Muon Calo Deposits ---//
    //TrackDetectorAssociator   trackAssociator_; 
    //TrackAssociatorParameters trackAssociatorParameters_;

    double towerEtThreshold_ ; 
    bool useHO_ ; 


  };
  //define this as a plug-in

} //end of namespace

#endif

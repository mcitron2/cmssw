// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/Handle.h" 
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

#include "AnalysisDataFormats/SUSYBSMObjects/interface/HSCParticle.h"

using namespace edm;
using namespace reco;
using namespace susybsm;


class  BetaCalculatorMUON{
   public:
      BetaCalculatorMUON(const edm::ParameterSet& iConfig);
      void  addInfoToCandidate(HSCParticle& candidate, edm::Event& iEvent, const edm::EventSetup& iSetup);

      edm::InputTag m_muontiming_dt;
      edm::InputTag m_muontiming_csc;
      edm::InputTag m_muontiming_combined;
};



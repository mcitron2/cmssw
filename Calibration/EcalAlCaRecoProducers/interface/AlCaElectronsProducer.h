#ifndef _ALCAELECTRONSPRODUCER_H
#define _ALCAELECTRONSPRODUCER_H

// -*- C++ -*-
//
// Package:    AlCaElectronsProducer
// Class:      AlCaElectronsProducer
// 
/**\class AlCaElectronsProducer AlCaElectronsProducer.cc Calibration/EcalAlCaRecoProducers/src/AlCaElectronsProducer.cc

 Description: Example of a producer of AlCa electrons

 Implementation:
     <Notes on implementation>

*/
//
// Original Author:  Lorenzo AGOSTINO
//         Created:  Mon Jul 17 18:07:01 CEST 2006
// $Id: AlCaElectronsProducer.h,v 1.12 2010/01/06 17:46:42 presotto Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//PG #include "TH2.h"
//PG #include "TFile.h"
//PG #include "TCanvas.h"

//!
//! class declaration
//!

class AlCaElectronsProducer : public edm::EDProducer {
   public:
      //! ctor
      explicit AlCaElectronsProducer(const edm::ParameterSet&);
      ~AlCaElectronsProducer();

 
//PG       void beginJob (const edm::EventSetup&)
//PG         {
//PG           std::cerr << "saveTest beginJob" << std::endl ;
//PG           m_failMap = new TH2F ("failMap","failMap",100,0,100,100,0,100) ;
//PG           std::cerr << "saveTest beginJob " << m_failMap->GetEntries () << std::endl ;
//PG         }
      //! producer
      virtual void produce(edm::Event &, const edm::EventSetup&);
//PG       void endJob () 
//PG         {
//PG           std::cerr << "saveTest endJob" << std::endl ;
//PG           TCanvas c1 ;
//PG           c1.cd () ;
//PG           m_failMap->Draw ("BOX") ;
//PG           c1.Print ("fail.eps","eps") ;
//PG           TDirectory * curr = gDirectory ;
//PG           TFile * saveTest = new TFile ("fail.root","recreate") ;
//PG           saveTest->cd () ;
//PG           m_failMap->Write () ;
//PG           curr->cd () ;
//PG           saveTest->Close () ;
//PG         }

   private:
      // ----------member data ---------------------------

  
  edm::InputTag ebRecHitsLabel_;
  edm::InputTag eeRecHitsLabel_;
  edm::InputTag esRecHitsLabel_;
  edm::InputTag electronLabel_;
  std::string alcaBarrelHitsCollection_;
  std::string alcaEndcapHitsCollection_;
  std::string alcaPreshowerHitsCollection_;
  int etaSize_;
  int phiSize_;
  float weight_;
  int esNstrips_;
  int esNcolumns_;

  bool selectByEleNum_;
  int minEleNumber_;
  double minElePt_;

//PG  TH2F * m_failMap ;

};

#endif

#ifndef RxCalculator_h
#define RxCalculator_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"

#include "RecoCaloTools/MetaCollections/interface/CaloRecHitMetaCollections.h"


class RxCalculator
{
  public:
  
   RxCalculator(const edm::Event &iEvent, const edm::EventSetup &iSetup, edm::InputTag hbheLabel, edm::InputTag hfLabel, edm::InputTag hoLabel) ;
  
   double getRx (const reco::SuperClusterRef clus, double i, double threshold);
   double getRFx(const reco::SuperClusterRef clus, double i, double threshold);
   double getROx(const reco::SuperClusterRef clus, double i, double threshold);
   double getCRx(const reco::SuperClusterRef clus, double i, double threshold); // background subtracted Rx

  private:
   
   const HBHERecHitCollection         *fHBHERecHits_;
   const HORecHitCollection           *fHORecHits_;
   const HFRecHitCollection           *fHFRecHits_;
   const CaloGeometry                 *geometry_;
};

#endif

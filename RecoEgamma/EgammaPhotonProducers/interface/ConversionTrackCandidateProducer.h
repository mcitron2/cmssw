#ifndef RecoEgamma_EgammaPhotonProducers_ConversionTrackCandidateProducer_h
#define RecoEgamma_EgammaPhotonProducers_ConversionTrackCandidateProducer_h
/** \class ConversionTrackCandidateProducer
 **  
 **
 **  $Id: ConversionTrackCandidateProducer.h,v 1.14 2009/03/04 21:19:55 nancy Exp $ 
 **  $Date: 2009/03/04 21:19:55 $ 
 **  $Revision: 1.14 $
 **  \author Nancy Marinelli, U. of Notre Dame, US
 **
 ***/

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "RecoTracker/MeasurementDet/interface/MeasurementTracker.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "RecoCaloTools/MetaCollections/interface/CaloRecHitMetaCollections.h"
#include "TrackingTools/MeasurementDet/interface/LayerMeasurements.h"
#include "TrackingTools/DetLayers/interface/NavigationSetter.h"
#include "TrackingTools/DetLayers/interface/NavigationSchool.h"
#include "RecoTracker/TkNavigation/interface/SimpleNavigationSchool.h"
#include "RecoTracker/TkDetLayers/interface/GeometricSearchTracker.h"
#include "DataFormats/TrackCandidate/interface/TrackCandidateCollection.h"
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"

class OutInConversionSeedFinder;
class InOutConversionSeedFinder;
class OutInConversionTrackFinder;
class InOutConversionTrackFinder;

// ConversionTrackCandidateProducer inherits from EDProducer, so it can be a module:
class ConversionTrackCandidateProducer : public edm::EDProducer {

 public:

  ConversionTrackCandidateProducer (const edm::ParameterSet& ps);
  ~ConversionTrackCandidateProducer();


  
  virtual void beginRun (edm::Run &, edm::EventSetup const & es);
  virtual void endRun (edm::Run &, edm::EventSetup const & es);
  virtual void produce(edm::Event& evt, const edm::EventSetup& es);

 private:

  int nEvt_;
  
 /// Initialize EventSetup objects at each event
  void setEventSetup( const edm::EventSetup& es ) ;

  std::string OutInTrackCandidateCollection_;
  std::string InOutTrackCandidateCollection_;


  std::string OutInTrackSuperClusterAssociationCollection_;
  std::string InOutTrackSuperClusterAssociationCollection_;
  
  edm::InputTag bcBarrelCollection_;
  edm::InputTag bcEndcapCollection_;
  edm::InputTag scHybridBarrelProducer_;
  edm::InputTag scIslandEndcapProducer_;
  edm::ParameterSet conf_;
  edm::InputTag hcalTowers_;
 
  double hOverEConeSize_;
  double maxHOverE_;
  double minSCEt_;

  edm::ESHandle<CaloGeometry> theCaloGeom_;  

  const NavigationSchool*       theNavigationSchool_;
  OutInConversionSeedFinder*  theOutInSeedFinder_;
  OutInConversionTrackFinder* theOutInTrackFinder_;
  InOutConversionSeedFinder*  theInOutSeedFinder_;
  InOutConversionTrackFinder* theInOutTrackFinder_;


  std::vector<edm::Ptr<reco::CaloCluster> > caloPtrVecOutIn_; 
  std::vector<edm::Ptr<reco::CaloCluster> > caloPtrVecInOut_; 

  std::vector<edm::Ref<reco::SuperClusterCollection> > vecOfSCRefForOutIn;  
  std::vector<edm::Ref<reco::SuperClusterCollection> > vecOfSCRefForInOut;  
  
  void buildCollections( const edm::Handle<edm::View<reco::CaloCluster> > & scHandle,
			 const edm::Handle<edm::View<reco::CaloCluster> > & bcHandle,
			 const edm::Handle<CaloTowerCollection> & hcalTowersHandle,
			 TrackCandidateCollection& outInTracks,
			 TrackCandidateCollection& inOutTracks,
			 std::vector<edm::Ptr<reco::CaloCluster> >& vecRecOI,
			 std::vector<edm::Ptr<reco::CaloCluster> >& vecRecIO
);


};
#endif

#ifndef _SiPixelDataQuality_h_
#define _SiPixelDataQuality_h_

#include "DQMServices/Core/interface/MonitorElement.h"

#include "DQM/SiPixelMonitorClient/interface/SiPixelConfigParser.h"
#include "DQM/SiPixelMonitorClient/interface/SiPixelConfigWriter.h"
#include "DQM/SiPixelMonitorClient/interface/SiPixelActionExecutor.h"
#include "DQM/SiPixelMonitorClient/interface/SiPixelLayoutParser.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/SiPixelDigi/interface/PixelDigi.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/SiPixelObjects/interface/DetectorIndex.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFrameConverter.h"

#include "xgi/Utils.h"
#include "xgi/Method.h"

#include "TCanvas.h"
#include "TPaveText.h"
#include "TF1.h"
#include "TH2F.h"
#include "TGaxis.h"

#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <string>
#include <map>
#include <boost/cstdint.hpp>

class DQMStore;
class SiPixelEDAClient;
class SiPixelWebInterface;
class SiPixelHistoPlotter;
class SiPixelDataQuality {

 public:

  SiPixelDataQuality(  bool                                      offlineXMLfile);
 ~SiPixelDataQuality();

  int getDetId(                 MonitorElement                          * mE) ;				

  void bookGlobalQualityFlag    (DQMStore                               * bei,
				 bool                                     Tier0Flag,
				 int                                      nFEDs);

  void computeGlobalQualityFlag (DQMStore                               * bei,
                                 bool                                     init,
				 int                                      nFEDs,
				 bool                                     Tier0Flag);
  
  void computeGlobalQualityFlagByLumi (DQMStore                         * bei,
                                       bool                               init,
				       int                                nFEDs,
				       bool                               Tier0Flag,
				       int                                nEvents_lastLS_);
  
  void fillGlobalQualityPlot    (DQMStore                               * bei,
                                 bool                                     init,
                                 edm::EventSetup const                  & eSetup,
				 int                                      nFEDs,
				 bool                                     Tier0Flag,
				 int                                      lumisec);
  
 private:

  bool  offlineXMLfile_;
  
  
  TH2F * allmodsMap;
  TH2F * errmodsMap;
  TH2F * goodmodsMap;
  TH1D * allmodsVec;
  TH1D * errmodsVec;
  TH1D * goodmodsVec;
  int count;
  int errcount;
  bool gotDigis;
  
  int objectCount_;
  bool DONE_;
  
  
  ofstream myfile_;  
  int nevents_;
  bool endOfModules_;
  edm::ESHandle<SiPixelFedCablingMap> theCablingMap;
  
  // Final combined Data Quality Flags:
  MonitorElement * SummaryReportMap;
  MonitorElement * SummaryPixel;
  MonitorElement * SummaryBarrel;
  MonitorElement * SummaryEndcap;
  float qflag_;
  int allMods_, errorMods_, barrelMods_, endcapMods_;
 
  // FEDErrors Cuts:
  MonitorElement * NErrorsBarrel;
  MonitorElement * NErrorsEndcap;
  MonitorElement * NErrorsFEDs;
  int n_errors_barrel_, n_errors_endcap_, n_errors_pixel_;
  float barrel_error_flag_, endcap_error_flag_, pixel_error_flag_;
  
  bool digiStatsBarrel, clusterStatsBarrel, trackStatsBarrel;
  int digiCounterBarrel, clusterCounterBarrel, trackCounterBarrel;
  bool digiStatsEndcap, clusterStatsEndcap, trackStatsEndcap;
  int digiCounterEndcap, clusterCounterEndcap, trackCounterEndcap;

  // Digis Cuts:
  MonitorElement * NDigisBarrel;
  MonitorElement * NDigisEndcap;
  MonitorElement * DigiChargeBarrel;
  MonitorElement * DigiChargeEndcap;
  
  // Cluster Cuts:
  MonitorElement * ClusterSizeBarrel;
  MonitorElement * ClusterSizeEndcap;
  MonitorElement * ClusterChargeBarrel;
  MonitorElement * ClusterChargeEndcap;
  MonitorElement * NClustersBarrel;
  MonitorElement * NClustersEndcap;
  
  // Track Cuts:
  MonitorElement * NPixelTracks;
    
  int count1;
  int count2;
  int count3;
  int count4;
  int count5;
  int count6;
  
  int timeoutCounter_;
  int modCounter_;
  int lastLS_;
};
#endif

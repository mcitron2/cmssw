#ifndef SiStripMonitorCluster_SiStripMonitorCluster_h
#define SiStripMonitorCluster_SiStripMonitorCluster_h
// -*- C++ -*-
// Package:     SiStripMonitorCluster
// Class  :     SiStripMonitorCluster
/**\class SiStripMonitorCluster SiStripMonitorCluster.h DQM/SiStripMonitorCluster/interface/SiStripMonitorCluster.h
   Data Quality Monitoring source of the Silicon Strip Tracker. Produces histograms related to clusters.
*/
// Original Author:  dkcira
//         Created:  Wed Feb  1 16:47:14 CET 2006
// $Id: SiStripMonitorCluster.h,v 1.35 2010/04/22 16:26:59 dutta Exp $
#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DQM/SiStripCommon/interface/TkHistoMap.h"

#include <vector>

class DQMStore;
class SiStripDetCabling;
class SiStripCluster;
class SiStripDCSStatus;

class SiStripMonitorCluster : public edm::EDAnalyzer {
 public:
  explicit SiStripMonitorCluster(const edm::ParameterSet&);
  ~SiStripMonitorCluster();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  //virtual void beginJob() ;
  virtual void endJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);

  struct ModMEs{ // MEs for one single detector module

    MonitorElement* NumberOfClusters;
    MonitorElement* ClusterPosition;
    MonitorElement* ClusterDigiPosition;
    MonitorElement* ClusterWidth;
    MonitorElement* ClusterCharge;
    MonitorElement* ClusterNoise;
    MonitorElement* ClusterSignalOverNoise;
    MonitorElement* ClusterSignalOverNoiseVsPos;
    MonitorElement* ModuleLocalOccupancy;
    MonitorElement* NrOfClusterizedStrips; // can be used at client level for occupancy calculations
  };

  struct LayerMEs{ // MEs for Layer Level
    MonitorElement* LayerClusterStoN;
    MonitorElement* LayerClusterStoNTrend;
    MonitorElement* LayerClusterCharge;
    MonitorElement* LayerClusterChargeTrend;
    MonitorElement* LayerClusterNoise;
    MonitorElement* LayerClusterNoiseTrend;
    MonitorElement* LayerClusterWidth;
    MonitorElement* LayerClusterWidthTrend;
    MonitorElement* LayerLocalOccupancy;
    MonitorElement* LayerLocalOccupancyTrend;
    MonitorElement* LayerNumberOfClusterProfile;
    MonitorElement* LayerClusterWidthProfile;

  };

  struct SubDetMEs{ // MEs for Subdetector Level
    int totNClusters; 
    MonitorElement* SubDetTotClusterTH1;
    MonitorElement* SubDetTotClusterProf;
    MonitorElement* SubDetClusterApvProf;
    MonitorElement* SubDetClusterApvTH2;
    MonitorElement* SubDetClusterDBxCycleProf;
    MonitorElement* SubDetApvDBxProf2;
  };

  struct ClusterProperties { // Cluster Properties
    float charge;
    float position;
    short start;
    short width;
    float noise;
  };

  MonitorElement* GlobalApvCycleDBxTH2; 
 private:

  void createMEs(const edm::EventSetup& es);
  void createLayerMEs(std::string label, int ndets);
  void createModuleMEs(ModMEs& mod_single, uint32_t detid);
  void createSubDetMEs(std::string label);

  void fillModuleMEs(ModMEs& mod_mes, ClusterProperties& cluster);
  void fillLayerMEs(LayerMEs&, ClusterProperties& cluster, float timeinorbit);

  void ResetModuleMEs(uint32_t idet);

  inline void fillME(MonitorElement* ME,float value1){if (ME!=0)ME->Fill(value1);}
  inline void fillME(MonitorElement* ME,float value1,float value2){if (ME!=0)ME->Fill(value1,value2);}
  inline void fillME(MonitorElement* ME,float value1,float value2,float value3){if (ME!=0)ME->Fill(value1,value2,value3);}
  inline void fillME(MonitorElement* ME,float value1,float value2,float value3,float value4){if (ME!=0)ME->Fill(value1,value2,value3,value4);}
  MonitorElement * bookMETrend(const char*, const char*);
  MonitorElement* bookME1D(const char* ParameterSetLabel, const char* HistoName);

 private:
  DQMStore* dqmStore_;
  edm::ParameterSet conf_;
  std::map<uint32_t, ModMEs> ModuleMEsMap;
  std::map<std::string, LayerMEs> LayerMEsMap;
  std::map<std::string, std::vector< uint32_t > > LayerDetMap;
  std::map<std::string, SubDetMEs> SubDetMEsMap;
  std::map<std::string, std::string> SubDetPhasePartMap;

  // flags
  bool show_mechanical_structure_view, show_readout_view, show_control_view, select_all_detectors, reset_each_run;
  unsigned long long m_cacheID_;

  edm::ESHandle<SiStripDetCabling> SiStripDetCabling_;
  std::vector<uint32_t> ModulesToBeExcluded_;

  edm::ParameterSet Parameters;

  // TkHistoMap added
  TkHistoMap* tkmapcluster; 

  int runNb, eventNb;
  int firstEvent;

  bool layerswitchncluson;
  bool layerswitchcluschargeon;
  bool layerswitchclusstonon;
  bool layerswitchclusstonVsposon;
  bool layerswitchclusposon;
  bool layerswitchclusdigiposon;
  bool layerswitchclusnoiseon;
  bool layerswitchcluswidthon;
  bool layerswitchlocaloccupancy;
  bool layerswitchnrclusterizedstrip;
  bool layerswitchnumclusterprofon;
  bool layerswitchclusterwidthprofon;

  bool moduleswitchncluson;
  bool moduleswitchcluschargeon;
  bool moduleswitchclusstonon;
  bool moduleswitchclusstonVsposon;
  bool moduleswitchclusposon;
  bool moduleswitchclusdigiposon;
  bool moduleswitchclusnoiseon;
  bool moduleswitchcluswidthon;
  bool moduleswitchlocaloccupancy;
  bool moduleswitchnrclusterizedstrip;
  bool subdetswitchtotclusprofon;
  bool subdetswitchapvcycleprofon;
  bool subdetswitchapvcycleth2on;
  bool subdetswitchapvcycledbxprof2on;
  bool subdetswitchdbxcycleprofon;
  bool subdetswitchtotclusth1on;
  bool globalswitchapvcycledbxth2on;

  bool clustertkhistomapon;
  bool createTrendMEs;

  bool Mod_On_;

  std::string topFolderName_;
  std::string qualityLabel_;

  edm::InputTag clusterProducer_;
  edm::InputTag historyProducer_;  
  edm::InputTag apvPhaseProducer_;

  bool   applyClusterQuality_;
  double sToNLowerLimit_;  
  double sToNUpperLimit_;  
  double widthLowerLimit_;
  double widthUpperLimit_;

  SiStripDCSStatus* dcsStatus_;
};
#endif

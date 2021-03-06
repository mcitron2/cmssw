// $Id: SealModule.cc,v 1.27 2010/11/09 15:23:56 markusm Exp $

#include "DQMOffline/Trigger/interface/FourVectorHLTClient.h"
#include "DQMOffline/Trigger/interface/FourVectorHLTOffline.h"
#include "DQMOffline/Trigger/interface/EgHLTOfflineSource.h"
#include "DQMOffline/Trigger/interface/EgHLTOfflineClient.h"
#include "DQMOffline/Trigger/interface/EgHLTOfflineSummaryClient.h"
#include "DQMOffline/Trigger/interface/HLTTauRefProducer.h"
#include "DQMOffline/Trigger/interface/HLTTauDQMOfflineSource.h"
#include "DQMOffline/Trigger/interface/HLTTauPostProcessor.h"
#include "DQMOffline/Trigger/interface/JetMETHLTOfflineSource.h"
#include "DQMOffline/Trigger/interface/JetMETHLTOfflineClient.h"
#include "DQMOffline/Trigger/interface/DQMOfflineHLTEventInfoClient.h"
#include "DQMOffline/Trigger/interface/HLTTauCertifier.h"
#include "DQMOffline/Trigger/interface/TopHLTDiMuonDQM.h"
#include "DQMOffline/Trigger/interface/TopHLTDiMuonDQMClient.h"

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(FourVectorHLTClient);
DEFINE_FWK_MODULE(FourVectorHLTOffline);
DEFINE_FWK_MODULE(EgHLTOfflineSource);
DEFINE_FWK_MODULE(EgHLTOfflineClient);
DEFINE_FWK_MODULE(EgHLTOfflineSummaryClient);
DEFINE_FWK_MODULE(HLTTauRefProducer);
DEFINE_FWK_MODULE(HLTTauDQMOfflineSource);
DEFINE_FWK_MODULE(HLTTauPostProcessor);
DEFINE_FWK_MODULE(JetMETHLTOfflineSource);
DEFINE_FWK_MODULE(JetMETHLTOfflineClient);
DEFINE_FWK_MODULE(DQMOfflineHLTEventInfoClient);
DEFINE_FWK_MODULE(HLTTauCertifier);
DEFINE_FWK_MODULE(TopHLTDiMuonDQM);
DEFINE_FWK_MODULE(TopHLTDiMuonDQMClient);


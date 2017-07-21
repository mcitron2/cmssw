import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.BTaggingMonitor_cfi import hltBTVmonitoring

#BTagMu AK4
BTagMu_AK4DiJet20_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4DiJet20_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK4DiJet20_Mu5')
BTagMu_AK4DiJet20_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4DiJet20_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4DiJet20_Mu5.njets = cms.uint32(2)
BTagMu_AK4DiJet20_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4DiJet20_Mu5.jetSelection = cms.string('pt>10 & abs(eta)<2.4')
BTagMu_AK4DiJet20_Mu5.bjetSelection = cms.string('pt>5 & abs(eta)<2.4')
BTagMu_AK4DiJet20_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4DiJet20_Mu5_v*')
BTagMu_AK4DiJet20_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,10,15,20,30,50,70,100,150,200,400,700,1000,1500,3000)

BTagMu_AK4DiJet40_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4DiJet40_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK4DiJet40_Mu5')
BTagMu_AK4DiJet40_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4DiJet40_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4DiJet40_Mu5.njets = cms.uint32(2)
BTagMu_AK4DiJet40_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4DiJet40_Mu5.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
BTagMu_AK4DiJet40_Mu5.bjetSelection = cms.string('pt>20 & abs(eta)<2.4')
BTagMu_AK4DiJet40_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4DiJet40_Mu5_v*')
BTagMu_AK4DiJet40_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,30,40,50,70,100,150,200,400,700,1000,1500,3000)

BTagMu_AK4DiJet70_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4DiJet70_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK4DiJet70_Mu5')
BTagMu_AK4DiJet70_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4DiJet70_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4DiJet70_Mu5.njets = cms.uint32(2)
BTagMu_AK4DiJet70_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4DiJet70_Mu5.jetSelection = cms.string('pt>50 & abs(eta)<2.4')
BTagMu_AK4DiJet70_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4DiJet70_Mu5_v*')
BTagMu_AK4DiJet70_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,50,60,70,80,90,100,150,200,400,700,1000,1500,3000)

BTagMu_AK4DiJet110_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4DiJet110_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK4DiJet110_Mu5')
BTagMu_AK4DiJet110_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4DiJet110_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4DiJet110_Mu5.njets = cms.uint32(2)
BTagMu_AK4DiJet110_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4DiJet110_Mu5.jetSelection = cms.string('pt>90 & abs(eta)<2.4')
BTagMu_AK4DiJet110_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4DiJet110_Mu5_v*')
BTagMu_AK4DiJet110_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,90,100,110,120,130,150,200,400,700,1000,1500,3000)

BTagMu_AK4DiJet170_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4DiJet170_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK4DiJet170_Mu5')
BTagMu_AK4DiJet170_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4DiJet170_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4DiJet170_Mu5.njets = cms.uint32(2)
BTagMu_AK4DiJet170_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4DiJet170_Mu5.jetSelection = cms.string('pt>150 & abs(eta)<2.4')
BTagMu_AK4DiJet170_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4DiJet170_Mu5_v*')
BTagMu_AK4DiJet170_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,150,160,170,180,190,200,400,700,1000,1500,3000)

BTagMu_AK4Jet300_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK4Jet300_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_Jet/BTagMu_AK4Jet300_Mu5')
BTagMu_AK4Jet300_Mu5.nmuons = cms.uint32(1)
BTagMu_AK4Jet300_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK4Jet300_Mu5.njets = cms.uint32(1)
BTagMu_AK4Jet300_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK4Jet300_Mu5.jetSelection = cms.string('pt>250 & abs(eta)<2.4')
BTagMu_AK4Jet300_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK4Jet300_Mu5_v*')
BTagMu_AK4Jet300_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,250,280,300,320,360,400,700,1000,1500,3000)

#BTagMu AK8
BTagMu_AK8DiJet170_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK8DiJet170_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_DiJet/BTagMu_AK8DiJet170_Mu5')
BTagMu_AK8DiJet170_Mu5.nmuons = cms.uint32(1)
BTagMu_AK8DiJet170_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK8DiJet170_Mu5.njets = cms.uint32(2)
BTagMu_AK8DiJet170_Mu5.jets = cms.InputTag("ak8PFJetsCHS")
BTagMu_AK8DiJet170_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK8DiJet170_Mu5.jetSelection = cms.string('pt>150 & abs(eta)<2.4')
BTagMu_AK8DiJet170_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK8DiJet170_Mu5_v*')
BTagMu_AK8DiJet170_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,150,160,170,180,190,200,400,700,1000,1500,3000)

BTagMu_AK8Jet300_Mu5 = hltBTVmonitoring.clone()
BTagMu_AK8Jet300_Mu5.FolderName = cms.string('HLT/BTV/BTagMu_Jet/BTagMu_AK8Jet300_Mu5')
BTagMu_AK8Jet300_Mu5.nmuons = cms.uint32(1)
BTagMu_AK8Jet300_Mu5.nelectrons = cms.uint32(0)
BTagMu_AK8Jet300_Mu5.njets = cms.uint32(1)
BTagMu_AK8Jet300_Mu5.jets = cms.InputTag("ak8PFJetsCHS")
BTagMu_AK8Jet300_Mu5.muoSelection = cms.string('pt>3 & abs(eta)<2.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & globalTrack.hitPattern.numberOfValidMuonHits>0 & globalTrack.normalizedChi2<10')
BTagMu_AK8Jet300_Mu5.jetSelection = cms.string('pt>250 & abs(eta)<2.4')
BTagMu_AK8Jet300_Mu5.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_BTagMu_AK8Jet300_Mu5_v*')
BTagMu_AK8Jet300_Mu5.histoPSet.jetPtBinning = cms.vdouble(0,250,280,300,320,360,400,700,1000,1500,3000)

#PFJet AK4
PFJet40 = hltBTVmonitoring.clone()
PFJet40.FolderName = cms.string('HLT/BTV/PFJet/PFJet40')
PFJet40.nmuons = cms.uint32(0)
PFJet40.nelectrons = cms.uint32(0)
PFJet40.njets = cms.uint32(1)
PFJet40.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
PFJet40.bjetSelection = cms.string('pt>20 & abs(eta)<2.4')
PFJet40.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet40_v*')
PFJet40.histoPSet.jetPtBinning = cms.vdouble(0,30,35,40,45,50,60,70,100,150,200,400,700,1000,1500,3000)

PFJet60 = hltBTVmonitoring.clone()
PFJet60.FolderName = cms.string('HLT/BTV/PFJet/PFJet60')
PFJet60.nmuons = cms.uint32(0)
PFJet60.nelectrons = cms.uint32(0)
PFJet60.njets = cms.uint32(1)
PFJet60.jetSelection = cms.string('pt>50 & abs(eta)<2.4')
PFJet60.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')
PFJet60.histoPSet.jetPtBinning = cms.vdouble(0,50,55,60,65,70,80,90,100,120,150,200,400,700,1000,1500,3000)

PFJet80 = hltBTVmonitoring.clone()
PFJet80.FolderName = cms.string('HLT/BTV/PFJet/PFJet80')
PFJet80.nmuons = cms.uint32(0)
PFJet80.nelectrons = cms.uint32(0)
PFJet80.njets = cms.uint32(1)
PFJet80.jetSelection = cms.string('pt>70 & abs(eta)<2.4')
PFJet80.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet80_v*')
PFJet80.histoPSet.jetPtBinning = cms.vdouble(0,70,75,80,85,90,100,120,150,200,400,700,1000,1500,3000)

PFJet140 = hltBTVmonitoring.clone()
PFJet140.FolderName = cms.string('HLT/BTV/PFJet/PFJet140')
PFJet140.nmuons = cms.uint32(0)
PFJet140.nelectrons = cms.uint32(0)
PFJet140.njets = cms.uint32(1)
PFJet140.jetSelection = cms.string('pt>120 & abs(eta)<2.4')
PFJet140.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet140_v*')
PFJet140.histoPSet.jetPtBinning = cms.vdouble(0,120,130,140,150,160,170,200,400,700,1000,1500,3000)

PFJet200 = hltBTVmonitoring.clone()
PFJet200.FolderName = cms.string('HLT/BTV/PFJet/PFJet200')
PFJet200.nmuons = cms.uint32(0)
PFJet200.nelectrons = cms.uint32(0)
PFJet200.njets = cms.uint32(1)
PFJet200.jetSelection = cms.string('pt>170 & abs(eta)<2.4')
PFJet200.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet200_v*')
PFJet200.histoPSet.jetPtBinning = cms.vdouble(0,170,180,190,200,210,220,250,300,400,700,1000,1500,3000)

PFJet260 = hltBTVmonitoring.clone()
PFJet260.FolderName = cms.string('HLT/BTV/PFJet/PFJet260')
PFJet260.nmuons = cms.uint32(0)
PFJet260.nelectrons = cms.uint32(0)
PFJet260.njets = cms.uint32(1)
PFJet260.jetSelection = cms.string('pt>220 & abs(eta)<2.4')
PFJet260.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet260_v*')
PFJet260.histoPSet.jetPtBinning = cms.vdouble(0,220,240,260,280,300,350,400,700,1000,1500,3000)

PFJet320 = hltBTVmonitoring.clone()
PFJet320.FolderName = cms.string('HLT/BTV/PFJet/PFJet320')
PFJet320.nmuons = cms.uint32(0)
PFJet320.nelectrons = cms.uint32(0)
PFJet320.njets = cms.uint32(1)
PFJet320.jetSelection = cms.string('pt>280 & abs(eta)<2.4')
PFJet320.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet320_v*')
PFJet320.histoPSet.jetPtBinning = cms.vdouble(0,280,300,320,340,360,400,500,700,1000,1500,3000)

PFJet400 = hltBTVmonitoring.clone()
PFJet400.FolderName = cms.string('HLT/BTV/PFJet/PFJet400')
PFJet400.nmuons = cms.uint32(0)
PFJet400.nelectrons = cms.uint32(0)
PFJet400.njets = cms.uint32(1)
PFJet400.jetSelection = cms.string('pt>350 & abs(eta)<2.4')
PFJet400.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet400_v*')
PFJet400.histoPSet.jetPtBinning = cms.vdouble(0,350,380,400,420,450,500,700,1000,1500,3000)

PFJet450 = hltBTVmonitoring.clone()
PFJet450.FolderName = cms.string('HLT/BTV/PFJet/PFJet450')
PFJet450.nmuons = cms.uint32(0)
PFJet450.nelectrons = cms.uint32(0)
PFJet450.njets = cms.uint32(1)
PFJet450.jetSelection = cms.string('pt>400 & abs(eta)<2.4')
PFJet450.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet450_v*')
PFJet450.histoPSet.jetPtBinning = cms.vdouble(0,400,430,450,470,500,700,1000,1500,3000)

PFJet500 = hltBTVmonitoring.clone()
PFJet500.FolderName = cms.string('HLT/BTV/PFJet/PFJet500')
PFJet500.nmuons = cms.uint32(0)
PFJet500.nelectrons = cms.uint32(0)
PFJet500.njets = cms.uint32(1)
PFJet500.jetSelection = cms.string('pt>450 & abs(eta)<2.4')
PFJet500.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet500_v*')
PFJet500.histoPSet.jetPtBinning = cms.vdouble(0,450,480,500,520,550,600,700,1000,1500,3000)

PFJet550 = hltBTVmonitoring.clone()
PFJet550.FolderName = cms.string('HLT/BTV/PFJet/PFJet550')
PFJet550.nmuons = cms.uint32(0)
PFJet550.nelectrons = cms.uint32(0)
PFJet550.njets = cms.uint32(1)
PFJet550.jetSelection = cms.string('pt>500 & abs(eta)<2.4')
PFJet550.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet550_v*')
PFJet550.histoPSet.jetPtBinning = cms.vdouble(0,500,520,550,600,700,1000,1500,3000)

#PFJet AK8
AK8PFJet40 = hltBTVmonitoring.clone()
AK8PFJet40.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet40')
AK8PFJet40.nmuons = cms.uint32(0)
AK8PFJet40.nelectrons = cms.uint32(0)
AK8PFJet40.njets = cms.uint32(1)
AK8PFJet40.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet40.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
AK8PFJet40.bjetSelection = cms.string('pt>20 & abs(eta)<2.4')
AK8PFJet40.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet40_v*')
AK8PFJet40.histoPSet.jetPtBinning = cms.vdouble(0,30,35,40,45,50,60,70,100,150,200,400,700,1000,1500,3000)

AK8PFJet60 = hltBTVmonitoring.clone()
AK8PFJet60.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet60')
AK8PFJet60.nmuons = cms.uint32(0)
AK8PFJet60.nelectrons = cms.uint32(0)
AK8PFJet60.njets = cms.uint32(1)
AK8PFJet60.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet60.jetSelection = cms.string('pt>50 & abs(eta)<2.4')
AK8PFJet60.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet60_v*')
AK8PFJet60.histoPSet.jetPtBinning = cms.vdouble(0,50,55,60,65,70,80,90,100,120,150,200,400,700,1000,1500,3000)

AK8PFJet80 = hltBTVmonitoring.clone()
AK8PFJet80.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet80')
AK8PFJet80.nmuons = cms.uint32(0)
AK8PFJet80.nelectrons = cms.uint32(0)
AK8PFJet80.njets = cms.uint32(1)
AK8PFJet80.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet80.jetSelection = cms.string('pt>70 & abs(eta)<2.4')
AK8PFJet80.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet80_v*')
AK8PFJet80.histoPSet.jetPtBinning = cms.vdouble(0,70,75,80,85,90,100,120,150,200,400,700,1000,1500,3000)

AK8PFJet140 = hltBTVmonitoring.clone()
AK8PFJet140.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet140')
AK8PFJet140.nmuons = cms.uint32(0)
AK8PFJet140.nelectrons = cms.uint32(0)
AK8PFJet140.njets = cms.uint32(1)
AK8PFJet140.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet140.jetSelection = cms.string('pt>120 & abs(eta)<2.4')
AK8PFJet140.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet140_v*')
AK8PFJet140.histoPSet.jetPtBinning = cms.vdouble(0,120,130,140,150,160,170,200,400,700,1000,1500,3000)

AK8PFJet200 = hltBTVmonitoring.clone()
AK8PFJet200.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet200')
AK8PFJet200.nmuons = cms.uint32(0)
AK8PFJet200.nelectrons = cms.uint32(0)
AK8PFJet200.njets = cms.uint32(1)
AK8PFJet200.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet200.jetSelection = cms.string('pt>170 & abs(eta)<2.4')
AK8PFJet200.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet200_v*')
AK8PFJet200.histoPSet.jetPtBinning = cms.vdouble(0,170,180,190,200,210,220,250,300,400,700,1000,1500,3000)

AK8PFJet260 = hltBTVmonitoring.clone()
AK8PFJet260.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet260')
AK8PFJet260.nmuons = cms.uint32(0)
AK8PFJet260.nelectrons = cms.uint32(0)
AK8PFJet260.njets = cms.uint32(1)
AK8PFJet260.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet260.jetSelection = cms.string('pt>220 & abs(eta)<2.4')
AK8PFJet260.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet260_v*')
AK8PFJet260.histoPSet.jetPtBinning = cms.vdouble(0,220,240,260,280,300,350,400,700,1000,1500,3000)

AK8PFJet320 = hltBTVmonitoring.clone()
AK8PFJet320.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet320')
AK8PFJet320.nmuons = cms.uint32(0)
AK8PFJet320.nelectrons = cms.uint32(0)
AK8PFJet320.njets = cms.uint32(1)
AK8PFJet320.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet320.jetSelection = cms.string('pt>280 & abs(eta)<2.4')
AK8PFJet320.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet320_v*')
AK8PFJet320.histoPSet.jetPtBinning = cms.vdouble(0,280,300,320,340,360,400,500,700,1000,1500,3000)

AK8PFJet400 = hltBTVmonitoring.clone()
AK8PFJet400.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet400')
AK8PFJet400.nmuons = cms.uint32(0)
AK8PFJet400.nelectrons = cms.uint32(0)
AK8PFJet400.njets = cms.uint32(1)
AK8PFJet400.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet400.jetSelection = cms.string('pt>350 & abs(eta)<2.4')
AK8PFJet400.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet400_v*')
AK8PFJet400.histoPSet.jetPtBinning = cms.vdouble(0,350,380,400,420,450,500,700,1000,1500,3000)

AK8PFJet450 = hltBTVmonitoring.clone()
AK8PFJet450.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet450')
AK8PFJet450.nmuons = cms.uint32(0)
AK8PFJet450.nelectrons = cms.uint32(0)
AK8PFJet450.njets = cms.uint32(1)
AK8PFJet450.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet450.jetSelection = cms.string('pt>400 & abs(eta)<2.4')
AK8PFJet450.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet450_v*')
AK8PFJet450.histoPSet.jetPtBinning = cms.vdouble(0,400,430,450,470,500,700,1000,1500,3000)

AK8PFJet500 = hltBTVmonitoring.clone()
AK8PFJet500.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet500')
AK8PFJet500.nmuons = cms.uint32(0)
AK8PFJet500.nelectrons = cms.uint32(0)
AK8PFJet500.njets = cms.uint32(1)
AK8PFJet500.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet500.jetSelection = cms.string('pt>450 & abs(eta)<2.4')
AK8PFJet500.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet500_v*')
AK8PFJet500.histoPSet.jetPtBinning = cms.vdouble(0,450,480,500,520,550,600,700,1000,1500,3000)

AK8PFJet550 = hltBTVmonitoring.clone()
AK8PFJet550.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJet550')
AK8PFJet550.nmuons = cms.uint32(0)
AK8PFJet550.nelectrons = cms.uint32(0)
AK8PFJet550.njets = cms.uint32(1)
AK8PFJet550.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJet550.jetSelection = cms.string('pt>500 & abs(eta)<2.4')
AK8PFJet550.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJet550_v*')
AK8PFJet550.histoPSet.jetPtBinning = cms.vdouble(0,500,520,550,600,700,1000,1500,3000)



#PFJetFwd AK4
PFJetFwd40 = hltBTVmonitoring.clone()
PFJetFwd40.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd40')
PFJetFwd40.nmuons = cms.uint32(0)
PFJetFwd40.nelectrons = cms.uint32(0)
PFJetFwd40.njets = cms.uint32(1)
PFJetFwd40.jetSelection = cms.string('pt>30 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd40.bjetSelection = cms.string('pt>20 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd40.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd40_v*')
PFJetFwd40.histoPSet.jetPtBinning = cms.vdouble(0,30,35,40,45,50,60,70,100,150,200,400,700,1000,1500,3000)

PFJetFwd60 = hltBTVmonitoring.clone()
PFJetFwd60.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd60')
PFJetFwd60.nmuons = cms.uint32(0)
PFJetFwd60.nelectrons = cms.uint32(0)
PFJetFwd60.njets = cms.uint32(1)
PFJetFwd60.jetSelection = cms.string('pt>50 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd60.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd60_v*')
PFJetFwd60.histoPSet.jetPtBinning = cms.vdouble(0,50,55,60,65,70,80,90,100,120,150,200,400,700,1000,1500,3000)

PFJetFwd80 = hltBTVmonitoring.clone()
PFJetFwd80.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd80')
PFJetFwd80.nmuons = cms.uint32(0)
PFJetFwd80.nelectrons = cms.uint32(0)
PFJetFwd80.njets = cms.uint32(1)
PFJetFwd80.jetSelection = cms.string('pt>70 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd80.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd80_v*')
PFJetFwd80.histoPSet.jetPtBinning = cms.vdouble(0,70,75,80,85,90,100,120,150,200,400,700,1000,1500,3000)

PFJetFwd140 = hltBTVmonitoring.clone()
PFJetFwd140.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd140')
PFJetFwd140.nmuons = cms.uint32(0)
PFJetFwd140.nelectrons = cms.uint32(0)
PFJetFwd140.njets = cms.uint32(1)
PFJetFwd140.jetSelection = cms.string('pt>120 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd140.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd140_v*')
PFJetFwd140.histoPSet.jetPtBinning = cms.vdouble(0,120,130,140,150,160,170,200,400,700,1000,1500,3000)

PFJetFwd200 = hltBTVmonitoring.clone()
PFJetFwd200.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd200')
PFJetFwd200.nmuons = cms.uint32(0)
PFJetFwd200.nelectrons = cms.uint32(0)
PFJetFwd200.njets = cms.uint32(1)
PFJetFwd200.jetSelection = cms.string('pt>170 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd200.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd200_v*')
PFJetFwd200.histoPSet.jetPtBinning = cms.vdouble(0,170,180,190,200,210,220,250,300,400,700,1000,1500,3000)

PFJetFwd260 = hltBTVmonitoring.clone()
PFJetFwd260.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd260')
PFJetFwd260.nmuons = cms.uint32(0)
PFJetFwd260.nelectrons = cms.uint32(0)
PFJetFwd260.njets = cms.uint32(1)
PFJetFwd260.jetSelection = cms.string('pt>220 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd260.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd260_v*')
PFJetFwd260.histoPSet.jetPtBinning = cms.vdouble(0,220,240,260,280,300,350,400,700,1000,1500,3000)

PFJetFwd320 = hltBTVmonitoring.clone()
PFJetFwd320.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd320')
PFJetFwd320.nmuons = cms.uint32(0)
PFJetFwd320.nelectrons = cms.uint32(0)
PFJetFwd320.njets = cms.uint32(1)
PFJetFwd320.jetSelection = cms.string('pt>280 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd320.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd320_v*')
PFJetFwd320.histoPSet.jetPtBinning = cms.vdouble(0,280,300,320,340,360,400,500,700,1000,1500,3000)

PFJetFwd400 = hltBTVmonitoring.clone()
PFJetFwd400.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd400')
PFJetFwd400.nmuons = cms.uint32(0)
PFJetFwd400.nelectrons = cms.uint32(0)
PFJetFwd400.njets = cms.uint32(1)
PFJetFwd400.jetSelection = cms.string('pt>350 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd400.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd400_v*')
PFJetFwd400.histoPSet.jetPtBinning = cms.vdouble(0,350,380,400,420,450,500,700,1000,1500,3000)

PFJetFwd450 = hltBTVmonitoring.clone()
PFJetFwd450.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd450')
PFJetFwd450.nmuons = cms.uint32(0)
PFJetFwd450.nelectrons = cms.uint32(0)
PFJetFwd450.njets = cms.uint32(1)
PFJetFwd450.jetSelection = cms.string('pt>400 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd450.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd450_v*')
PFJetFwd450.histoPSet.jetPtBinning = cms.vdouble(0,400,430,450,470,500,700,1000,1500,3000)

PFJetFwd500 = hltBTVmonitoring.clone()
PFJetFwd500.FolderName = cms.string('HLT/BTV/PFJet/PFJetFwd500')
PFJetFwd500.nmuons = cms.uint32(0)
PFJetFwd500.nelectrons = cms.uint32(0)
PFJetFwd500.njets = cms.uint32(1)
PFJetFwd500.jetSelection = cms.string('pt>450 & abs(eta)>2.7 & abs(eta)<5.0')
PFJetFwd500.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJetFwd500_v*')
PFJetFwd500.histoPSet.jetPtBinning = cms.vdouble(0,450,480,500,520,550,600,700,1000,1500,3000)


#PFJetFwd AK8
AK8PFJetFwd40 = hltBTVmonitoring.clone()
AK8PFJetFwd40.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd40')
AK8PFJetFwd40.nmuons = cms.uint32(0)
AK8PFJetFwd40.nelectrons = cms.uint32(0)
AK8PFJetFwd40.njets = cms.uint32(1)
AK8PFJetFwd40.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd40.jetSelection = cms.string('pt>30 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd40.bjetSelection = cms.string('pt>20 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd40.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd40_v*')
AK8PFJetFwd40.histoPSet.jetPtBinning = cms.vdouble(0,30,35,40,45,50,60,70,100,150,200,400,700,1000,1500,3000)

AK8PFJetFwd60 = hltBTVmonitoring.clone()
AK8PFJetFwd60.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd60')
AK8PFJetFwd60.nmuons = cms.uint32(0)
AK8PFJetFwd60.nelectrons = cms.uint32(0)
AK8PFJetFwd60.njets = cms.uint32(1)
AK8PFJetFwd60.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd60.jetSelection = cms.string('pt>50 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd60.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd60_v*')
AK8PFJetFwd60.histoPSet.jetPtBinning = cms.vdouble(0,50,55,60,65,70,80,90,100,120,150,200,400,700,1000,1500,3000)

AK8PFJetFwd80 = hltBTVmonitoring.clone()
AK8PFJetFwd80.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd80')
AK8PFJetFwd80.nmuons = cms.uint32(0)
AK8PFJetFwd80.nelectrons = cms.uint32(0)
AK8PFJetFwd80.njets = cms.uint32(1)
AK8PFJetFwd80.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd80.jetSelection = cms.string('pt>70 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd80.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd80_v*')
AK8PFJetFwd80.histoPSet.jetPtBinning = cms.vdouble(0,70,75,80,85,90,100,120,150,200,400,700,1000,1500,3000)

AK8PFJetFwd140 = hltBTVmonitoring.clone()
AK8PFJetFwd140.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd140')
AK8PFJetFwd140.nmuons = cms.uint32(0)
AK8PFJetFwd140.nelectrons = cms.uint32(0)
AK8PFJetFwd140.njets = cms.uint32(1)
AK8PFJetFwd140.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd140.jetSelection = cms.string('pt>120 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd140.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd140_v*')
AK8PFJetFwd140.histoPSet.jetPtBinning = cms.vdouble(0,120,130,140,150,160,170,200,400,700,1000,1500,3000)

AK8PFJetFwd200 = hltBTVmonitoring.clone()
AK8PFJetFwd200.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd200')
AK8PFJetFwd200.nmuons = cms.uint32(0)
AK8PFJetFwd200.nelectrons = cms.uint32(0)
AK8PFJetFwd200.njets = cms.uint32(1)
AK8PFJetFwd200.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd200.jetSelection = cms.string('pt>170 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd200.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd200_v*')
AK8PFJetFwd200.histoPSet.jetPtBinning = cms.vdouble(0,170,180,190,200,210,220,250,300,400,700,1000,1500,3000)

AK8PFJetFwd260 = hltBTVmonitoring.clone()
AK8PFJetFwd260.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd260')
AK8PFJetFwd260.nmuons = cms.uint32(0)
AK8PFJetFwd260.nelectrons = cms.uint32(0)
AK8PFJetFwd260.njets = cms.uint32(1)
AK8PFJetFwd260.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd260.jetSelection = cms.string('pt>220 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd260.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd260_v*')
AK8PFJetFwd260.histoPSet.jetPtBinning = cms.vdouble(0,220,240,260,280,300,350,400,700,1000,1500,3000)

AK8PFJetFwd320 = hltBTVmonitoring.clone()
AK8PFJetFwd320.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd320')
AK8PFJetFwd320.nmuons = cms.uint32(0)
AK8PFJetFwd320.nelectrons = cms.uint32(0)
AK8PFJetFwd320.njets = cms.uint32(1)
AK8PFJetFwd320.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd320.jetSelection = cms.string('pt>280 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd320.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd320_v*')
AK8PFJetFwd320.histoPSet.jetPtBinning = cms.vdouble(0,280,300,320,340,360,400,500,700,1000,1500,3000)

AK8PFJetFwd400 = hltBTVmonitoring.clone()
AK8PFJetFwd400.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd400')
AK8PFJetFwd400.nmuons = cms.uint32(0)
AK8PFJetFwd400.nelectrons = cms.uint32(0)
AK8PFJetFwd400.njets = cms.uint32(1)
AK8PFJetFwd400.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd400.jetSelection = cms.string('pt>350 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd400.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd400_v*')
AK8PFJetFwd400.histoPSet.jetPtBinning = cms.vdouble(0,350,380,400,420,450,500,700,1000,1500,3000)

AK8PFJetFwd450 = hltBTVmonitoring.clone()
AK8PFJetFwd450.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd450')
AK8PFJetFwd450.nmuons = cms.uint32(0)
AK8PFJetFwd450.nelectrons = cms.uint32(0)
AK8PFJetFwd450.njets = cms.uint32(1)
AK8PFJetFwd450.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd450.jetSelection = cms.string('pt>400 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd450.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd450_v*')
AK8PFJetFwd450.histoPSet.jetPtBinning = cms.vdouble(0,400,430,450,470,500,700,1000,1500,3000)

AK8PFJetFwd500 = hltBTVmonitoring.clone()
AK8PFJetFwd500.FolderName = cms.string('HLT/BTV/PFJet/AK8PFJetFwd500')
AK8PFJetFwd500.nmuons = cms.uint32(0)
AK8PFJetFwd500.nelectrons = cms.uint32(0)
AK8PFJetFwd500.njets = cms.uint32(1)
AK8PFJetFwd500.jets = cms.InputTag("ak8PFJetsCHS")
AK8PFJetFwd500.jetSelection = cms.string('pt>450 & abs(eta)>2.7 & abs(eta)<5.0')
AK8PFJetFwd500.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_AK8PFJetFwd500_v*')
AK8PFJetFwd500.histoPSet.jetPtBinning = cms.vdouble(0,450,480,500,520,550,600,700,1000,1500,3000)


btagMonitorHLT = cms.Sequence(
    BTagMu_AK4DiJet20_Mu5
    + BTagMu_AK4DiJet40_Mu5
    + BTagMu_AK4DiJet70_Mu5
    + BTagMu_AK4DiJet110_Mu5    
    + BTagMu_AK4DiJet170_Mu5
    + BTagMu_AK4Jet300_Mu5
    + BTagMu_AK8DiJet170_Mu5
    + BTagMu_AK8Jet300_Mu5
    + PFJet40
    + PFJet60
    + PFJet80
    + PFJet140
    + PFJet200
    + PFJet260
    + PFJet320
    + PFJet400
    + PFJet450
    + PFJet500
    + PFJet550
    + AK8PFJet40
    + AK8PFJet60
    + AK8PFJet80
    + AK8PFJet140
    + AK8PFJet200
    + AK8PFJet260
    + AK8PFJet320
    + AK8PFJet400
    + AK8PFJet450
    + AK8PFJet500
    + AK8PFJet550
    + PFJetFwd40
    + PFJetFwd60
    + PFJetFwd80
    + PFJetFwd140
    + PFJetFwd200
    + PFJetFwd260
    + PFJetFwd320
    + PFJetFwd400
    + PFJetFwd450
    + PFJetFwd500
    + AK8PFJetFwd40
    + AK8PFJetFwd60
    + AK8PFJetFwd80
    + AK8PFJetFwd140
    + AK8PFJetFwd200
    + AK8PFJetFwd260
    + AK8PFJetFwd320
    + AK8PFJetFwd400
    + AK8PFJetFwd450
    + AK8PFJetFwd500
)

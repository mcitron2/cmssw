import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")


process.MessageLogger = cms.Service(
        "MessageLogger",
            categories = cms.untracked.vstring('info', 'debug','cout')
            )

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)


# source
process.source = cms.Source("PoolSource", 
     #fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/user/r/rompotis/RedigiSummer08RootTrees/WenuRedigi_RECO_SAMPLE.root')
     fileNames = cms.untracked.vstring(
    'file:zee_Summer09-MC_31X_V3_AODSIM_v1_AODSIM.root'
    #'file:/tmp/rompotis/Run123505_LS70-80_BscMinBiasInnerThreshold.root',
    )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Load additional processes
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
## global tags:
## >>>> to run with data
# process.GlobalTag.globaltag = cms.string('GR09_P_V7::All')
## >>>> to run MC summer09 production
process.GlobalTag.globaltag = cms.string('MC_31X_V5::All')
#process.GlobalTag.globaltag = cms.string('STARTUP31X_V4::All')
process.load("Configuration.StandardSequences.MagneticField_cff")


################################################################################################
###    P r e p a r a t i o n      o f    t h e    P A T    O b j e c t s   f r o m    A O D  ###
################################################################################################

## pat sequences to be loaded:
process.load("PhysicsTools.PFCandProducer.PF2PAT_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")
#process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
##
#
# for ecal isolation: set the correct name of the ECAL rechit collection
# 
process.eleIsoDepositEcalFromHits.ExtractorPSet.barrelEcalHits = cms.InputTag("reducedEcalRecHitsEB", "", "RECO")
process.eleIsoDepositEcalFromHits.ExtractorPSet.endcapEcalHits = cms.InputTag("reducedEcalRecHitsEE", "", "RECO")
#
#
process.eidRobustHighEnergy.reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB", "", "RECO")
process.eidRobustHighEnergy.reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE", "", "RECO")     
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## CHOICE OF THE HLT PATH     this section is not used from PAT
##                            
## Define here as string the names of the triggers only once
## please consult the table of the available triggers at the end of this file
# trigger menu selection
##
#process.patTrigger.processName = cms.string(HLT_process_name)  
#process.patTriggerMatcher = cms.Sequence(process.patTriggerElectronMatcher)
#process.electronTriggerMatchHltElectrons.pathNames = cms.vstring(HLT_path_name)
#process.patTriggerMatchEmbedder = cms.Sequence(process.cleanLayer1ElectronsTriggerMatch)
#process.patTriggerSequence = cms.Sequence(process.patTrigger*process.patTriggerMatcher*
#                                          process.patTriggerMatchEmbedder)
##
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## MET creation     <=== WARNING: YOU MAY WANT TO MODIFY THIS PART OF THE CODE       %%%%%%%%%%%%%
##                                specify the names of the MET collections that you need here %%%%
##                                                                                             #%%
## if you don't specify anything the default MET is the raw Calo MET                           #%%
process.layer1RawCaloMETs = process.layer1METs.clone(                                          #%%
    metSource = cms.InputTag("met"),
    addTrigMatch = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addGenMET = cms.bool(False),
    )
## specify here what you want to have on the plots! <===== MET THAT YOU WANT ON THE PLOTS  %%%%%%%
myDesiredMetCollection = 'layer1RawCaloMETs'
## modify the sequence of the MET creation:                                                    #%%
process.makeLayer1METs = cms.Sequence(process.layer1RawCaloMETs)
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## modify the final pat sequence: keep only electrons + METS (muons are needed for met corrections)
process.load("RecoEgamma.EgammaIsolationAlgos.egammaIsolationSequence_cff")
process.electronEcalRecHitIsolationLcone.ecalBarrelRecHitProducer = cms.InputTag("reducedEcalRecHitsEB")
process.electronEcalRecHitIsolationScone.ecalBarrelRecHitProducer = cms.InputTag("reducedEcalRecHitsEB")
process.electronEcalRecHitIsolationLcone.ecalEndcapRecHitProducer = cms.InputTag("reducedEcalRecHitsEE")
process.electronEcalRecHitIsolationScone.ecalEndcapRecHitProducer = cms.InputTag("reducedEcalRecHitsEE")
#
process.electronEcalRecHitIsolationLcone.ecalBarrelRecHitCollection = cms.InputTag("")
process.electronEcalRecHitIsolationScone.ecalBarrelRecHitCollection = cms.InputTag("")
process.electronEcalRecHitIsolationLcone.ecalEndcapRecHitCollection = cms.InputTag("")
process.electronEcalRecHitIsolationScone.ecalEndcapRecHitCollection = cms.InputTag("")
#
#
process.patElectronIsolation = cms.Sequence(process.egammaIsolationSequence)
process.allLayer1Electrons.userIsolation = cms.PSet(
    tracker = cms.PSet(
      src = cms.InputTag("electronTrackIsolationScone"),
    ),
    ecal = cms.PSet(
      src = cms.InputTag("electronEcalRecHitIsolationLcone"),
    ),
    hcal = cms.PSet(
      src = cms.InputTag("electronHcalTowerIsolationLcone"),
    ),
    )
process.allLayer1Electrons.isoDeposits = cms.PSet()
process.allLayer1Electrons.addElectronID = cms.bool(False)
process.allLayer1Electrons.electronIDSources = cms.PSet()
process.allLayer1Electrons.addGenMatch = cms.bool(False)
process.allLayer1Electrons.embedGenMatch = cms.bool(False)
process.allLayer1Electrons.embedHighLevelSelection = cms.bool(False)
##
process.allLayer1Muons.addGenMatch = cms.bool(False)
process.allLayer1Muons.embedGenMatch = cms.bool(False)
##
process.makeAllLayer1Electrons = cms.Sequence(process.patElectronIsolation*process.allLayer1Electrons)
process.makeAllLayer1Muons = cms.Sequence(process.allLayer1Muons)
#
process.allLayer1Objects = cms.Sequence(process.makeAllLayer1Electrons+process.makeAllLayer1Muons+process.makeLayer1METs)
process.selectedLayer1Objects = cms.Sequence(process.selectedLayer1Electrons+process.selectedLayer1Muons)
process.cleanLayer1Objects  = cms.Sequence(process.cleanLayer1Muons*process.cleanLayer1Electrons)
process.countLayer1Objects  = cms.Sequence(process.countLayer1Electrons+process.countLayer1Muons)

process.patDefaultSequence = cms.Sequence(process.allLayer1Objects * process.selectedLayer1Objects *
                                          process.cleanLayer1Objects*process.countLayer1Objects
                                          )

##  ################################################################################
##
##  the filter to select the candidates from the data samples
##
## WARNING: you may want to modify this item:  T R I G G E R     S E L E C T I O N
HLT_process_name = "HLT8E29"   # options: HLT or HLT8E29 >>>>>>> to run with summer09 samples
# HLT_process_name = "HLT"   # >>>>>>> to run with data
# trigger path selection
HLT_path_name    = "HLT_Ele15_LW_L1R"
# trigger filter name
HLT_filter_name  =  "hltL1NonIsoHLTNonIsoSingleElectronLWEt15PixelMatchFilter"
#
process.zeeFilter = cms.EDFilter('ZeeCandidateFilter',
                                 # cuts
                                 ETCut = cms.untracked.double(20.),
                                 METCut = cms.untracked.double(0.),
                                 useTriggerInfo = cms.untracked.bool(False),
                                 # trigger
                                 triggerCollectionTag = cms.untracked.InputTag("TriggerResults","",HLT_process_name),
                                 triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLT_process_name),
                                 hltpath = cms.untracked.string(HLT_path_name),
                                 hltpathFilter = cms.untracked.InputTag(HLT_filter_name,"",HLT_process_name),
                                 electronMatched2HLT = cms.untracked.bool(True),
                                 electronMatched2HLT_DR = cms.untracked.double(0.2),
                                 # electrons and MET
                                 electronCollectionTag = cms.untracked.InputTag("selectedLayer1Electrons","","PAT"),
                                 metCollectionTag = cms.untracked.InputTag(myDesiredMetCollection,"","PAT")
                                 )
####################################################################################
##
## the Z selection that you prefer
selection_a2 = cms.PSet (
    trackIso_EB = cms.untracked.double(7.2),
    ecalIso_EB = cms.untracked.double(5.7),
    hcalIso_EB = cms.untracked.double(8.1),
    sihih_EB = cms.untracked.double(0.01),
    dphi_EB = cms.untracked.double(1000.),
    deta_EB = cms.untracked.double(0.0071),
    hoe_EB = cms.untracked.double(1000),
    
    trackIso_EE = cms.untracked.double(5.1),
    ecalIso_EE = cms.untracked.double(5.0),
    hcalIso_EE = cms.untracked.double(3.4),
    sihih_EE = cms.untracked.double(0.028),
    dphi_EE = cms.untracked.double(1000.),
    deta_EE = cms.untracked.double(0.0066),
    hoe_EE = cms.untracked.double(1000.)
    )

selection_inverse = cms.PSet (
    trackIso_EB_inv = cms.untracked.bool(True),
    trackIso_EE_inv = cms.untracked.bool(True)
    )
selection_secondLeg = cms.PSet (
    ## set this to true if you want to switch on diff 2nd leg selection
    useDifferentSecondLegSelection = cms.untracked.bool(True),
    ##
    trackIso2_EB = cms.untracked.double(7.2),
    ecalIso2_EB = cms.untracked.double(5.7),
    hcalIso2_EB = cms.untracked.double(8.1),
    sihih2_EB = cms.untracked.double(0.01),
    dphi2_EB = cms.untracked.double(1000.),
    deta2_EB = cms.untracked.double(0.0071),
    hoe2_EB = cms.untracked.double(1000),
    
    trackIso2_EE = cms.untracked.double(5.1),
    ecalIso2_EE = cms.untracked.double(5.0),
    hcalIso2_EE = cms.untracked.double(3.4),
    sihih2_EE = cms.untracked.double(0.028),
    dphi2_EE = cms.untracked.double(1000.),
    deta2_EE = cms.untracked.double(0.0066),
    hoe2_EE = cms.untracked.double(1000.)
    )

####################################################################################
##
## and the plot creator
process.plotter = cms.EDAnalyzer('ZeePlots',
                                 selection_a2,
                                 selection_secondLeg,
                                 zeeCollectionTag = cms.untracked.InputTag("zeeFilter","selectedZeeCandidates","PAT")
                                 )




process.p = cms.Path(process.patDefaultSequence +process.zeeFilter + process.plotter)



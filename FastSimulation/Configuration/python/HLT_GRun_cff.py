# /dev/CMSSW_3_11_0/GRun/V16 (CMSSW_3_11_0_HLT18)

import FWCore.ParameterSet.Config as cms
from FastSimulation.HighLevelTrigger.HLTSetup_cff import *


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_11_0/GRun/V16')
)

hltESSBTagRecord = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "JetTagComputerRecord" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
hltESSMCJetCorrectorIcone5HF07 = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2Relative" ),
  algorithm = cms.string( "" ),
  section = cms.string( "" ),
  era = cms.string( "HLT" )
)
hltESSMCJetCorrectorIcone5Unit = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2RelativeFlat" ),
  algorithm = cms.string( "" ),
  section = cms.string( "" ),
  era = cms.string( "HLT" )
)

AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  ComponentName = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet( 
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    tccUnpacking = cms.bool( False ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    feIdCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    forceKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
  ),
  ElectronicsMapper = cms.PSet( 
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  ),
  UncalibRHAlgo = cms.PSet(  Type = cms.string( "EcalUncalibRecHitWorkerWeights" ) ),
  CalibRHAlgo = cms.PSet( 
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 6, 6, 6, 7, 8 ),
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    killDeadChannels = cms.bool( True ),
    ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14, 78, 142 ),
    laserCorrection = cms.bool( False )
  )
)
HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
XMLFromDBSource = cms.ESProducer( "XMLIdealGeometryESProducer",
  rootDDName = cms.string( "cms:OCMS" ),
  label = cms.string( "Extended" ),
  appendToDataLabel = cms.string( "" )
)
ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( '' ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  Level = cms.int32( 1 ),
      RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' )
    ),
    cms.PSet(  Level = cms.int32( 5 ),
      RecHitFlags = cms.vstring( 'HSCP_R1R2',
        'HSCP_FracLeader',
        'HSCP_OuterEnergy',
        'HSCP_ExpFit',
        'ADCSaturationBit' ),
      ChannelStatus = cms.vstring( '' )
    ),
    cms.PSet(  Level = cms.int32( 8 ),
      RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
        'HBHEPulseShape',
        'HOBit',
        'HFDigiTime',
        'HFInTimeWindow',
        'HFS8S1Ratio',
        'ZDCBit',
        'CalibrationBit',
        'TimingErrorBit' ),
      ChannelStatus = cms.vstring( '' )
    ),
    cms.PSet(  Level = cms.int32( 11 ),
      RecHitFlags = cms.vstring( 'HFLongShort' ),
      ChannelStatus = cms.vstring( '' )
    ),
    cms.PSet(  Level = cms.int32( 12 ),
      RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' )
    ),
    cms.PSet(  Level = cms.int32( 15 ),
      RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( 'HcalCellHot' )
    ),
    cms.PSet(  Level = cms.int32( 20 ),
      RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' )
    )
  ),
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  appendToDataLabel = cms.string( "" ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" ),
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" ),
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
hltESPCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" ),
  appendToDataLabel = cms.string( "" )
)
hltESPESUnpackerWorker = cms.ESProducer( "ESUnpackerWorkerESProducer",
  ComponentName = cms.string( "hltESPESUnpackerWorker" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) ),
  RHAlgo = cms.PSet( 
    Type = cms.string( "ESRecHitWorker" ),
    ESRecoAlgo = cms.int32( 0 )
  )
)
hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  appendToDataLabel = cms.string( "" ),
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPHIPixelLayerPairs" ),
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPHIPixelLayerTriplets" ),
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" ),
  appendToDataLabel = cms.string( "" )
)
hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  HitMatcher = cms.string( "StandardMatcher" ),
  Regional = cms.bool( True ),
  OnDemand = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripModuleQualityDB = cms.bool( True ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  appendToDataLabel = cms.string( "" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  inactiveStripDetectorLabels = cms.VInputTag(  ),
  badStripCuts = cms.PSet( 
    TIB = cms.PSet( 
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    )
  )
)
hltESPMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPMixedLayerPairs" ),
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg',
    'FPix2_pos+TEC1_pos',
    'FPix2_pos+TEC2_pos',
    'TEC1_pos+TEC2_pos',
    'TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC1_neg',
    'FPix2_neg+TEC2_neg',
    'TEC1_neg+TEC2_neg',
    'TEC2_neg+TEC3_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  )
)
hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 1.0 )
  )
)
hltESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  useSeedLayer = cms.bool( False ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  appendToDataLabel = cms.string( "" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( False ),
  alwaysUseInvalidHits = cms.bool( True )
)
hltESPMuonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    chargeSignificance = cms.double( -1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
  appendToDataLabel = cms.string( "" )
)
hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  size_cutX = cms.double( 3.0 ),
  size_cutY = cms.double( 3.0 ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  inflate_errors = cms.bool( False ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  IrradiationBiasCorrection = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 )
)
hltESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerPairs" ),
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTriplets" ),
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPPixelLayerTripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHB" ),
  layerList = cms.vstring( 'BPix1+BPix2+BPix3' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPPixelLayerTripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHE" ),
  layerList = cms.vstring( 'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(  )
)
hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  appendToDataLabel = cms.string( "" )
)
hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  appendToDataLabel = cms.string( "" )
)
hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  appendToDataLabel = cms.string( "" ),
  distance = cms.double( 0.5 )
)
hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  appendToDataLabel = cms.string( "" ),
  ipSign = cms.string( "any" )
)
hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  appendToDataLabel = cms.string( "" )
)
hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  appendToDataLabel = cms.string( "" ),
  nthTrack = cms.int32( 2 ),
  impactParameterType = cms.int32( 0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  trackQualityClass = cms.string( "any" )
)
hltESPTrajectoryBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPTrajectoryBuilderL3" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterL3" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" ),
  fractionShared = cms.double( 0.5 ),
  allowSharedFirstHit = cms.bool( False )
)
hltESPTrajectoryFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPTrajectoryFilterL3" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 7 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
hltESPbJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 1.0 )
  )
)
hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer",
  appendToDataLabel = cms.string( "" )
)
sistripconn = cms.ESProducer( "SiStripConnectivity" )

DQMStore = cms.Service( "DQMStore",
)
DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
  getSCInfo = cms.untracked.bool( True ),
  processingMode = cms.untracked.string( "HLT" )
)

hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
hltL1sL1BscMinBiasORBptxPlusANDMinus = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BscMinBiasOR_BptxPlusANDMinus" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreActivityCSC = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltCSCActivityFilter = cms.EDFilter( "HLTCSCActivityFilter",
    cscStripDigiTag = cms.InputTag( 'simMuonCSCDigis','MuonCSCStripDigi' ),
    applyfilter = cms.bool( True ),
    skipStationRing = cms.bool( True ),
    skipRingNumber = cms.int32( 4 ),
    skipStationNumber = cms.int32( 1 )
)
hltL1sL1Jet6U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet6U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1Jet6U_BPTX = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1Jet10U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1Jet10U_BPTX = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1SingleJet6U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet6U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreJet15U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHitAll:EcalRecHitsEB','hltEcalRecHitAll:EcalRecHitsEE' )
)
hltIterativeCone5CaloJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltMCJetCorJetIcone5HF07 = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( "hltIterativeCone5CaloJets" ),
    verbose = cms.untracked.bool( False ),
    alias = cms.untracked.string( "MCJetCorJetIcone5" ),
    correctors = cms.vstring( 'hltESSMCJetCorrectorIcone5HF07' )
)
hlt1jet15U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sJet30U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet20U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreJet30U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet30U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sJet50U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreJet50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet50U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 50.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1SingleJet40U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet40U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreJet70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet70U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 70.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1SingleJet60U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet60U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreJet100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet100U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 100.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltPreJet140U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet140U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 140.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltPreJet180U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1jet180U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 180.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltPreDiJetAve15U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve15U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 15.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltL1sL1SingleJet20U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet20U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDiJetAve30U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve30U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 30.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltL1sL1SingleJet30U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDiJetAve50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve50U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 50.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltPreDiJetAve70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve70U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 70.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltPreDiJetAve100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve100U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 100.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltPreDiJetAve140U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJetAve140U = cms.EDFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    minPtAve = cms.double( 140.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( -1.0 )
)
hltL1sL1DoubleForJet10UEtaOpp = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet10U_EtaOpp" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDoubleJet15UForwardBackward = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltTowerMakerForJets = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRegionalJetsRecHit:EcalRecHitsEB','hltEcalRegionalJetsRecHit:EcalRecHitsEE' )
)
hltIterativeCone5CaloJetsRegional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( "hltTowerMakerForJets" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltDoubleJet15UForwardBackward = cms.EDFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
    saveTag = cms.untracked.bool( True ),
    minPt = cms.double( 15.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
hltPreDoubleJet25UForwardBackward = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDoubleJet25UForwardBackward = cms.EDFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
    saveTag = cms.untracked.bool( True ),
    minPt = cms.double( 25.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
hltPreDoubleJet35UForwardBackward = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDoubleJet35UForwardBackward = cms.EDFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
    saveTag = cms.untracked.bool( True ),
    minPt = cms.double( 35.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
hltL1sL1HTT50 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_HTT50" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDiJet20UMeff180U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJet20UMeff180U = cms.EDFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 2 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 180.0 ),
    minHt = cms.double( 0.0 ),
    minAlphaT = cms.double( 0.0 ),
    minPtJet = cms.vdouble( 20.0, 20.0 ),
    etaJet = cms.vdouble( 9999.0, 9999.0 )
)
hltPreDiJet50UPT50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiJet50UPT50U = cms.EDFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 3 ),
    usePt = cms.bool( False ),
    minPT12 = cms.double( 50.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minAlphaT = cms.double( 0.0 ),
    minPtJet = cms.vdouble( 50.0, 50.0 ),
    etaJet = cms.vdouble( 9999.0, 9999.0 )
)
hltPreExclDiJet30UHFAND = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltExclDiJet30UAND = cms.EDFilter( "HLTExclDiJetFilter",
    inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    minPtJet = cms.double( 30.0 ),
    minHFe = cms.double( 50.0 ),
    HF_OR = cms.bool( False )
)
hltPreExclDiJet30UHFOR = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltExclDiJet30UOR = cms.EDFilter( "HLTExclDiJetFilter",
    inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    minPtJet = cms.double( 30.0 ),
    minHFe = cms.double( 50.0 ),
    HF_OR = cms.bool( True )
)
hltL1sL1QuadJet8U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_QuadJet8U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreQuadJet15U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt4jet15U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 4 )
)
hltPreQuadJet20U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt4jet20U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 4 )
)
hltPreQuadJet25U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt4jet25U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 25.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 4 )
)
hltPreR010UMR50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltMet = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltTowerMakerForAll" ),
    InputType = cms.string( "CandidateCollection" ),
    METType = cms.string( "CaloMET" ),
    alias = cms.string( "RawCaloMET" ),
    globalThreshold = cms.double( 0.3 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltRHemisphere = cms.EDFilter( "HLTRHemisphere",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minJetPt = cms.double( 30.0 ),
    maxEta = cms.double( 3.0 ),
    maxNJ = cms.int32( 7 ),
    acceptNJ = cms.bool( True )
)
hltR010UMR50U = cms.EDFilter( "HLTRFilter",
    inputTag = cms.InputTag( "hltRHemisphere" ),
    inputMetTag = cms.InputTag( "hltMet" ),
    minR = cms.double( 0.1 ),
    minMR = cms.double( 50.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
hltPreR030UMR100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltR030UMR100U = cms.EDFilter( "HLTRFilter",
    inputTag = cms.InputTag( "hltRHemisphere" ),
    inputMetTag = cms.InputTag( "hltMet" ),
    minR = cms.double( 0.3 ),
    minMR = cms.double( 100.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
hltPreR033UMR100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltR033UMR100U = cms.EDFilter( "HLTRFilter",
    inputTag = cms.InputTag( "hltRHemisphere" ),
    inputMetTag = cms.InputTag( "hltMet" ),
    minR = cms.double( 0.3 ),
    minMR = cms.double( 100.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
hltPreRP025UMR70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltRP025UMR70U = cms.EDFilter( "HLTRFilter",
    inputTag = cms.InputTag( "hltRHemisphere" ),
    inputMetTag = cms.InputTag( "hltMet" ),
    minR = cms.double( 0.25 ),
    minMR = cms.double( 70.0 ),
    doRPrime = cms.bool( True ),
    acceptNJ = cms.bool( True )
)
hltL1sL1ETT100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETT100" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1ETT100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1ETT140 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETT140" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreEcalOnlySumEt160 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltTowerMakerForEcalBarrelOnly = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "" ),
    hoInput = cms.InputTag( "" ),
    hfInput = cms.InputTag( "" ),
    AllowMissingInputs = cms.bool( True ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHitAll:EcalRecHitsEB' )
)
hltEcalOnlyMet = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltTowerMakerForEcalBarrelOnly" ),
    InputType = cms.string( "CandidateCollection" ),
    METType = cms.string( "CaloMET" ),
    alias = cms.string( "RawCaloMET" ),
    globalThreshold = cms.double( 0.2 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hlt1EcalOnlySumET160 = cms.EDFilter( "HLTGlobalSumsCaloMET",
    inputTag = cms.InputTag( "hltEcalOnlyMet" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 160.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1MET20 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETM20" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1MET20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1ETM30 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETM30" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMET45 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1MET45 = cms.EDFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( "hltMet" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 45.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreMET45DiJet30U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt2jet30U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltPreMET65Jet50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1MET65 = cms.EDFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( "hltMet" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 65.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hlt1cenjet50U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 50.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 1 )
)
hltPreMET80Jet50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreMET100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1MET100 = cms.EDFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( "hltMet" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 100.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreMET120 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1MET120 = cms.EDFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( "hltMet" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 120.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1SingleJet10U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreHT50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltJet20UHt = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltHT50U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 50.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT100U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 100.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT130U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT130U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 130.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT140UJ30UEta3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltJetEta3Ht = cms.EDFilter( "CaloJetSelector",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    filter = cms.bool( False ),
    cut = cms.string( "abs(eta)<3" )
)
hltJet30UEta3Ht = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltJetEta3Ht" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 30.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltHT140UJ30Eta3 = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet30UEta3Ht" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 140.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT150U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT150U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 150.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT150UEta3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltJet20UEta3Ht = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltJetEta3Ht" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltHT150UEta3 = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UEta3Ht" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 150.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT160U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT160U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 160.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT160UEta3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT160UEta3 = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UEta3Ht" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 160.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreHT200U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT200U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 200.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1SingleMuOpen = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1MuOpen_BPTX = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1MuOpenL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpen" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
hltPreL1MuOpenDT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1MuOpenL1FilteredDT = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpen" ),
    MaxEta = cms.double( 1.25 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
hltL1sL1SingleMu7 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu7" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1Mu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1Mu7L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu7" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
hltL1sL1SingleMu20 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu20" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1Mu20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1Mu20L1Filtered20 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu20" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
hltL1sL1SingleMu0 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu0" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL2Mu0NoVertex = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu0L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu0" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    dtDigiLabel = cms.InputTag( "simMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    recAlgoConfig = cms.PSet( 
      debug = cms.untracked.bool( False ),
      minTime = cms.double( -3.0 ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet( 
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        tTrigLabel = cms.string( "" )
      ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" )
    )
)
hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgoConfig = cms.PSet( 
          debug = cms.untracked.bool( False ),
          minTime = cms.double( -3.0 ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet( 
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False ),
            tTrigLabel = cms.string( "" )
          ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" )
        ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgoConfig = cms.PSet( 
        debug = cms.untracked.bool( False ),
        minTime = cms.double( -3.0 ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet( 
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False ),
          tTrigLabel = cms.string( "" )
        ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False )
    )
)
hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    CSCUseCalibrations = cms.bool( True ),
    CSCUseStaticPedestals = cms.bool( False ),
    CSCUseTimingCorrections = cms.bool( True ),
    stripDigiTag = cms.InputTag( 'simMuonCSCDigis','MuonCSCStripDigi' ),
    wireDigiTag = cms.InputTag( 'simMuonCSCDigis','MuonCSCWireDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    XTasymmetry_ME1b = cms.double( 0.0 ),
    ConstSyst_ME1b = cms.double( 0.0070 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    readBadChannels = cms.bool( True ),
    readBadChambers = cms.bool( True ),
    UseAverageTime = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    UseFivePoleFit = cms.bool( True )
)
hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_type = cms.int32( 1 ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            BPMinImprovement = cms.double( 10000.0 ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            tanThetaMax = cms.double( 1.2 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            minHitsPerSegment = cms.int32( 3 ),
            dPhiFineMax = cms.double( 0.025 ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 ),
            preClusteringUseChaining = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            NormChi2Cut2D = cms.double( 20.0 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            prePrun = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 ),
            SeedSmall = cms.double( 2.0E-4 ),
            SeedBig = cms.double( 0.0015 ),
            ForceCovariance = cms.bool( False ),
            ForceCovarianceAll = cms.bool( False ),
            Covariance = cms.double( 0.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            BPMinImprovement = cms.double( 10000.0 ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            tanThetaMax = cms.double( 1.2 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            minHitsPerSegment = cms.int32( 3 ),
            dPhiFineMax = cms.double( 0.025 ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 ),
            preClusteringUseChaining = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            NormChi2Cut2D = cms.double( 20.0 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            prePrun = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 ),
            SeedSmall = cms.double( 2.0E-4 ),
            SeedBig = cms.double( 0.0015 ),
            ForceCovariance = cms.bool( False ),
            ForceCovarianceAll = cms.bool( False ),
            Covariance = cms.double( 0.0 )
          )
        ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 )
      )
    )
)
hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    rpcDigiLabel = cms.InputTag( "simMuonRPCDigis" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    maskSource = cms.string( "File" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    deadSource = cms.string( "File" ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    recAlgoConfig = cms.PSet(  )
)
hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    InputObjects = cms.InputTag( "l1extraParticles" ),
    GMTReadoutCollection = cms.InputTag( "gmtDigis" ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" ),
    L1MinPt = cms.double( 0.0 ),
    L1MaxEta = cms.double( 2.5 ),
    L1MinQuality = cms.uint32( 1 ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    )
)
hltL2Muons = cms.EDProducer( "L2MuonProducer",
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    L2TrajBuilderParameters = cms.PSet( 
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          Granularity = cms.int32( 0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False ),
          ExcludeRPCFromFit = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        UseSubRecHits = cms.bool( False ),
        NMinRecHits = cms.uint32( 2 ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          Granularity = cms.int32( 2 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False ),
          ExcludeRPCFromFit = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True ),
      beamSpot = cms.InputTag( "offlineBeamSpot" )
    )
)
hltL2MuonCandidatesNoVtx = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( "hltL2Muons" )
)
hltSingleL2Mu0L2PreFilteredNoVtx = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu0L1Filtered" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreL2Mu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1SingleMu7L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu7" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL2Mu7L2Filtered7 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreL2Mu30 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL2Mu30L2Filtered30 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 30.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1SingleMu0L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu0" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltSingleMu0L2Filtered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu0L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      errorMatrixPset = cms.PSet( 
        action = cms.string( "use" ),
        atIP = cms.bool( True ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      maxChi2 = cms.double( 40.0 )
    ),
    TrackerSeedCleaner = cms.PSet(  ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        TrackerSkipSection = cms.int32( -1 ),
        Chi2CutCSC = cms.double( 150.0 ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        PropDirForCosmics = cms.bool( False ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        Eta_fixed = cms.double( 0.2 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        OnDemand = cms.double( -1.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaR = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        Rescale_eta = cms.double( 3.0 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Phi_fixed = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        Rescale_Dz = cms.double( 3.0 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    )
)
hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        TrackerSkipSection = cms.int32( -1 ),
        Chi2CutCSC = cms.double( 150.0 ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        PropDirForCosmics = cms.bool( False ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        Eta_fixed = cms.double( 0.2 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        OnDemand = cms.double( -1.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaR = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        Rescale_eta = cms.double( 3.0 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Phi_fixed = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        Rescale_Dz = cms.double( 3.0 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    )
)
hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        TrackerSkipSection = cms.int32( -1 ),
        Chi2CutCSC = cms.double( 150.0 ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        PropDirForCosmics = cms.bool( False ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        Eta_fixed = cms.double( 0.2 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        OnDemand = cms.double( -1.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaR = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        Rescale_eta = cms.double( 3.0 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Phi_fixed = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        Rescale_Dz = cms.double( 3.0 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    )
)
hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3TkTracksFromL2IOHit','hltL3TkTracksFromL2OIHit','hltL3TkTracksFromL2OIState' )
)
hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputObjects = cms.InputTag( "hltL3Muons" )
)
hltSingleMu0L3Filtered0 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu0L2Filtered0" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu3L2Filtered3 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu0L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltSingleMu3L3Filtered3 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu3L2Filtered3" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1sL1SingleMu3 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1SingleMu3L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltSingleMu5L2Filtered4 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu3L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 4.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMu5L3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu5L2Filtered4" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1sL1SingleMu5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1SingleMu5L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu5" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltSingleMu7L2Filtered5 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu5L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMu7L3Filtered7 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu7L2Filtered5" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu9 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu9L3Filtered9 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 9.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu11 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu11L3Filtered11 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 11.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu13 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu13L3Filtered13 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 13.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu15L3Filtered15 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu17L3Filtered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu19L3Filtered19 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 19.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu21 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu21L3Filtered21 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 21.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu25 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu21L3Filtered25 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 25.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreIsoMu9 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltTowerMakerForMuons = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRegionalMuonsRecHit:EcalRecHitsEB','hltEcalRegionalMuonsRecHit:EcalRecHitsEE' )
)
hltL2MuonIsolations = cms.EDProducer( "L2MuonIsolationProducer",
    StandAloneCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    ExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.24 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.5 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForMuons" ),
      Weight_H = cms.double( 1.0 )
    ),
    IsolatorPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24 ),
      ComponentName = cms.string( "SimpleCutsIsolator" ),
      Thresholds = cms.vdouble( 4.0, 3.7, 4.0, 3.5, 3.4, 3.4, 3.2, 3.4, 3.1, 2.9, 2.9, 2.7, 3.1, 3.0, 2.4, 2.1, 2.0, 2.3, 2.2, 2.4, 2.5, 2.5, 2.6, 2.9, 3.1, 2.9 ),
      EtaBounds = cms.vdouble( 0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411 )
    )
)
hltSingleMuIsoL2IsoFiltered7 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
    MinN = cms.int32( 1 ),
    DepTag = cms.VInputTag( 'hltL2MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltSingleMuIsoL3PreFiltered9 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 9.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltL3MuonIsolations = cms.EDProducer( "L3MuonIsolationProducer",
    inputMuonCollection = cms.InputTag( "hltL3Muons" ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 1.1, 1.1, 1.1, 1.1, 1.2, 1.1, 1.2, 1.1, 1.2, 1.0, 1.1, 1.0, 1.0, 1.1, 1.0, 1.0, 1.1, 0.9, 1.1, 0.9, 1.1, 1.0, 1.0, 0.9, 0.8, 0.1 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    ExtractorPSet = cms.PSet( 
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPixelTracks" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.24 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( True ),
      DR_VetoPt = cms.double( 0.025 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( True ),
      PtVeto_Min = cms.double( 2.0 )
    )
)
hltSingleMuIsoL3IsoFiltered9 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered9" ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltPreIsoMu11 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMuIsoL3PreFiltered11 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 11.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMuIsoL3IsoFiltered11 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered11" ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltPreIsoMu13 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMuIsoL3PreFiltered13 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 13.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMuIsoL3IsoFiltered13 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered13" ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltPreIsoMu15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMuIsoL3PreFiltered15 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMuIsoL3IsoFiltered15 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered15" ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltPreIsoMu17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMuIsoL3PreFiltered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMuIsoL3IsoFiltered17 = cms.EDFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered17" ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(  )
)
hltPreMu30NoVertex = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltMu30NoVertexL2PreFiltered = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL3TrajectorySeedNoVtx = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( "hltL2Muons" ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      errorMatrixPset = cms.PSet( 
        action = cms.string( "use" ),
        atIP = cms.bool( True ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      maxChi2 = cms.double( 40.0 )
    ),
    TrackerSeedCleaner = cms.PSet(  ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
hltL3TkTracksFromL2NoVtx = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( "hltL3TrackCandidateFromL2NoVtx" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
hltL3MuonsNoVtx = cms.EDProducer( "L3TkMuonProducer",
    InputObjects = cms.InputTag( "hltL3TkTracksFromL2NoVtx" )
)
hltL3MuonCandidatesNoVtx = cms.EDProducer( "L3MuonCandidateProducer",
    InputObjects = cms.InputTag( "hltL3MuonsNoVtx" )
)
hltMu30NoVertexL3PreFiltered30 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidatesNoVtx" ),
    PreviousCandTag = cms.InputTag( "hltMu30NoVertexL2PreFiltered" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 30.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1sL1DoubleMuOpen = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1DoubleMuOpen = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDoubleMuLevel1PathL1OpenFiltered = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpen" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
hltPreL2DoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiMuonL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpen" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltDiMuonL2PreFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreL2DoubleMu20NoVertex = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL2DoubleMu20NoVertexL2PreFiltered = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 20.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreDoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiMuonL3PreFiltered0 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreDoubleMu0Quark = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDoubleMu0QuarkoniumL3PreFiltered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
    FastAccept = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    ChargeOpt = cms.int32( -1 ),
    MinPtPair = cms.double( 0.0 ),
    MinPtMax = cms.double( 0.0 ),
    MinPtMin = cms.double( 0.0 ),
    MinInvMass = cms.double( 1.5 ),
    MaxInvMass = cms.double( 14.5 ),
    MinAcop = cms.double( -999.0 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxPtBalance = cms.double( 999999.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDzMuMu = cms.double( 999999.0 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreDoubleMu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiMuonL3PreFiltered3 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreDoubleMu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDiMuonL3PreFiltered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu5L2Mu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltMu5L2Mu0L3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1sL1SingleEG8 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG8" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1SingleEG8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1SingleEG5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreEle10SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    debugLevel = cms.string( "INFO" ),
    basicclusterCollection = cms.string( "" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    doIsolated = cms.bool( True ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.0030 ),
    eThreshB = cms.double( 0.1 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  )
)
hltCorrectedHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1Isolated" ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
      brLinearHighThr = cms.double( 8.0 ),
      fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -5.735E-4, 1.343 )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
hltMulti5x5BasicClustersL1Isolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    doIsolated = cms.bool( True ),
    barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
hltMulti5x5SuperClustersL1Isolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Isolated" ),
    barrelClusterProducer = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    )
)
hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRegionalEgammaRecHit','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1Isolated','multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 5.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "" )
)
hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.6 ),
      fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
      brLinearHighThr = cms.double( 6.0 ),
      fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
    )
)
hltHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    debugLevel = cms.string( "INFO" ),
    basicclusterCollection = cms.string( "" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    doIsolated = cms.bool( False ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.0030 ),
    eThreshB = cms.double( 0.1 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  )
)
hltCorrectedHybridSuperClustersL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1NonIsolated" ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
      brLinearHighThr = cms.double( 8.0 ),
      fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -5.735E-4, 1.343 )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
hltCorrectedHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
    L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedTemp" ),
    L1IsoSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
    L1NonIsoSkimmedCollection = cms.string( "" )
)
hltMulti5x5BasicClustersL1NonIsolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    doIsolated = cms.bool( False ),
    barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
hltMulti5x5SuperClustersL1NonIsolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1NonIsolated" ),
    barrelClusterProducer = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    )
)
hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRegionalEgammaRecHit','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1NonIsolated','multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 5.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "" )
)
hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.6 ),
      fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
      brLinearHighThr = cms.double( 6.0 ),
      fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
    )
)
hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
    L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp" ),
    L1IsoSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
    L1NonIsoSkimmedCollection = cms.string( "" )
)
hltL1IsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltL1NonIsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG5" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional" ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
hltL1NonIsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
hltL1NonIsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        maxElement = cms.uint32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.0040 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.0040 ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      rMinI = cms.double( -0.2 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMax2 = cms.double( 0.0040 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
    )
)
hltL1NonIsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        maxElement = cms.uint32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.0040 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.0040 ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      rMinI = cms.double( -0.2 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMax2 = cms.double( 0.0040 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
    )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreEle12SWTighterEleIdL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional" ),
    etcutEB = cms.double( 12.0 ),
    etcutEE = cms.double( 12.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
hltL1NonIsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPixelMatchElectronsL1Iso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( "hltCtfL1IsoWithMaterialTracks" ),
    BSProducer = cms.InputTag( "offlineBeamSpot" )
)
hltPixelMatchElectronsL1NonIso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( "hltCtfL1NonIsoWithMaterialTracks" ),
    BSProducer = cms.InputTag( "offlineBeamSpot" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltElectronL1IsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    BSProducer = cms.InputTag( "offlineBeamSpot" )
)
hltElectronL1NonIsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    BSProducer = cms.InputTag( "offlineBeamSpot" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.08 ),
    thrRegularEE = cms.double( 0.08 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltPreEle17SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreEle17SWIsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolL1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 99999.0 ),
    thrRegularEE = cms.double( 99999.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
    ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
    etMinBarrel = cms.double( -9999.0 ),
    eMinBarrel = cms.double( 0.08 ),
    etMinEndcap = cms.double( 0.1 ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    extRadius = cms.double( 0.3 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    tryBoth = cms.bool( True ),
    subtract = cms.bool( False ),
    useNumCrystals = cms.bool( True )
)
hltL1NonIsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
    ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
    etMinBarrel = cms.double( -9999.0 ),
    eMinBarrel = cms.double( 0.08 ),
    etMinEndcap = cms.double( 0.1 ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    extRadius = cms.double( 0.3 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    tryBoth = cms.bool( True ),
    subtract = cms.bool( False ),
    useNumCrystals = cms.bool( True )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.16 ),
    outerCone = cms.double( 0.29 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( True )
)
hltL1NonIsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.16 ),
    outerCone = cms.double( 0.29 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( True )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHcalIsolFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 99999.0 ),
    thrRegularEE = cms.double( 99999.0 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 99999.0 ),
    thrRegularEE = cms.double( 99999.0 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1IsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    trackProducer = cms.InputTag( "hltL1IsoEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
hltL1NonIsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    trackProducer = cms.InputTag( "hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17IsolTrackIsolFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDphiFilter" ),
    isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.2 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltPreEle17SWTighterEleIdIsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.0080 ),
    thrRegularEE = cms.double( 0.0070 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.1 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolTrackIsolFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter" ),
    isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.15 ),
    thrOverPtEE = cms.double( 0.1 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    useEt = cms.untracked.bool( True )
)
hltPreEle17TightCaloEleIdEle8HEL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.012 ),
    thrRegularEE = cms.double( 0.032 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.1 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltHybridSuperClustersActivity = cms.EDProducer( "HybridClusterProducer",
    debugLevel = cms.string( "ERROR" ),
    basicclusterCollection = cms.string( "hybridBarrelBasicClusters" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.string( "hltEcalRecHitAll" ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    HybridBarrelSeedThr = cms.double( 1.0 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.0030 ),
    eThreshB = cms.double( 0.1 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    severityRecHitThreshold = cms.double( 4.0 )
)
hltCorrectedHybridSuperClustersActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersActivity" ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fBremVec = cms.vdouble( -0.04382, 0.1169, 0.9267, -9.413E-4, 1.419 ),
      brLinearHighThr = cms.double( 8.0 ),
      fEtEtaVec = cms.vdouble( 0.0, 1.00121, -0.63672, 0.0, 0.0, 0.0, 0.5655, 6.457, 0.5081, 8.0, 1.023, -0.00181 )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
hltMulti5x5BasicClustersActivity = cms.EDProducer( "Multi5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    barrelHitProducer = cms.string( "hltEcalRecHitAll" ),
    endcapHitProducer = cms.string( "hltEcalRecHitAll" ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    doEndcap = cms.bool( True ),
    doBarrel = cms.bool( False ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    IslandBarrelSeedThr = cms.double( 0.5 ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet( 
      LogWeighted = cms.bool( True ),
      T0_barl = cms.double( 7.4 ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
hltMulti5x5SuperClustersActivity = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    barrelClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet( 
        cryVec = cms.vint32( 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3 ),
        cryMin = cms.int32( 2 ),
        etVec = cms.vdouble( 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 45.0, 55.0, 135.0, 195.0, 225.0 )
      ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      )
    )
)
hltMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRecHitAll','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersActivity','multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 0.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "ERROR" )
)
hltCorrectedMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersWithPreshowerActivity" ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.9 ),
      fBremVec = cms.vdouble( -0.05228, 0.08738, 0.9508, 0.002677, 1.221 ),
      brLinearHighThr = cms.double( 6.0 ),
      fEtEtaVec = cms.vdouble( 1.0, -0.4386, -32.38, 0.6372, 15.67, -0.0928, -2.462, 1.138, 20.93 )
    )
)
hltRecoEcalSuperClusterActivityCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" ),
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltEcalActivitySuperClusterWrapper = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    candIsolatedTag = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    candNonIsolatedTag = cms.InputTag( "none" ),
    doIsolated = cms.bool( True )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltActivityR9Shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9Shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltActivityPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltActivityStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" ),
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.0040 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.0040 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.0040 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    )
)
hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoublePixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltPreEle22SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22L1MatchFilterRegional" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreEle22SWTighterCaloIdIsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolL1MatchFilterRegional" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloldIsolEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloldIsolEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHcalIsolFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( 999999.0 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( 999999.0 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolTrackIsolFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDphiFilter" ),
    isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.15 ),
    thrOverPtEE = cms.double( 0.1 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltPreEle22SWTighterEleIdL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdL1MatchFilterRegional" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.0080 ),
    thrRegularEE = cms.double( 0.0070 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.1 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltPreEle32SWTighterEleIdL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdL1MatchFilterRegional" ),
    etcutEB = cms.double( 32.0 ),
    etcutEE = cms.double( 32.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.0080 ),
    thrRegularEE = cms.double( 0.0070 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.1 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1sL1DoubleEG5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDoubleEle17SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt17L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt17EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt17L1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt17HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt17EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 0.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt17PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt17HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton10L1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG5" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional" ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt10HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreSinglePhoton17IsolSC17HEL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEL1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HER9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HER9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1IsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    trackProducer = cms.InputTag( "hltL1IsoEgammaRegionalCTFFinalFitWithMaterial" ),
    countTracks = cms.bool( False ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    egTrkIsoZSpan = cms.double( 999999.0 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
hltL1NonIsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    trackProducer = cms.InputTag( "hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial" ),
    countTracks = cms.bool( False ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    egTrkIsoZSpan = cms.double( 999999.0 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HETrackIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleEtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9Shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltPrePhoton20L1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional" ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton20CleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePho20IsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonE20IsolCleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonE20IsolCleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedTrackIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreSinglePhoton22SC22HEL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEL1MatchFilterRegional" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HER9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HER9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleEtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9Shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltPrePhoton30CleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 30.0 ),
    etcutEE = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton40CaloIdCleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 40.0 ),
    etcutEE = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePho40IsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 40.0 ),
    etcutEE = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonE40IsolCleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonE40IsolCleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedTrackIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton50HECleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 50.0 ),
    etcutEE = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton50L1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional" ),
    etcutEB = cms.double( 50.0 ),
    etcutEE = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt50HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton70HECleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 70.0 ),
    etcutEE = cms.double( 70.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPrePhoton110NoHECleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 110.0 ),
    etcutEE = cms.double( 110.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreDoublePhoton5CEPL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltDoublePhotonEt5L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltDoublePhotonEt5EtPhiFilter = cms.EDFilter( "HLTEgammaDoubleEtDeltaPhiFilter",
    inputTag = cms.InputTag( "hltDoublePhotonEt5L1MatchFilterRegional" ),
    etcut = cms.double( 5.0 ),
    minDeltaPhi = cms.double( 2.5 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltDoublePhotonEt5EcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltDoublePhotonEt5EtPhiFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 3.0 ),
    thrRegularEE = cms.double( 3.0 ),
    thrOverEEB = cms.double( 0.1 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltDoublePhotonEt5HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltDoublePhotonEt5EcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltTowerMakerForHcal = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0E-99 ),
    EEWeight = cms.double( 1.0E-99 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( True ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag(  )
)
hltHcalTowerFilter = cms.EDFilter( "HLTHcalTowerFilter",
    inputTag = cms.InputTag( "hltTowerMakerForHcal" ),
    MinE_HB = cms.double( 1.5 ),
    MinE_HE = cms.double( 2.5 ),
    MinE_HF = cms.double( 9.0 ),
    MaxN_HB = cms.int32( 2 ),
    MaxN_HE = cms.int32( 2 ),
    MaxN_HF = cms.int32( 8 )
)
hltPreSingleDoublePhoton17SingleIsolL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolL1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolLooseHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolLooseHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolTrackIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreDoublePhoton22L1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt22L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt22EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt22L1MatchFilterRegional" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoublePhotonEt22HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt22EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1sSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltCaloTowersTau1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 0 )
)
hltIconeTau1Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersTau1Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersTau2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 1 )
)
hltIconeTau2Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersTau2Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersTau3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 2 )
)
hltIconeTau3Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersTau3Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersTau4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 3 )
)
hltIconeTau4Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersTau4Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersCentral1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 0 )
)
hltIconeCentral1Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersCentral1Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersCentral2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 1 )
)
hltIconeCentral2Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersCentral2Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersCentral3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 2 )
)
hltIconeCentral3Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersCentral3Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltCaloTowersCentral4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    towers = cms.InputTag( "hltTowerMakerForJets" ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 3 )
)
hltIconeCentral4Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( "hltCaloTowersCentral4Regional" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltL2TauJets = cms.EDProducer( "L2TauJetsMerger",
    EtMin = cms.double( 15.0 ),
    JetSrc = cms.VInputTag( 'hltIconeTau1Regional','hltIconeTau2Regional','hltIconeTau3Regional','hltIconeTau4Regional','hltIconeCentral1Regional','hltIconeCentral2Regional','hltIconeCentral3Regional','hltIconeCentral4Regional' )
)
hltFilterL2EtCutSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL2TauJets" ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL2TauNarrowConeIsolationProducer = cms.EDProducer( "L2TauNarrowConeIsolationProducer",
    L2TauJetCollection = cms.InputTag( "hltL2TauJets" ),
    EBRecHits = cms.InputTag( 'hltEcalRegionalJetsRecHit','EcalRecHitsEB' ),
    EERecHits = cms.InputTag( 'hltEcalRegionalJetsRecHit','EcalRecHitsEE' ),
    CaloTowers = cms.InputTag( "hltTowerMakerForJets" ),
    associationRadius = cms.double( 0.5 ),
    crystalThresholdEE = cms.double( 0.45 ),
    crystalThresholdEB = cms.double( 0.15 ),
    towerThreshold = cms.double( 1.0 ),
    ECALIsolation = cms.PSet( 
      innerCone = cms.double( 0.15 ),
      runAlgorithm = cms.bool( True ),
      outerCone = cms.double( 0.5 )
    ),
    ECALClustering = cms.PSet( 
      runAlgorithm = cms.bool( True ),
      clusterRadius = cms.double( 0.08 )
    ),
    TowerIsolation = cms.PSet( 
      innerCone = cms.double( 0.2 ),
      runAlgorithm = cms.bool( True ),
      outerCone = cms.double( 0.5 )
    )
)
hltL2TauRelaxingIsolationSelector = cms.EDProducer( "L2TauRelaxingIsolationSelector",
    L2InfoAssociation = cms.InputTag( "hltL2TauNarrowConeIsolationProducer" ),
    MinJetEt = cms.double( 15.0 ),
    SeedTowerEt = cms.double( -10.0 ),
    EcalIsolationEt = cms.vdouble( 5.0, 0.025, 7.5E-4 ),
    TowerIsolationEt = cms.vdouble( 1000.0, 0.0, 0.0 ),
    NumberOfClusters = cms.vdouble( 1000.0, 0.0, 0.0 ),
    ClusterPhiRMS = cms.vdouble( 1000.0, 0.0, 0.0 ),
    ClusterEtaRMS = cms.vdouble( 1000.0, 0.0, 0.0 ),
    ClusterDRRMS = cms.vdouble( 1000.0, 0.0, 0.0 )
)
hltFilterL2EcalIsolationSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauRelaxingIsolationSelector','Isolated' ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltFilterL2TauMET25 = cms.EDFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( "hltMet" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 25.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltL25TauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltL2TauRelaxingIsolationSelector','Isolated' ),
    tracks = cms.InputTag( "hltL25TauCtfWithMaterialTracks" ),
    coneSize = cms.double( 0.5 )
)
hltL25TauConeIsolation = cms.EDProducer( "ConeIsolation",
    JetTrackSrc = cms.InputTag( "hltL25TauJetTracksAssociator" ),
    vertexSrc = cms.InputTag( "hltPixelVertices" ),
    useVertex = cms.bool( True ),
    useBeamSpot = cms.bool( True ),
    BeamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    MinimumNumberOfPixelHits = cms.int32( 2 ),
    MinimumNumberOfHits = cms.int32( 5 ),
    MaximumTransverseImpactParameter = cms.double( 300.0 ),
    MinimumTransverseMomentum = cms.double( 1.0 ),
    MaximumChiSquared = cms.double( 100.0 ),
    DeltaZetTrackVertex = cms.double( 0.2 ),
    MatchingCone = cms.double( 0.2 ),
    SignalCone = cms.double( 0.15 ),
    IsolationCone = cms.double( 0.5 ),
    MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
    UseFixedSizeCone = cms.bool( True ),
    VariableConeParameter = cms.double( 3.5 ),
    VariableMaxCone = cms.double( 0.17 ),
    VariableMinCone = cms.double( 0.05 )
)
hltL25TauLeadingTrackPtCut15Selector = cms.EDProducer( "IsolatedTauJetsSelector",
    MinimumTransverseMomentumLeadingTrack = cms.double( 15.0 ),
    UseIsolationDiscriminator = cms.bool( False ),
    UseInHLTOpen = cms.bool( False ),
    JetSrc = cms.VInputTag( 'hltL25TauConeIsolation' )
)
hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCut15Selector" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL3TauSingleTrack15JetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltL25TauLeadingTrackPtCut15Selector" ),
    tracks = cms.InputTag( "hltL3TauSingleTrack15CtfWithMaterialTracks" ),
    coneSize = cms.double( 0.5 )
)
hltL3TauSingleTrack15ConeIsolation = cms.EDProducer( "ConeIsolation",
    JetTrackSrc = cms.InputTag( "hltL3TauSingleTrack15JetTracksAssociator" ),
    vertexSrc = cms.InputTag( "hltPixelVertices" ),
    useVertex = cms.bool( True ),
    useBeamSpot = cms.bool( True ),
    BeamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    MinimumNumberOfPixelHits = cms.int32( 2 ),
    MinimumNumberOfHits = cms.int32( 5 ),
    MaximumTransverseImpactParameter = cms.double( 300.0 ),
    MinimumTransverseMomentum = cms.double( 1.0 ),
    MaximumChiSquared = cms.double( 100.0 ),
    DeltaZetTrackVertex = cms.double( 0.2 ),
    MatchingCone = cms.double( 0.2 ),
    SignalCone = cms.double( 0.15 ),
    IsolationCone = cms.double( 0.5 ),
    MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
    UseFixedSizeCone = cms.bool( True ),
    VariableConeParameter = cms.double( 3.5 ),
    VariableMaxCone = cms.double( 0.17 ),
    VariableMinCone = cms.double( 0.05 )
)
hltL3TauSingleTrack15IsolationSelector = cms.EDProducer( "IsolatedTauJetsSelector",
    MinimumTransverseMomentumLeadingTrack = cms.double( 15.0 ),
    UseIsolationDiscriminator = cms.bool( True ),
    UseInHLTOpen = cms.bool( False ),
    JetSrc = cms.VInputTag( 'hltL3TauSingleTrack15ConeIsolation' )
)
hltL1HLTSingleIsoTau20Trk15MET25JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( "hltL3TauSingleTrack15IsolationSelector" ),
    L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau20Trk15MET25" ),
    EtMin = cms.double( 20.0 )
)
hltFilterL3TrackIsolationSingleIsoTau20Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL1HLTSingleIsoTau20Trk15MET25JetsMatch" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltFilterL2EtCutSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL2TauJets" ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltFilterL2EcalIsolationSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauRelaxingIsolationSelector','Isolated' ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltFilterL25LeadingTrackPtCutSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCut15Selector" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1HLTSingleIsoTau35Trk15MET25JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( "hltL3TauSingleTrack15IsolationSelector" ),
    L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau35Trk15MET25" ),
    EtMin = cms.double( 35.0 )
)
hltFilterL3TrackIsolationSingleIsoTau35Trk15MET25 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL1HLTSingleIsoTau35Trk15MET25JetsMatch" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet14U OR L1_DoubleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltFilterL2EtCutDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL2TauJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltFilterL2EcalIsolationDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauRelaxingIsolationSelector','Isolated' ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltL25TauLeadingTrackPtCutSelector = cms.EDProducer( "IsolatedTauJetsSelector",
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    UseIsolationDiscriminator = cms.bool( False ),
    UseInHLTOpen = cms.bool( False ),
    JetSrc = cms.VInputTag( 'hltL25TauConeIsolation' )
)
hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
    L1TauTrigger = cms.InputTag( "hltL1sDoubleOneLegIsoTau15Trk5" ),
    EtMin = cms.double( 15.0 )
)
hltFilterL25LeadingTrackPtCutDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltL3TauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
    tracks = cms.InputTag( "hltL3TauCtfWithMaterialTracks" ),
    coneSize = cms.double( 0.5 )
)
hltL3TauConeIsolation = cms.EDProducer( "ConeIsolation",
    JetTrackSrc = cms.InputTag( "hltL3TauJetTracksAssociator" ),
    vertexSrc = cms.InputTag( "hltPixelVertices" ),
    useVertex = cms.bool( True ),
    useBeamSpot = cms.bool( True ),
    BeamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    MinimumNumberOfPixelHits = cms.int32( 2 ),
    MinimumNumberOfHits = cms.int32( 5 ),
    MaximumTransverseImpactParameter = cms.double( 300.0 ),
    MinimumTransverseMomentum = cms.double( 1.0 ),
    MaximumChiSquared = cms.double( 100.0 ),
    DeltaZetTrackVertex = cms.double( 0.2 ),
    MatchingCone = cms.double( 0.2 ),
    SignalCone = cms.double( 0.15 ),
    IsolationCone = cms.double( 0.5 ),
    MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
    UseFixedSizeCone = cms.bool( True ),
    VariableConeParameter = cms.double( 3.5 ),
    VariableMaxCone = cms.double( 0.17 ),
    VariableMinCone = cms.double( 0.05 )
)
hltL3TauIsolationSelector = cms.EDProducer( "IsolatedTauJetsSelector",
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    UseIsolationDiscriminator = cms.bool( True ),
    UseInHLTOpen = cms.bool( False ),
    JetSrc = cms.VInputTag( 'hltL3TauConeIsolation' )
)
hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
    L1TauTrigger = cms.InputTag( "hltL1sDoubleOneLegIsoTau15Trk5" ),
    EtMin = cms.double( 15.0 )
)
hltFilterL3TrackIsolationDoubleOneLegIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
hltL1sDoubleIsoTau15Trk5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet14U OR L1_DoubleJet30U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreDoubleIsoTau15Trk5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltFilterL2EtCutDoubleIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL2TauJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltFilterL2EcalIsolationDoubleIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauRelaxingIsolationSelector','Isolated' ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltL1HLTDoubleIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
    L1TauTrigger = cms.InputTag( "hltL1sDoubleIsoTau15Trk5" ),
    EtMin = cms.double( 15.0 )
)
hltFilterL3TrackIsolationDoubleIsoTau15Trk5 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltL1HLTDoubleIsoTau15Trk5JetsMatch" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
hltL1sBTagMuDiJet10U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet6U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreBTagMuDiJet10U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltBDiJet10U = cms.EDFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 10.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
hltSelector4JetsU = cms.EDFilter( "LargestEtCaloJetSelector",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    filter = cms.bool( False ),
    maxNumber = cms.uint32( 4 )
)
hltBSoftMuonL25JetsU = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( "hltSelector4JetsU" ),
    filter = cms.bool( False ),
    etMin = cms.double( 10.0 )
)
hltBSoftMuonL25TagInfosU = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptons = cms.InputTag( "hltL2Muons" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
hltBSoftMuonL25BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonL25TagInfosU' )
)
hltBSoftMuonL25FilterUByDR = cms.EDFilter( "HLTJetTag",
    JetTag = cms.InputTag( "hltBSoftMuonL25BJetTagsUByDR" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( False )
)
hltBSoftMuonL3TagInfosU = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptons = cms.InputTag( "hltL3Muons" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
hltBSoftMuonL3BJetTagsUByPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByPt" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonL3TagInfosU' )
)
hltBSoftMuonL3BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonL3TagInfosU' )
)
hltBSoftMuonL3FilterUByDR = cms.EDFilter( "HLTJetTag",
    JetTag = cms.InputTag( "hltBSoftMuonL3BJetTagsUByDR" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
hltPreBTagMuDiJet20U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltBDiJet20U = cms.EDFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
hltPreBTagMuDiJet30U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltBDiJet30U = cms.EDFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
hltPreBTagMuDiJet20UMu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltBSoftMuonL3 = cms.EDFilter( "RecoTrackRefSelector",
    src = cms.InputTag( "hltL3Muons" ),
    maxChi2 = cms.double( 10000.0 ),
    tip = cms.double( 120.0 ),
    minRapidity = cms.double( -5.0 ),
    lip = cms.double( 300.0 ),
    ptMin = cms.double( 5.0 ),
    maxRapidity = cms.double( 5.0 ),
    quality = cms.vstring(  ),
    algorithm = cms.vstring(  ),
    minHit = cms.int32( 0 ),
    min3DHit = cms.int32( 0 ),
    beamSpot = cms.InputTag( "offlineBeamSpot" )
)
hltBSoftMuonSelL3TagInfosU = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptons = cms.InputTag( "hltBSoftMuonL3" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
hltBSoftMuonSelL3BJetTagsUByPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByPt" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonSelL3TagInfosU' )
)
hltBSoftMuonSelL3BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonSelL3TagInfosU' )
)
hltBSoftMuonSelL3FilterUByDR = cms.EDFilter( "HLTJetTag",
    JetTag = cms.InputTag( "hltBSoftMuonSelL3BJetTagsUByDR" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
hltPreBTagMuDiJet30UMu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1SingleJet10UNotBptxOR = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U_NotBptxOR" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    saveTags = cms.untracked.bool( False )
)
hltPreStoppedHSCP20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltStoppedHSCPHpdFilter = cms.EDFilter( "HLTHPDFilter",
    inputTag = cms.InputTag( "hltHbhereco" ),
    energy = cms.double( -99.0 ),
    hpdSpikeEnergy = cms.double( 10.0 ),
    hpdSpikeIsolationEnergy = cms.double( 1.0 ),
    rbxSpikeEnergy = cms.double( 50.0 ),
    rbxSpikeUnbalance = cms.double( 0.2 )
)
hltStoppedHSCPTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "" ),
    hfInput = cms.InputTag( "" ),
    AllowMissingInputs = cms.bool( True ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag(  )
)
hltStoppedHSCPIterativeCone5CaloJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( "hltStoppedHSCPTowerMakerForAll" ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltStoppedHSCP1CaloJetEnergy20 = cms.EDFilter( "HLT1CaloJetEnergy",
    inputTag = cms.InputTag( "hltStoppedHSCPIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    MinE = cms.double( 20.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
hltPreStoppedHSCP35 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltStoppedHSCP1CaloJetEnergy35 = cms.EDFilter( "HLT1CaloJetEnergy",
    inputTag = cms.InputTag( "hltStoppedHSCPIterativeCone5CaloJets" ),
    saveTag = cms.untracked.bool( True ),
    MinE = cms.double( 35.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
hltL1sL1Mu3EG5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_EG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu7Photon13CleanedL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1Mu3EG5" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedL1MatchFilterRegional" ),
    etcutEB = cms.double( 13.0 ),
    etcutEE = cms.double( 13.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1SingleMu3EG5L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1Mu3EG5" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltSingleMu5EG5L2Filtered4 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMu3EG5L1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 4.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMu7EG5L3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu5EG5L2Filtered4" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1sL1SingleMuOpenIgnorePrescale = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( False ),
    L1NrBxInEvent = cms.int32( 1 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu5Ele13 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1SingleMuOpenIgnorePrescaleL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenIgnorePrescale" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltSingleMuIgnorePrescaleL2Filtered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1SingleMuOpenIgnorePrescaleL1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltSingleMuIgnorePrescaleL3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIgnorePrescaleL2Filtered0" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1NonIsoHLTNonIsoSingleElectronEt13L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt13EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt13L1MatchFilterRegional" ),
    etcutEB = cms.double( 13.0 ),
    etcutEE = cms.double( 13.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt13R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt13EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt13HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt13R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt13PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt13HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreMu5Ele17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoMu5Ele17L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoMu5Ele17EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoMu5Ele17L1MatchFilterRegional" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoMu5Ele17R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoMu5Ele17EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoMu5Ele17HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoMu5Ele17R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoMu5Ele17PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoMu5Ele17HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltPreMu8Ele8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu8L3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu5L2Filtered4" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1NonIsoHLTNonIsoSingleMu8Ele8EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltActivityR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleMu8Ele8R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu8Ele8EtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu8Ele8HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu8Ele8R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu8Ele8PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu8Ele8HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltPreMu11Ele8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMu11L3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMu5L2Filtered4" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 11.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1NonIsoHLTNonIsoSingleMu11Ele8EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" )
)
hltL1NonIsoHLTNonIsoSingleMu11Ele8R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu11Ele8EtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu11Ele8HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu11Ele8R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu11Ele8PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu11Ele8HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1sL1Mu3Jet10U = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet10U" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu5Jet50U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1Mu3Jet10UL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( "l1extraParticles" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1Mu3Jet10U" ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    SelectQualities = cms.vint32(  )
)
hltL2Mu5Jet10UL2Filtered4 = cms.EDFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL1Mu3Jet10UL1Filtered0" ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 4.0 ),
    NSigmaPt = cms.double( 0.0 )
)
hltL3Mu5Jet10UL3Filtered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltL2Mu5Jet10UL2Filtered4" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltPreMu5Jet70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1ETM20 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETM20" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMu5MET45 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreMu5HT70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltHT70U = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHt" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 70.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreMu5HT100U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreMu3Ele8HT70U = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltSingleMuIgnorePrescaleL3Filtered3 = cms.EDFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltSingleMuIgnorePrescaleL2Filtered0" ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UEtFilter" ),
    isoTag = cms.InputTag( "hltActivityR9shape" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    L1NonIsoCand = cms.InputTag( "" )
)
hltMCJetCorJetIcone5HF07Mu3Ele8HT70U = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UPixelMatchFilter" ),
    SourceJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minDeltaR = cms.double( 0.5 )
)
hltJet20UHtMu3Ele8HT70U = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07Mu3Ele8HT70U" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltMu3Ele8HT70UHTFilter = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHtMu3Ele8HT70U" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 70.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreEle10HT70SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT70L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT70EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT70L1MatchFilterRegional" ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT70R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT70EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT70HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT70R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT70PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT70HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltMCJetCorJetIcone5HF07Ele10Removed = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT70PixelMatchFilter" ),
    SourceJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minDeltaR = cms.double( 0.5 )
)
hltJet20UHtEle10 = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07Ele10Removed" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltEle10HT70HTFilter = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHtEle10" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 70.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreEle10EleIdHT70SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70L1MatchFilterRegional" ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70ClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70ClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70OneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70PixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70DetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70OneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.0080 ),
    thrRegularEE = cms.double( 0.0070 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70DphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70DetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.1 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltMCJetCorJetIcone5HF07Ele10EleIdRemoved = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70PixelMatchFilter" ),
    SourceJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minDeltaR = cms.double( 0.5 )
)
hltJet20UHtEle10EleId = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07Ele10EleIdRemoved" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltEle10EleIdHT70HTFilter = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHtEle10EleId" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 70.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreEle10HT100SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT100L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT100EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT100L1MatchFilterRegional" ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT100R9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT100EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT100HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT100R9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt10HT100PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT100HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltMCJetCorJetIcone5HF07Ele10ForHT100Removed = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HT100PixelMatchFilter" ),
    SourceJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minDeltaR = cms.double( 0.5 )
)
hltJet20UHtEle10HT100 = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07Ele10ForHT100Removed" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltEle10HT100HTFilter = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHtEle10HT100" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 100.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreDoubleEle8HT70SWL1R = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70L1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70L1MatchFilterRegional" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70EtFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 0.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70HEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltMCJetCorJetIcone5HF07DiEle8Removed = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70PixelMatchFilter" ),
    SourceJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
    minDeltaR = cms.double( 0.5 )
)
hltJet20UHtDiEle8 = cms.EDProducer( "METProducer",
    src = cms.InputTag( "hltMCJetCorJetIcone5HF07DiEle8Removed" ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 20.0 ),
    noHF = cms.bool( False ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    jets = cms.InputTag( "unused" ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.0050 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.0050 ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    HO_PhiResPar = cms.vdouble( 0.02511 )
)
hltDoubleEle8HT70HTFilter = cms.EDFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( "hltJet20UHtDiEle8" ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 70.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
hltPreMu11PFTau15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltIterativeCone5CaloJets8 = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( "hltIterativeCone5CaloJets" ),
    filter = cms.bool( False ),
    etMin = cms.double( 8.0 )
)
hltFilterMu11PFTau15CaloJet8 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJets8" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 8.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltParticleFlowRecHitECAL = cms.EDProducer( "PFRecHitProducerECAL",
    ecalRecHitsEB = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    ecalRecHitsEE = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    crossBarrelEndcapBorder = cms.bool( False ),
    timing_Cleaning = cms.bool( False ),
    thresh_Cleaning = cms.double( 2.0 ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.08 ),
    thresh_Endcap = cms.double( 0.3 ),
    topological_Cleaning = cms.bool( True )
)
hltParticleFlowRecHitHCAL = cms.EDProducer( "PFRecHitProducerHCAL",
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    caloTowers = cms.InputTag( "hltTowerMakerForAll" ),
    thresh_HF = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    weight_HFem = cms.double( 1.0 ),
    weight_HFhad = cms.double( 1.0 ),
    HCAL_Calib = cms.bool( True ),
    HF_Calib = cms.bool( False ),
    Max_Calib = cms.double( 5.0 ),
    ShortFibre_Cut = cms.double( 60.0 ),
    LongFibre_Fraction = cms.double( 0.05 ),
    LongFibre_Cut = cms.double( 120.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    ApplyLongShortDPG = cms.bool( False ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    ApplyTimeDPG = cms.bool( False ),
    ApplyPulseDPG = cms.bool( False ),
    ECAL_Compensate = cms.bool( False ),
    ECAL_Threshold = cms.double( 10.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    EM_Depth = cms.double( 22.0 ),
    HAD_Depth = cms.double( 47.0 ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.4 ),
    thresh_Endcap = cms.double( 0.4 ),
    HCAL_Calib_29 = cms.double( 1.35 ),
    HF_Calib_29 = cms.double( 1.07 )
)
hltParticleFlowRecHitPS = cms.EDProducer( "PFRecHitProducerPS",
    ecalRecHitsES = cms.InputTag( 'hltESRecHitAll','EcalRecHitsES' ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 7.0E-6 ),
    thresh_Endcap = cms.double( 7.0E-6 )
)
hltParticleFlowClusterECAL = cms.EDProducer( "PFClusterProducer",
    thresh_Barrel = cms.double( 0.08 ),
    thresh_Seed_Barrel = cms.double( 0.23 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 4.0 ),
    thresh_Endcap = cms.double( 0.3 ),
    thresh_Seed_Endcap = cms.double( 0.6 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 100000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 10.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( 0.04 ),
    thresh_DoubleSpike_Endcap = cms.double( 1.0E9 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 8 ),
    posCalcNCrystal = cms.int32( 9 ),
    showerSigma = cms.double( 1.5 ),
    useCornerCells = cms.bool( True ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 1 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( "hltParticleFlowRecHitECAL" ),
    minS4S1_Clean_Barrel = cms.vdouble( 0.04, -0.024 ),
    minS4S1_Clean_Endcap = cms.vdouble( 0.04, -0.025 )
)
hltParticleFlowClusterHCAL = cms.EDProducer( "PFClusterProducer",
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 0.8 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 1.0E7 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.1 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 1000000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 10.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( 0.04 ),
    thresh_DoubleSpike_Endcap = cms.double( 1.0E9 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 4 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 1.5 ),
    useCornerCells = cms.bool( True ),
    cleanRBXandHPDs = cms.bool( True ),
    depthCor_Mode = cms.int32( 0 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( "hltParticleFlowRecHitHCAL" ),
    minS4S1_Clean_Barrel = cms.vdouble( 0.032, -0.045 ),
    minS4S1_Clean_Endcap = cms.vdouble( 0.032, -0.045 )
)
hltParticleFlowClusterHFEM = cms.EDProducer( "PFClusterProducer",
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 1.4 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 80.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.4 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.15 ),
    thresh_Clean_Endcap = cms.double( 80.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 10.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( 0.04 ),
    thresh_DoubleSpike_Endcap = cms.double( 1.0E9 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 0 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 0 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitHCAL','HFEM' ),
    minS4S1_Clean_Barrel = cms.vdouble( 0.11, -0.19 ),
    minS4S1_Clean_Endcap = cms.vdouble( 0.11, -0.19 )
)
hltParticleFlowClusterHFHAD = cms.EDProducer( "PFClusterProducer",
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 1.4 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 120.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.4 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 120.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 10.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( 0.04 ),
    thresh_DoubleSpike_Endcap = cms.double( 1.0E9 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 0 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 0 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitHCAL','HFHAD' ),
    minS4S1_Clean_Barrel = cms.vdouble( 0.045, -0.08 ),
    minS4S1_Clean_Endcap = cms.vdouble( 0.045, -0.08 )
)
hltParticleFlowClusterPS = cms.EDProducer( "PFClusterProducer",
    thresh_Barrel = cms.double( 6.0E-5 ),
    thresh_Seed_Barrel = cms.double( 1.2E-4 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 100000.0 ),
    thresh_Endcap = cms.double( 6.0E-5 ),
    thresh_Seed_Endcap = cms.double( 1.2E-4 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 100000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 10.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( 0.04 ),
    thresh_DoubleSpike_Endcap = cms.double( 1.0E9 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 8 ),
    posCalcNCrystal = cms.int32( -1 ),
    showerSigma = cms.double( 0.2 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 0 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( "hltParticleFlowRecHitPS" ),
    minS4S1_Clean_Barrel = cms.vdouble( 0.0, 0.0 ),
    minS4S1_Clean_Endcap = cms.vdouble( 0.0, 0.0 )
)
hltLightPFTracks = cms.EDProducer( "LightPFTrackProducer",
    UseQuality = cms.bool( False ),
    TrackQuality = cms.string( "none" ),
    TkColList = cms.VInputTag( 'hltPFJetCtfWithMaterialTracks' )
)
hltParticleFlowBlock = cms.EDProducer( "PFBlockProducer",
    RecTracks = cms.InputTag( "hltLightPFTracks" ),
    GsfRecTracks = cms.InputTag( "pfTrackElec" ),
    ConvBremGsfRecTracks = cms.InputTag( 'pfTrackElec','Secondary' ),
    RecMuons = cms.InputTag( "muons" ),
    PFNuclear = cms.InputTag( "pfDisplacedTrackerVertex" ),
    PFConversions = cms.InputTag( "pfConversions" ),
    PFV0 = cms.InputTag( "pfV0" ),
    PFClustersECAL = cms.InputTag( "hltParticleFlowClusterECAL" ),
    PFClustersHCAL = cms.InputTag( "hltParticleFlowClusterHCAL" ),
    PFClustersHFEM = cms.InputTag( "hltParticleFlowClusterHFEM" ),
    PFClustersHFHAD = cms.InputTag( "hltParticleFlowClusterHFHAD" ),
    PFClustersPS = cms.InputTag( "hltParticleFlowClusterPS" ),
    usePFatHLT = cms.bool( True ),
    useNuclear = cms.bool( False ),
    useConversions = cms.bool( False ),
    useConvBremGsfTracks = cms.bool( False ),
    useConvBremPFRecTracks = cms.bool( False ),
    useV0 = cms.bool( False ),
    useIterTracking = cms.bool( False ),
    nuclearInteractionsPurity = cms.uint32( 1 ),
    pf_DPtoverPt_Cut = cms.vdouble( -1.0, -1.0, -1.0, -1.0 ),
    pf_NHit_Cut = cms.vuint32( 0, 0, 0, 0 ),
    useRecMuons = cms.bool( False ),
    useGsfRecTracks = cms.bool( False ),
    useEGPhotons = cms.bool( False )
)
hltParticleFlow = cms.EDProducer( "PFProducer",
    pf_newCalib = cms.uint32( 2 ),
    pfcluster_lowEP0 = cms.double( 0.3249189 ),
    pfcluster_lowEP1 = cms.double( 0.790799 ),
    pfcluster_globalP0 = cms.double( -2.315 ),
    pfcluster_globalP1 = cms.double( 1.01 ),
    pfcluster_allowNegative = cms.uint32( 0 ),
    pfcluster_doCorrection = cms.uint32( 1 ),
    pfcluster_barrelEndcapEtaDiv = cms.double( 1.4 ),
    pfcluster_doEtaCorrection = cms.uint32( 1 ),
    calibHF_use = cms.bool( False ),
    blocks = cms.InputTag( "hltParticleFlowBlock" ),
    muons = cms.InputTag( "" ),
    postMuonCleaning = cms.bool( False ),
    usePFElectrons = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    egammaElectrons = cms.InputTag( "" ),
    pf_electron_output_col = cms.string( "electrons" ),
    usePFSCEleCalib = cms.bool( True ),
    useEGammaSupercluster = cms.bool( False ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    pf_calib_ECAL_slope = cms.double( 1.0 ),
    pf_calib_ECAL_offset = cms.double( 0.0 ),
    pf_calib_ECAL_HCAL_eslope = cms.double( 1.05 ),
    pf_calib_ECAL_HCAL_hslope = cms.double( 1.06 ),
    pf_calib_ECAL_HCAL_offset = cms.double( 6.11 ),
    pf_calib_HCAL_slope = cms.double( 2.17 ),
    pf_calib_HCAL_offset = cms.double( 1.73 ),
    pf_calib_HCAL_damping = cms.double( 2.49 ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan.txt" ),
    pf_electronID_crackCorrection = cms.bool( False ),
    rejectTracks_Bad = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    usePFNuclearInteractions = cms.bool( False ),
    usePFConversions = cms.bool( False ),
    usePFDecays = cms.bool( False ),
    dptRel_DispVtx = cms.double( 20.0 ),
    algoType = cms.uint32( 0 ),
    nsigma_TRACK = cms.double( 1.0 ),
    pt_Error = cms.double( 1.0 ),
    usePFMuonMomAssign = cms.bool( False ),
    postHFCleaning = cms.bool( False ),
    minHFCleaningPt = cms.double( 5.0 ),
    minSignificance = cms.double( 2.5 ),
    maxSignificance = cms.double( 2.5 ),
    minSignificanceReduction = cms.double( 1.4 ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    minDeltaMet = cms.double( 0.4 ),
    vertexCollection = cms.InputTag( "hltPixelVertices" ),
    useVerticesForNeutral = cms.bool( True ),
    pfcluster_etaCorrection = cms.vdouble( 1.01, -0.0102, 0.0517, 0.563, -0.425, 0.11 ),
    calibHF_eta_step = cms.vdouble( 0.0, 2.9, 3.0, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.2 ),
    calibHF_a_EMonly = cms.vdouble( 0.96945, 0.96701, 0.76309, 0.82268, 0.87583 ),
    calibHF_b_HADonly = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348 ),
    calibHF_a_EMHAD = cms.vdouble( 1.42215, 1.00496, 0.68961, 0.81656, 0.98504 ),
    calibHF_b_EMHAD = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348 ),
    calibPFSCEle_barrel = cms.vdouble( 1.0326, -13.71, 339.72, 0.4862, 0.00182, 0.36445, 1.411, 1.0206, 0.0059162, -5.14434E-5, 1.42516E-7 ),
    calibPFSCEle_endcap = cms.vdouble( 0.9995, -12.313, 2.8784, -1.057E-4, 10.282, 3.059, 0.0013502, -2.2185, 3.4206 ),
    muon_HCAL = cms.vdouble( 3.0, 3.0 ),
    muon_ECAL = cms.vdouble( 0.5, 0.5 ),
    factors_45 = cms.vdouble( 10.0, 100.0 ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHCAL:Cleaned','hltParticleFlowClusterHFHAD:Cleaned','hltParticleFlowClusterHFEM:Cleaned' ),
    iCfgCandConnector = cms.PSet( 
      bCalibSecondary = cms.bool( False ),
      bCalibPrimary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      nuclCalibFactors = cms.vdouble( 0.88, 0.28, 0.04 )
    ),
    pf_clusterRecovery = cms.bool( False ),
    ecalHcalEcalEndcap = cms.vdouble( 0.46, 3.0, 1.1, 0.4, -0.02, 1.4 ),
    ecalHcalEcalBarrel = cms.vdouble( 0.67, 3.0, 1.15, 0.9, -0.06, 1.4 ),
    ecalHcalHcalBarrel = cms.vdouble( 0.46, 3.0, 1.15, 0.3, -0.02, 1.4 ),
    ecalHcalHcalEndcap = cms.vdouble( 0.46, 3.0, 1.1, 0.3, -0.02, 1.4 ),
    useCalibrationsFromDB = cms.bool( False ),
    usePFPhotons = cms.bool( False ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble( 0.6, 6.0, -0.0255975, 0.0576727, 0.975442, -5.46394E-4, 1.26147, 25.0, -0.02025, 0.04537, 0.9728, -8.962E-4, 1.172 ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble( 0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 4.74665E-4, 1.10782 )
)
hltIcone5PFJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( "hltParticleFlow" ),
    srcPVs = cms.InputTag( "hltPixelVertices" ),
    jetType = cms.string( "PFJet" ),
    jetPtMin = cms.double( 15.0 ),
    inputEtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
hltIcone5ConvPFJets = cms.EDProducer( "PFJetToCaloProducer",
    Source = cms.InputTag( "hltIcone5PFJets" )
)
hltFilterMu11PFTau15PFJet15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIcone5ConvPFJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltPFTauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltIcone5PFJets" ),
    tracks = cms.InputTag( "hltPFJetCtfWithMaterialTracks" ),
    coneSize = cms.double( 0.5 )
)
hltPFTauTagInfo = cms.EDProducer( "PFRecoTauTagInfoProducer",
    PFCandidateProducer = cms.InputTag( "hltParticleFlow" ),
    PFJetTracksAssociatorProducer = cms.InputTag( "hltPFTauJetTracksAssociator" ),
    PVProducer = cms.InputTag( "hltPixelVertices" ),
    smearedPVsigmaX = cms.double( 0.0015 ),
    smearedPVsigmaY = cms.double( 0.0015 ),
    smearedPVsigmaZ = cms.double( 0.0050 ),
    ChargedHadrCand_AssociationCone = cms.double( 0.8 ),
    ChargedHadrCand_tkminPt = cms.double( 0.0 ),
    ChargedHadrCand_tkminPixelHitsn = cms.int32( 0 ),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32( 3 ),
    ChargedHadrCand_tkmaxipt = cms.double( 0.2 ),
    ChargedHadrCand_tkmaxChi2 = cms.double( 1000.0 ),
    NeutrHadrCand_HcalclusMinEt = cms.double( 1.0 ),
    GammaCand_EcalclusMinEt = cms.double( 0.5 ),
    tkminPt = cms.double( 0.0 ),
    tkminPixelHitsn = cms.int32( 0 ),
    tkminTrackerHitsn = cms.int32( 3 ),
    tkmaxipt = cms.double( 0.2 ),
    tkmaxChi2 = cms.double( 100.0 ),
    UsePVconstraint = cms.bool( False ),
    ChargedHadrCand_tkPVmaxDZ = cms.double( 0.4 ),
    tkPVmaxDZ = cms.double( 0.4 )
)
hltPFTaus = cms.EDProducer( "PFRecoTauProducer",
    PFTauTagInfoProducer = cms.InputTag( "hltPFTauTagInfo" ),
    ElectronPreIDProducer = cms.InputTag( "elecpreid" ),
    PVProducer = cms.InputTag( "hltPixelVertices" ),
    Algorithm = cms.string( "ConeBased" ),
    smearedPVsigmaX = cms.double( 0.0015 ),
    smearedPVsigmaY = cms.double( 0.0015 ),
    smearedPVsigmaZ = cms.double( 0.0050 ),
    JetPtMin = cms.double( 0.0 ),
    LeadPFCand_minPt = cms.double( 0.0 ),
    UseChargedHadrCandLeadChargedHadrCand_tksDZconstraint = cms.bool( False ),
    ChargedHadrCandLeadChargedHadrCand_tksmaxDZ = cms.double( 0.4 ),
    LeadTrack_minPt = cms.double( 0.0 ),
    UseTrackLeadTrackDZconstraint = cms.bool( False ),
    TrackLeadTrack_maxDZ = cms.double( 0.4 ),
    MatchingConeMetric = cms.string( "DR" ),
    MatchingConeSizeFormula = cms.string( "0.2" ),
    MatchingConeSize_min = cms.double( 0.0 ),
    MatchingConeSize_max = cms.double( 0.6 ),
    TrackerSignalConeMetric = cms.string( "DR" ),
    TrackerSignalConeSizeFormula = cms.string( "0.2" ),
    TrackerSignalConeSize_min = cms.double( 0.0 ),
    TrackerSignalConeSize_max = cms.double( 0.2 ),
    TrackerIsolConeMetric = cms.string( "DR" ),
    TrackerIsolConeSizeFormula = cms.string( "0.40" ),
    TrackerIsolConeSize_min = cms.double( 0.0 ),
    TrackerIsolConeSize_max = cms.double( 0.6 ),
    ECALSignalConeMetric = cms.string( "DR" ),
    ECALSignalConeSizeFormula = cms.string( "0.2" ),
    ECALSignalConeSize_min = cms.double( 0.0 ),
    ECALSignalConeSize_max = cms.double( 0.6 ),
    ECALIsolConeMetric = cms.string( "DR" ),
    ECALIsolConeSizeFormula = cms.string( "0.50" ),
    ECALIsolConeSize_min = cms.double( 0.0 ),
    ECALIsolConeSize_max = cms.double( 0.6 ),
    HCALSignalConeMetric = cms.string( "DR" ),
    HCALSignalConeSizeFormula = cms.string( "0.10" ),
    HCALSignalConeSize_min = cms.double( 0.0 ),
    HCALSignalConeSize_max = cms.double( 0.6 ),
    HCALIsolConeMetric = cms.string( "DR" ),
    HCALIsolConeSizeFormula = cms.string( "0.50" ),
    HCALIsolConeSize_min = cms.double( 0.0 ),
    HCALIsolConeSize_max = cms.double( 0.6 ),
    Rphi = cms.double( 2.0 ),
    MaxEtInEllipse = cms.double( 2.0 ),
    AddEllipseGammas = cms.bool( False ),
    AreaMetric_recoElements_maxabsEta = cms.double( 2.5 ),
    ChargedHadrCand_IsolAnnulus_minNhits = cms.uint32( 0 ),
    Track_IsolAnnulus_minNhits = cms.uint32( 3 ),
    ElecPreIDLeadTkMatch_maxDR = cms.double( 0.01 ),
    EcalStripSumE_minClusEnergy = cms.double( 0.1 ),
    EcalStripSumE_deltaEta = cms.double( 0.03 ),
    EcalStripSumE_deltaPhiOverQ_minValue = cms.double( -0.1 ),
    EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.5 ),
    maximumForElectrionPreIDOutput = cms.double( -0.1 ),
    DataType = cms.string( "AOD" ),
    emMergingAlgorithm = cms.string( "" ),
    candOverlapCriterion = cms.string( "" ),
    doOneProng = cms.bool( False ),
    doOneProngStrip = cms.bool( False ),
    doOneProngTwoStrips = cms.bool( False ),
    doThreeProng = cms.bool( False ),
    tauPtThreshold = cms.double( 0.0 ),
    leadPionThreshold = cms.double( 0.0 ),
    stripPtThreshold = cms.double( 0.0 ),
    chargeHadrIsolationConeSize = cms.double( 0.0 ),
    gammaIsolationConeSize = cms.double( 0.0 ),
    neutrHadrIsolationConeSize = cms.double( 0.0 ),
    useIsolationAnnulus = cms.bool( False ),
    matchingCone = cms.double( 0.0 ),
    coneMetric = cms.string( "" ),
    coneSizeFormula = cms.string( "" ),
    minimumSignalCone = cms.double( 0.0 ),
    maximumSignalCone = cms.double( 0.0 ),
    oneProngStripMassWindow = cms.vdouble(  ),
    oneProngTwoStripsMassWindow = cms.vdouble(  ),
    oneProngTwoStripsPi0MassWindow = cms.vdouble(  ),
    threeProngMassWindow = cms.vdouble(  )
)
hltPFTauTrackFindingDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( "hltPFTaus" ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 0.0 )
)
hltPFTauIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTaus" ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    maximumSumPtCut = cms.double( 6.0 ),
    maximumOccupancy = cms.uint32( 0 ),
    relativeSumPtCut = cms.double( 0.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    PVProducer = cms.InputTag( "hltPixelVertices" ),
    applyOccupancyCut = cms.bool( True ),
    applyRelativeSumPtCut = cms.bool( False ),
    applySumPtCut = cms.bool( False ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    qualityCuts = cms.PSet( 
      signalQualityCuts = cms.PSet( 
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        maxDeltaZ = cms.double( 0.5 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        minTrackPt = cms.double( 0.0 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 )
      ),
      isolationQualityCuts = cms.PSet( 
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.8 ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPt = cms.double( 1.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 )
      )
    )
)
hltSelectedPFTaus = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( "hltPFTaus" ),
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackFindingDiscriminator" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauIsolationDiscriminator" ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
hltConvPFTaus = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( "hltSelectedPFTaus" )
)
hltFilterMu11PFTau15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltConvPFTaus" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltOverlapFilterMu11PFTau15 = cms.EDFilter( "HLT2MuonTau",
    inputTag1 = cms.InputTag( "hltSingleMu11L3Filtered11" ),
    inputTag2 = cms.InputTag( "hltFilterMu11PFTau15" ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
hltPreIsoMu9PFTau15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltFilterIsoMu9PFTau15CaloJet8 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJets8" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 8.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltFilterIsoMu9PFTau15PFJet15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIcone5ConvPFJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltFilterIsoMu9PFTau15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltConvPFTaus" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltOverlapFilterIsoMu9PFTau15 = cms.EDFilter( "HLT2MuonTau",
    inputTag1 = cms.InputTag( "hltSingleMuIsoL3IsoFiltered9" ),
    inputTag2 = cms.InputTag( "hltFilterIsoMu9PFTau15" ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
hltPreIsoEle12PFTau15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional" ),
    etcutEB = cms.double( 12.0 ),
    etcutEE = cms.double( 12.0 ),
    ncandcut = cms.int32( 1 ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolR9ShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter" ),
    isoTag = cms.InputTag( "hltL1IsoR9shape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolR9ShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter" ),
    isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
    L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter" ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter" ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi','Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi','Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.08 ),
    thrRegularEE = cms.double( 0.08 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter = cms.EDFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter" ),
    isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
    nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.15 ),
    thrOverPtEE = cms.double( 0.1 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
    L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
    useEt = cms.untracked.bool( True )
)
hltFilterIsoEle12PFTau15CaloJet8 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIterativeCone5CaloJets8" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 8.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltPreOverlapFilterElectronTauCaloJet = cms.EDFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter" ),
    inputTag2 = cms.InputTag( "hltFilterIsoEle12PFTau15CaloJet8" ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 9999.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 9999.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 99999.0 ),
    MinN = cms.int32( 1 )
)
hltFilterIsoEle12PFTau15PFJet15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltIcone5ConvPFJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltFilterIsoEle12PFTau15 = cms.EDFilter( "HLT1Tau",
    inputTag = cms.InputTag( "hltConvPFTaus" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
hltOverlapFilterIsoEle12PFTau15 = cms.EDFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter" ),
    inputTag2 = cms.InputTag( "hltFilterIsoEle12PFTau15" ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
hltL1sZeroBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "4" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreZeroBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreZeroBiasPixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPixelCandsForMinBias = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltPixelTracksForMinBias" ),
    particleType = cms.string( "pi+" )
)
hltMinBiasPixelFilter1 = cms.EDFilter( "HLTPixlMBFilt",
    pixlTag = cms.InputTag( "hltPixelCandsForMinBias" ),
    MinPt = cms.double( 0.0 ),
    MinTrks = cms.uint32( 1 ),
    MinSep = cms.double( 1.0 )
)
hltPreMinBiasPixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1TechBSCminBiasOR = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( 'L1Tech_BSC_minBias_OR' ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
hltPreMultiVertex6 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPixelVerticesForMultiVertex = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.3 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 0.5 ),
    TrackCollection = cms.InputTag( "hltPixelTracks" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Method2 = cms.bool( True )
)
hltVertexFilter6 = cms.EDFilter( "HLTVertexFilter",
    inputTag = cms.InputTag( "hltPixelVerticesForMultiVertex" ),
    minNDoF = cms.double( 0.0 ),
    maxChi2 = cms.double( 99999.0 ),
    maxD0 = cms.double( 1.0 ),
    maxZ = cms.double( 15.0 ),
    minVertices = cms.uint32( 6 )
)
hltL1sETT60 = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETT60" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreMultiVertex8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltVertexFilter8 = cms.EDFilter( "HLTVertexFilter",
    inputTag = cms.InputTag( "hltPixelVerticesForMultiVertex" ),
    minNDoF = cms.double( 0.0 ),
    maxChi2 = cms.double( 99999.0 ),
    maxD0 = cms.double( 1.0 ),
    maxZ = cms.double( 15.0 ),
    minVertices = cms.uint32( 8 )
)
hltL1sL1BptxXORBscMinBiasOR = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BptxXOR_BscMinBiasOR" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1BptxXORBscMinBiasOR = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreL1TechBSCminBiasOR = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreL1TechBSCminBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1TechBSCminBias = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( 'L1Tech_BSC_minBias_inner_threshold1',
      'L1Tech_BSC_minBias_inner_threshold2',
      'L1Tech_BSC_minBias_threshold1',
      'L1Tech_BSC_minBias_threshold2' ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
hltPreL1TechBSChalo = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1TechBSChalo = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( 'L1Tech_BSC_halo_beam2_inner',
      'L1Tech_BSC_halo_beam2_outer',
      'L1Tech_BSC_halo_beam1_inner',
      'L1Tech_BSC_halo_beam1_outer' ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
hltPreL1TechBSChalo_forPhysicsBackground = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sHighMultiplicityBSC = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "35" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreHighMultiplicityBSC = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1TechRPCTTURBst1collisions = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "31" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1TechRPCTTURBst1collisions = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreL1HFTech = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1TechHCALHF = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( 'L1Tech_HCAL_HF_MM_or_PP_or_PM',
      'L1Tech_HCAL_HF_coincidence_PM',
      'L1Tech_HCAL_HF_MMP_or_MPP' ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
hltL1sTrackerCosmics = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "25" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreTrackerCosmics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltTrackerCosmicsPattern = cms.EDFilter( "HLTLevel1Pattern",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    triggerBit = cms.string( "L1Tech_RPC_TTU_pointing_Cosmics.v0" ),
    daqPartitions = cms.uint32( 1 ),
    ignoreL1Mask = cms.bool( False ),
    invert = cms.bool( False ),
    throw = cms.bool( True ),
    bunchCrossings = cms.vint32( -2, -1, 0, 1, 2 ),
    triggerPattern = cms.vint32( 1, 1, 1, 0, 0 )
)
hltL1sRPCBarrelCosmics = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "24" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreRPCBarrelCosmics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPrePixelTracksMultiplicity70 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPixelVerticesForHighMult = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 0.2 ),
    TrackCollection = cms.InputTag( "hltPixelTracksForHighMult" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Method2 = cms.bool( True )
)
hltPixelCandsForHighMult = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltPixelTracksForHighMult" ),
    particleType = cms.string( "pi+" )
)
hlt1HighMult70 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
    trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
    MinPt = cms.double( 0.2 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.0 ),
    MaxVz = cms.double( 10.0 ),
    MinTrks = cms.int32( 70 ),
    MinSep = cms.double( 0.12 )
)
hltPrePixelTracksMultiplicity85 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1HighMult85 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
    trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
    MinPt = cms.double( 0.2 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.0 ),
    MaxVz = cms.double( 10.0 ),
    MinTrks = cms.int32( 85 ),
    MinSep = cms.double( 0.12 )
)
hltPrePixelTracksMultiplicity100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hlt1HighMult100 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
    trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
    MinPt = cms.double( 0.2 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.0 ),
    MaxVz = cms.double( 10.0 ),
    MinTrks = cms.int32( 100 ),
    MinSep = cms.double( 0.12 )
)
hltL1sGlobalRunHPDNoise = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U_NotBptxOR" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreGlobalRunHPDNoise = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sTechTrigHCALNoise = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "11 OR 12" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltL1sNotBptxPlusOrMinus = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "NOT L1_BptxPlusORMinus" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreTechTrigHCALNoise = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1BPTX = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "3" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1BPTX = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1BPTXMinusOnly = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BptxMinus_NotBptxPlus" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1BPTXMinusOnly = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltL1sL1BPTXPlusOnly = cms.EDFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BptxPlus_NotBptxMinus" ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" )
)
hltPreL1BPTXPlusOnly = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltPreLogMonitor = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" )
)
hltLogMonitorFilter = cms.EDFilter( "HLTLogMonitorFilter",
    default_threshold = cms.uint32( 10 ),
    categories = cms.VPSet( 
    )
)
hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
hltBoolTrue = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 1.0 ),
    TrackCollection = cms.InputTag( "hltPixelTracks" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Method2 = cms.bool( True )
)

HLTDoLocalHcalSequence = cms.Sequence( hltHcalDigis + hltHbhereco + hltHfreco + hltHoreco )
HLTDoCaloSequence = cms.Sequence( hltEcalRawToRecHitFacility + hltEcalRegionalRestFEDs + hltEcalRecHitAll + HLTDoLocalHcalSequence + hltTowerMakerForAll )
HLTRecoJetSequenceU = cms.Sequence( HLTDoCaloSequence + hltIterativeCone5CaloJets + hltMCJetCorJetIcone5HF07 )
HLTDoRegionalJetEcalSequence = cms.Sequence( hltEcalRawToRecHitFacility + hltEcalRegionalJetsFEDs + hltEcalRegionalJetsRecHit )
HLTRecoJetRegionalSequence = cms.Sequence( HLTDoRegionalJetEcalSequence + HLTDoLocalHcalSequence + hltTowerMakerForJets + hltIterativeCone5CaloJetsRegional )
HLTRecoMETSequence = cms.Sequence( HLTDoCaloSequence + hltMet )
HLTRSequence = cms.Sequence( HLTRecoJetSequenceU + HLTRecoMETSequence + hltRHemisphere )
HLTDoJet20UHTRecoSequence = cms.Sequence( hltJet20UHt )
HLTmuonlocalrecoSequence = cms.Sequence( cms.SequencePlaceholder( "simMuonDTDigis" ) + hltDt1DRecHits + hltDt4DSegments + cms.SequencePlaceholder( "simMuonCSCDigis" ) + hltCsc2DRecHits + hltCscSegments + cms.SequencePlaceholder( "simMuonRPCDigis" ) + hltRpcRecHits )
HLTL2muonrecoNocandSequence = cms.Sequence( HLTmuonlocalrecoSequence + hltL2MuonSeeds + hltL2Muons )
HLTL2muonrecoSequenceNoVtx = cms.Sequence( HLTL2muonrecoNocandSequence + hltL2MuonCandidatesNoVtx )
HLTL2muonrecoSequence = cms.Sequence( HLTL2muonrecoNocandSequence + hltL2MuonCandidates )
HLTL3muonTkCandidateSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL3TrajSeedOIState + hltL3TrackCandidateFromL2OIState + hltL3TkTracksFromL2OIState + hltL3MuonsOIState + hltL3TrajSeedOIHit + hltL3TrackCandidateFromL2OIHit + hltL3TkTracksFromL2OIHit + hltL3MuonsOIHit + hltL3TkFromL2OICombination + hltL3TrajSeedIOHit + hltL3TrackCandidateFromL2IOHit + hltL3TkTracksFromL2IOHit + hltL3MuonsIOHit + hltL3TrajectorySeed + hltL3TrackCandidateFromL2 )
HLTL3muonrecoNocandSequence = cms.Sequence( HLTL3muonTkCandidateSequence + hltL3TkTracksFromL2 + hltL3MuonsLinksCombination + hltL3Muons )
HLTL3muonrecoSequence = cms.Sequence( HLTL3muonrecoNocandSequence + hltL3MuonCandidates )
HLTL2muonisorecoSequence = cms.Sequence( hltEcalRawToRecHitFacility + hltEcalRegionalMuonsFEDs + hltEcalRegionalMuonsRecHit + HLTDoLocalHcalSequence + hltTowerMakerForMuons + hltL2MuonIsolations )
HLTL3muonisorecoSequence = cms.Sequence( hltPixelTracks + hltL3MuonIsolations )
HLTL3muonTkCandidateSequenceNoVtx = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL3TrajectorySeedNoVtx + hltL3TrackCandidateFromL2NoVtx )
HLTL3muonrecoNocandSequenceNoVtx = cms.Sequence( HLTL3muonTkCandidateSequenceNoVtx + hltL3TkTracksFromL2NoVtx + hltL3MuonsNoVtx )
HLTL3muonrecoSequenceNoVtx = cms.Sequence( HLTL3muonrecoNocandSequenceNoVtx + hltL3MuonCandidatesNoVtx )
HLTDoRegionalEgammaEcalSequence = cms.Sequence( hltESRawToRecHitFacility + hltEcalRawToRecHitFacility + hltEcalRegionalEgammaFEDs + hltEcalRegionalEgammaRecHit + hltESRegionalEgammaRecHit )
HLTMulti5x5SuperClusterL1Isolated = cms.Sequence( hltMulti5x5BasicClustersL1Isolated + hltMulti5x5SuperClustersL1Isolated + hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated + hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated )
HLTL1IsolatedEcalClustersSequence = cms.Sequence( hltHybridSuperClustersL1Isolated + hltCorrectedHybridSuperClustersL1Isolated + HLTMulti5x5SuperClusterL1Isolated )
HLTMulti5x5SuperClusterL1NonIsolated = cms.Sequence( hltMulti5x5BasicClustersL1NonIsolated + hltMulti5x5SuperClustersL1NonIsolated + hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated + hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp + hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated )
HLTL1NonIsolatedEcalClustersSequence = cms.Sequence( hltHybridSuperClustersL1NonIsolated + hltCorrectedHybridSuperClustersL1NonIsolatedTemp + hltCorrectedHybridSuperClustersL1NonIsolated + HLTMulti5x5SuperClusterL1NonIsolated )
HLTEgammaR9ShapeSequence = cms.Sequence( hltL1IsoR9shape + hltL1NonIsoR9shape )
HLTDoLocalHcalWithoutHOSequence = cms.Sequence( hltHcalDigis + hltHbhereco + hltHfreco )
HLTSingleElectronEt10L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt10PixelMatchFilter )
HLTPixelMatchElectronL1IsoTrackingSequence = cms.Sequence( hltCkfL1IsoTrackCandidates + hltCtfL1IsoWithMaterialTracks + hltPixelMatchElectronsL1Iso )
HLTPixelMatchElectronL1NonIsoTrackingSequence = cms.Sequence( hltCkfL1NonIsoTrackCandidates + hltCtfL1NonIsoWithMaterialTracks + hltPixelMatchElectronsL1NonIso )
HLTSingleElectronEt12L1NonIsoHLTTighterEleIdSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter + HLTPixelMatchElectronL1IsoTrackingSequence + HLTPixelMatchElectronL1NonIsoTrackingSequence + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDphiFilter )
HLTSingleElectronEt17L1NonIsoHLTnonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt17PixelMatchFilter )
HLTSingleElectronEt17L1NonIsoHLTIsolSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolClusterShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolPixelMatchFilter + hltCkfL1IsoTrackCandidates + hltCtfL1IsoWithMaterialTracks + hltPixelMatchElectronsL1Iso + hltCkfL1NonIsoTrackCandidates + hltCtfL1NonIsoWithMaterialTracks + hltPixelMatchElectronsL1NonIso + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolDphiFilter + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsoElectronTrackIsol + hltL1NonIsoElectronTrackIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17IsolTrackIsolFilter )
HLTSingleElectronEt17L1NonIsoHLTTighterEleIdIsolSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter + hltCkfL1IsoTrackCandidates + hltCtfL1IsoWithMaterialTracks + hltPixelMatchElectronsL1Iso + hltCkfL1NonIsoTrackCandidates + hltCtfL1NonIsoWithMaterialTracks + hltPixelMatchElectronsL1NonIso + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsoElectronTrackIsol + hltL1NonIsoElectronTrackIsol + hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolTrackIsolFilter )
HLTEcalActivitySequence = cms.Sequence( hltEcalRawToRecHitFacility + hltESRawToRecHitFacility + hltEcalRegionalRestFEDs + hltEcalRegionalESRestFEDs + hltEcalRecHitAll + hltESRecHitAll + hltHybridSuperClustersActivity + hltCorrectedHybridSuperClustersActivity + hltMulti5x5BasicClustersActivity + hltMulti5x5SuperClustersActivity + hltMulti5x5SuperClustersWithPreshowerActivity + hltCorrectedMulti5x5SuperClustersWithPreshowerActivity + hltRecoEcalSuperClusterActivityCandidate + hltEcalActivitySuperClusterWrapper )
HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdEle8HE = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEPixelMatchFilter + HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter + hltActivityR9Shape + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter + hltActivityStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoublePixelMatchFilter )
HLTSingleElectronEt22L1NonIsoHLTnonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt22L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt22EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt22R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt22HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt22PixelMatchFilter )
HLTSingleElectronEt22L1NonIsoHLTTighterCaloIdIsolIsolSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolClusterShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloldIsolEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolPixelMatchFilter + hltCkfL1IsoTrackCandidates + hltCtfL1IsoWithMaterialTracks + hltPixelMatchElectronsL1Iso + hltCkfL1NonIsoTrackCandidates + hltCtfL1NonIsoWithMaterialTracks + hltPixelMatchElectronsL1NonIso + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolDphiFilter + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsoElectronTrackIsol + hltL1NonIsoElectronTrackIsol + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterCaloIdIsolTrackIsolFilter )
HLTSingleElectronEt22L1NonIsoHLTTighterEleIdSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdHEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdPixelMatchFilter + HLTPixelMatchElectronL1IsoTrackingSequence + HLTPixelMatchElectronL1NonIsoTrackingSequence + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt22TighterEleIdDphiFilter )
HLTSingleElectronEt32L1NonIsoHLTTighterEleIdSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdHEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdPixelMatchFilter + HLTPixelMatchElectronL1IsoTrackingSequence + HLTPixelMatchElectronL1NonIsoTrackingSequence + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt32TighterEleIdDphiFilter )
HLTDoubleElectronEt17L1NonIsoHLTnonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoDoubleElectronEt17L1MatchFilterRegional + hltL1NonIsoHLTNonIsoDoubleElectronEt17EtFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoDoubleElectronEt17HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoDoubleElectronEt17PixelMatchFilter )
HLTSinglePhoton10L1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter + hltL1IsoR9shape + hltL1NonIsoR9shape + hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt10HEFilter )
HLTSinglePhotonEt17IsolSC17HEL1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HER9ShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + HLTDoLocalHcalWithoutHOSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEEcalIsolFilter + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsolatedPhotonHollowTrackIsol + hltL1NonIsolatedPhotonHollowTrackIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HETrackIsolFilter + HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleEtFilter + hltActivityR9Shape + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleR9ShapeFilter + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt17IsolSC17HEDoubleHEFilter )
HLTSinglePhoton20L1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt20HEFilter )
HLTSinglePhoton20CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedHEFilter )
HLTSinglePhoton20IsolCleanedL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonE20IsolCleanedR9ShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsolatedPhotonHollowTrackIsol + hltL1NonIsolatedPhotonHollowTrackIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt20IsolCleanedTrackIsolFilter )
HLTSinglePhotonEt22SC22HEL1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HER9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEHEFilter + HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleEtFilter + hltActivityR9Shape + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleR9ShapeFilter + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt22SC22HEDoubleHEFilter )
HLTSinglePhoton30CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedHEFilter )
HLTSinglePhoton40CaloIdCleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt40CaloIdCleanedHEFilter )
HLTSinglePhoton40IsolCleanedL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonE40IsolCleanedR9ShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsolatedPhotonHollowTrackIsol + hltL1NonIsolatedPhotonHollowTrackIsol + hltL1NonIsoHLTNonIsoSinglePhotonEt40IsolCleanedTrackIsolFilter )
HLTSinglePhoton50CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedHEFilter )
HLTSinglePhoton50L1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt50HEFilter )
HLTSinglePhoton70CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt70CleanedHEFilter )
HLTSinglePhoton110NoHECleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedEtFilter + hltL1IsoR9shape + hltL1NonIsoR9shape + hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt110NoHECleanedHEFilter )
HLTDoublePhotonEt5Sequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltDoublePhotonEt5L1MatchFilterRegional + hltDoublePhotonEt5EtPhiFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltDoublePhotonEt5EcalIsolFilter + HLTDoLocalHcalSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltDoublePhotonEt5HEFilter )
HLTDoublePhotonEt17SingleIsolL1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolL1MatchFilterRegional + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolLooseHEFilter + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHEFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolEcalIsolFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsolatedPhotonHollowTrackIsol + hltL1NonIsolatedPhotonHollowTrackIsol + hltL1NonIsoHLTNonIsoDoublePhotonEt17SingleIsolTrackIsolFilter )
HLTDoublePhotonEt22L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoDoublePhotonEt22L1MatchFilterRegional + hltL1NonIsoHLTNonIsoDoublePhotonEt22EtFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoDoublePhotonEt22HEFilter )
HLTCaloTausCreatorRegionalSequence = cms.Sequence( HLTDoRegionalJetEcalSequence + HLTDoLocalHcalSequence + hltTowerMakerForJets + hltCaloTowersTau1Regional + hltIconeTau1Regional + hltCaloTowersTau2Regional + hltIconeTau2Regional + hltCaloTowersTau3Regional + hltIconeTau3Regional + hltCaloTowersTau4Regional + hltIconeTau4Regional + hltCaloTowersCentral1Regional + hltIconeCentral1Regional + hltCaloTowersCentral2Regional + hltIconeCentral2Regional + hltCaloTowersCentral3Regional + hltIconeCentral3Regional + hltCaloTowersCentral4Regional + hltIconeCentral4Regional )
HLTL2TauJetsSequence = cms.Sequence( HLTCaloTausCreatorRegionalSequence + hltL2TauJets )
HLTL2TauEcalIsolationSequence = cms.Sequence( hltL2TauNarrowConeIsolationProducer + hltL2TauRelaxingIsolationSelector )
HLTMETWithTausSequence = cms.Sequence( hltEcalRegionalRestFEDs + hltEcalRecHitAll + hltTowerMakerForAll + hltMet )
HLTL25TauSingleTrack15IsolationSequence = cms.Sequence( hltL25TauJetTracksAssociator + hltL25TauConeIsolation + hltL25TauLeadingTrackPtCut15Selector )
HLTL3TauSingleTrack15IsolationSequence = cms.Sequence( hltL3TauSingleTrack15JetTracksAssociator + hltL3TauSingleTrack15ConeIsolation + hltL3TauSingleTrack15IsolationSelector )
HLTL25TauTrackIsolationSequence = cms.Sequence( hltL25TauJetTracksAssociator + hltL25TauConeIsolation + hltL25TauLeadingTrackPtCutSelector )
HLTL3TauTrackIsolationSequence = cms.Sequence( hltL3TauJetTracksAssociator + hltL3TauConeIsolation + hltL3TauIsolationSelector )
HLTBTagMuSequenceL25U = cms.Sequence( HLTL2muonrecoNocandSequence + hltSelector4JetsU + hltBSoftMuonL25JetsU + hltBSoftMuonL25TagInfosU + hltBSoftMuonL25BJetTagsUByDR )
HLTBTagMuSequenceL3U = cms.Sequence( HLTL3muonrecoNocandSequence + hltBSoftMuonL3TagInfosU + hltBSoftMuonL3BJetTagsUByPt + hltBSoftMuonL3BJetTagsUByDR )
HLTBTagMuSelSequenceL3U = cms.Sequence( HLTL3muonrecoNocandSequence + hltBSoftMuonL3 + hltBSoftMuonSelL3TagInfosU + hltBSoftMuonSelL3BJetTagsUByPt + hltBSoftMuonSelL3BJetTagsUByDR )
HLTSinglePhoton13CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedEtFilter + hltL1IsoR9shape + hltL1NonIsoR9shape + hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSinglePhotonEt13CleanedHEFilter )
HLTSingleElectronEt13L1NonIsoHLTnonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt13L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt13EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt13R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt13HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt13PixelMatchFilter )
HLTMu5Ele17ElectronSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoMu5Ele17L1MatchFilterRegional + hltL1NonIsoHLTNonIsoMu5Ele17EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoMu5Ele17R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoMu5Ele17HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoMu5Ele17PixelMatchFilter )
HLTSingleMu8Ele8L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSingleMu8Ele8EtFilter + hltActivityR9shape + hltL1NonIsoHLTNonIsoSingleMu8Ele8R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleMu8Ele8HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltActivityStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleMu8Ele8PixelMatchFilter )
HLTSingleMu11Ele8L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSingleMu11Ele8EtFilter + hltActivityR9shape + hltL1NonIsoHLTNonIsoSingleMu11Ele8R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleMu11Ele8HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltActivityStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleMu11Ele8PixelMatchFilter )
HLTSingleMu3Ele8HT70UL1NonIsoHLTNonIsoSequence = cms.Sequence( HLTEcalActivitySequence + hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UEtFilter + hltActivityR9shape + hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UR9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltActivityPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UHEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltActivityStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleMu3Ele8HT70UPixelMatchFilter )
HLTSingleElectronEt10HT70L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt10HT70L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt10HT70EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt10HT70R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt10HT70HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt10HT70PixelMatchFilter )
HLTSingleElectronEt10L1NonIsoHLTTEleIdHT70Sequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70R9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70ClusterShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70PixelMatchFilter + HLTPixelMatchElectronL1IsoTrackingSequence + HLTPixelMatchElectronL1NonIsoTrackingSequence + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70OneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70DetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt10EleIdHT70DphiFilter )
HLTSingleElectronEt10HT100L1NonIsoHLTNonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt10HT100L1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt10HT100EtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt10HT100R9ShapeFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt10HT100HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt10HT100PixelMatchFilter )
HLTDoubleElectronEt8HT70L1NonIsoHLTnonIsoSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70L1MatchFilterRegional + hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70EtFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70HEFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoDoubleElectronEt8HT70PixelMatchFilter )
HLTRecoJetSequencePrePF = cms.Sequence( HLTDoCaloSequence + hltIterativeCone5CaloJets + hltIterativeCone5CaloJets8 )
HLTPreshowerSequence = cms.Sequence( hltESRawToRecHitFacility + hltEcalRegionalESRestFEDs + hltESRecHitAll )
HLTParticleFlowSequence = cms.Sequence( HLTPreshowerSequence + hltParticleFlowRecHitECAL + hltParticleFlowRecHitHCAL + hltParticleFlowRecHitPS + hltParticleFlowClusterECAL + hltParticleFlowClusterHCAL + hltParticleFlowClusterHFEM + hltParticleFlowClusterHFHAD + hltParticleFlowClusterPS + hltLightPFTracks + hltParticleFlowBlock + hltParticleFlow )
HLTPFJetsSequence = cms.Sequence( hltIcone5PFJets + hltIcone5ConvPFJets )
HLTPFJetTriggerSequence = cms.Sequence( HLTRecopixelvertexingSequence + HLTTrackReconstructionForJets + HLTParticleFlowSequence + HLTPFJetsSequence )
HLTPFTauSequence = cms.Sequence( hltPFTauJetTracksAssociator + hltPFTauTagInfo + hltPFTaus + hltPFTauTrackFindingDiscriminator + hltPFTauIsolationDiscriminator + hltSelectedPFTaus + hltConvPFTaus )
HLTSingleElectronEt12L1NonIsoHLTTighterEleIdIsolSequence = cms.Sequence( HLTDoRegionalEgammaEcalSequence + HLTL1IsolatedEcalClustersSequence + HLTL1NonIsolatedEcalClustersSequence + hltL1IsoRecoEcalCandidate + hltL1NonIsoRecoEcalCandidate + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter + HLTEgammaR9ShapeSequence + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolR9ShapeFilter + hltL1IsoHLTClusterShape + hltL1NonIsoHLTClusterShape + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter + hltL1IsolatedPhotonEcalIsol + hltL1NonIsolatedPhotonEcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter + HLTDoLocalHcalWithoutHOSequence + hltL1IsolatedPhotonHcalForHE + hltL1NonIsolatedPhotonHcalForHE + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter + hltL1IsolatedPhotonHcalIsol + hltL1NonIsolatedPhotonHcalIsol + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL1IsoStartUpElectronPixelSeeds + hltL1NonIsoStartUpElectronPixelSeeds + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter + hltCkfL1IsoTrackCandidates + hltCtfL1IsoWithMaterialTracks + hltPixelMatchElectronsL1Iso + hltCkfL1NonIsoTrackCandidates + hltCtfL1NonIsoWithMaterialTracks + hltPixelMatchElectronsL1NonIso + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter + hltElectronL1IsoDetaDphi + hltElectronL1NonIsoDetaDphi + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter + HLTL1IsoEgammaRegionalRecoTrackerSequence + HLTL1NonIsoEgammaRegionalRecoTrackerSequence + hltL1IsoElectronTrackIsol + hltL1NonIsoElectronTrackIsol + hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter )
HLTRecopixelvertexingForMultiVertexSequence = cms.Sequence( hltPixelTracks + hltPixelVerticesForMultiVertex )
HLTRecopixelvertexingForHighMultSequence = cms.Sequence( hltPixelTracksForHighMult + hltPixelVerticesForHighMult )

HLTriggerFirstPath = cms.Path( hltGetRaw + hltBoolFalse )
HLT_Activity_CSC = cms.Path( HLTBeginSequenceBPTX + hltL1sL1BscMinBiasORBptxPlusANDMinus + hltPreActivityCSC + cms.SequencePlaceholder( "simMuonCSCDigis" ) + hltCSCActivityFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Jet6U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1Jet6U + hltPreL1Jet6U_BPTX + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Jet10U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1Jet10U + hltPreL1Jet10U_BPTX + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet15U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet6U + hltPreJet15U + HLTRecoJetSequenceU + hlt1jet15U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet30U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sJet30U + hltPreJet30U + HLTRecoJetSequenceU + hlt1jet30U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sJet50U + hltPreJet50U + HLTRecoJetSequenceU + hlt1jet50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet70U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet40U + hltPreJet70U + HLTRecoJetSequenceU + hlt1jet70U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet100U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet60U + hltPreJet100U + HLTRecoJetSequenceU + hlt1jet100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet140U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet60U + hltPreJet140U + HLTRecoJetSequenceU + hlt1jet140U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Jet180U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet60U + hltPreJet180U + HLTRecoJetSequenceU + hlt1jet180U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve15U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet6U + hltPreDiJetAve15U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve15U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve30U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreDiJetAve30U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve30U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet30U + hltPreDiJetAve50U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve70U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet40U + hltPreDiJetAve70U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve70U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve100U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet60U + hltPreDiJetAve100U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJetAve140U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet60U + hltPreDiJetAve140U + HLTDoCaloSequence + hltIterativeCone5CaloJets + hltDiJetAve140U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleJet15U_ForwardBackward_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleForJet10UEtaOpp + hltPreDoubleJet15UForwardBackward + HLTRecoJetRegionalSequence + hltDoubleJet15UForwardBackward + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleJet25U_ForwardBackward_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleForJet10UEtaOpp + hltPreDoubleJet25UForwardBackward + HLTRecoJetRegionalSequence + hltDoubleJet25UForwardBackward + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleJet35U_ForwardBackward_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleForJet10UEtaOpp + hltPreDoubleJet35UForwardBackward + HLTRecoJetRegionalSequence + hltDoubleJet35UForwardBackward + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJet20U_Meff180U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreDiJet20UMeff180U + HLTRecoJetSequenceU + hltDiJet20UMeff180U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiJet50U_PT50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet30U + hltPreDiJet50UPT50U + HLTRecoJetSequenceU + hltDiJet50UPT50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_ExclDiJet30U_HFAND_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreExclDiJet30UHFAND + HLTRecoJetSequenceU + hltExclDiJet30UAND + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_ExclDiJet30U_HFOR_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreExclDiJet30UHFOR + HLTRecoJetSequenceU + hltExclDiJet30UOR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_QuadJet15U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1QuadJet8U + hltPreQuadJet15U + HLTRecoJetSequenceU + hlt4jet15U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_QuadJet20U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1QuadJet8U + hltPreQuadJet20U + HLTRecoJetSequenceU + hlt4jet20U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_QuadJet25U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1QuadJet8U + hltPreQuadJet25U + HLTRecoJetSequenceU + hlt4jet25U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_R010U_MR50U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreR010UMR50U + HLTRSequence + hltR010UMR50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_R030U_MR100U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreR030UMR100U + HLTRSequence + hltR030UMR100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_R033U_MR100U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreR033UMR100U + HLTRSequence + hltR033UMR100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_RP025U_MR70U = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet20U + hltPreRP025UMR70U + HLTRSequence + hltRP025UMR70U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1ETT100 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETT100 + hltPreL1ETT100 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_EcalOnly_SumEt160_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETT140 + hltPreEcalOnlySumEt160 + hltEcalRawToRecHitFacility + hltEcalRegionalRestFEDs + hltEcalRecHitAll + hltTowerMakerForEcalBarrelOnly + hltEcalOnlyMet + hlt1EcalOnlySumET160 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1MET20 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1MET20 + hltPreL1MET20 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET45_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETM30 + hltPreMET45 + HLTRecoMETSequence + hlt1MET45 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET45_DiJet30U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1MET20 + hltPreMET45DiJet30U + HLTRecoMETSequence + hlt1MET45 + HLTRecoJetSequenceU + hlt2jet30U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET65_CenJet50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETM30 + hltPreMET65Jet50U + HLTRecoMETSequence + hlt1MET65 + HLTRecoJetSequenceU + hlt1cenjet50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET80_CenJet50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETM30 + hltPreMET80Jet50U + HLTRecoMETSequence + hlt1MET65 + HLTRecoJetSequenceU + hlt1cenjet50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET100_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETM30 + hltPreMET100 + HLTRecoMETSequence + hlt1MET100 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MET120_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETM30 + hltPreMET120 + HLTRecoMETSequence + hlt1MET120 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleJet10U + hltPreHT50U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT100U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT100U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT130U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT130U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT130U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT140U_J30U_Eta3_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT140UJ30UEta3 + HLTRecoJetSequenceU + hltJetEta3Ht + hltJet30UEta3Ht + hltHT140UJ30Eta3 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT150U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT150U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT150U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT150U_Eta3_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT150UEta3 + HLTRecoJetSequenceU + hltJetEta3Ht + hltJet20UEta3Ht + hltHT150UEta3 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT160U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT160U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT160U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT160U_Eta3_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT160UEta3 + HLTRecoJetSequenceU + hltJetEta3Ht + hltJet20UEta3Ht + hltHT160UEta3 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_HT200U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1HTT50 + hltPreHT200U + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT200U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1MuOpen_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMuOpen + hltPreL1MuOpen_BPTX + hltL1MuOpenL1Filtered0 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1MuOpen_DT_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMuOpen + hltPreL1MuOpenDT + hltL1MuOpenL1FilteredDT + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Mu7_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreL1Mu7 + hltL1Mu7L1Filtered0 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Mu20 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu20 + hltPreL1Mu20 + hltL1Mu20L1Filtered20 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L2Mu0_NoVertex = cms.Path( HLTBeginSequence + hltL1sL1SingleMu0 + hltPreL2Mu0NoVertex + hltSingleMu0L1Filtered + HLTL2muonrecoSequenceNoVtx + hltSingleL2Mu0L2PreFilteredNoVtx + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L2Mu7_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreL2Mu7 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L2Mu30_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreL2Mu30 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu30L2Filtered30 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu0_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu0 + hltPreMu0 + hltL1SingleMu0L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu0L2Filtered0 + HLTL3muonrecoSequence + hltSingleMu0L3Filtered0 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu3_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu0 + hltPreMu3 + hltL1SingleMu0L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu3L2Filtered3 + HLTL3muonrecoSequence + hltSingleMu3L3Filtered3 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu3 + hltPreMu5 + hltL1SingleMu3L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu5L2Filtered4 + HLTL3muonrecoSequence + hltSingleMu5L3Filtered5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu7 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu5 + hltPreMu7 + hltL1SingleMu5L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu7L2Filtered5 + HLTL3muonrecoSequence + hltSingleMu7L3Filtered7 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu9 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu9 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu9L3Filtered9 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu11 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu11 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu11L3Filtered11 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu13_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu13 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu13L3Filtered13 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu15_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu15 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu15L3Filtered15 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu17_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu17 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu17L3Filtered17 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu19_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu19 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu19L3Filtered19 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu21_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu21 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu21L3Filtered21 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu25_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu25 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu21L3Filtered25 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu9_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu9 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered9 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered9 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu11_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu11 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered11 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered11 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu13_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu13 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered13 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered13 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu15_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu15 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered15 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered15 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu17_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu17 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered17 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered17 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu30_NoVertex_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleMu7 + hltPreMu30NoVertex + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequenceNoVtx + hltMu30NoVertexL2PreFiltered + HLTL3muonrecoSequenceNoVtx + hltMu30NoVertexL3PreFiltered30 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1DoubleMuOpen = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreL1DoubleMuOpen + hltDoubleMuLevel1PathL1OpenFiltered + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L2DoubleMu0 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreL2DoubleMu0 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L2DoubleMu20_NoVertex_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMuOpen + hltPreL2DoubleMu20NoVertex + hltDiMuonL1Filtered0 + HLTL2muonrecoSequenceNoVtx + hltL2DoubleMu20NoVertexL2PreFiltered + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu0 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreDoubleMu0 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltDiMuonL3PreFiltered0 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu0_Quarkonium_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreDoubleMu0Quark + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltDoubleMu0QuarkoniumL3PreFiltered + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu3_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreDoubleMu3 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltDiMuonL3PreFiltered3 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu5_v1 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreDoubleMu5 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltDiMuonL3PreFiltered5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_L2Mu0 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreMu5L2Mu0 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltMu5L2Mu0L3Filtered5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1SingleEG8 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreL1SingleEG8 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele10_SW_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG5 + hltPreEle10SWL1R + HLTSingleElectronEt10L1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele12_SW_TighterEleId_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle12SWTighterEleIdL1R + HLTSingleElectronEt12L1NonIsoHLTTighterEleIdSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_SW_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle17SWL1R + HLTSingleElectronEt17L1NonIsoHLTnonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_SW_Isol_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle17SWIsolL1R + HLTSingleElectronEt17L1NonIsoHLTIsolSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_SW_TighterEleIdIsol_L1R_v3 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle17SWTighterEleIdIsolL1R + HLTSingleElectronEt17L1NonIsoHLTTighterEleIdIsolSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle17TightCaloEleIdEle8HEL1R + HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdEle8HE + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele22_SW_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle22SWL1R + HLTSingleElectronEt22L1NonIsoHLTnonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle22SWTighterCaloIdIsolL1R + HLTSingleElectronEt22L1NonIsoHLTTighterCaloIdIsolIsolSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele22_SW_TighterEleId_L1R_v3 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle22SWTighterEleIdL1R + HLTSingleElectronEt22L1NonIsoHLTTighterEleIdSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele32_SW_TighterEleId_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle32SWTighterEleIdL1R + HLTSingleElectronEt32L1NonIsoHLTTighterEleIdSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleEle17_SW_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG5 + hltPreDoubleEle17SWL1R + HLTDoubleElectronEt17L1NonIsoHLTnonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon10_Cleaned_L1R = cms.Path( HLTBeginSequence + hltL1sL1SingleEG5 + hltPrePhoton10L1R + HLTSinglePhoton10L1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon17_Isol_SC17HE_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreSinglePhoton17IsolSC17HEL1R + HLTSinglePhotonEt17IsolSC17HEL1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon20_NoHE_L1R = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton20L1R + HLTSinglePhoton20L1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon20_Cleaned_L1R = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton20CleanedL1R + HLTSinglePhoton20CleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon20_Isol_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePho20IsolL1R + HLTSinglePhoton20IsolCleanedL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon22_SC22HE_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreSinglePhoton22SC22HEL1R + HLTSinglePhotonEt22SC22HEL1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon30_Cleaned_L1R = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton30CleanedL1R + HLTSinglePhoton30CleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon40_CaloId_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton40CaloIdCleanedL1R + HLTSinglePhoton40CaloIdCleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon40_Isol_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePho40IsolL1R + HLTSinglePhoton40IsolCleanedL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon50_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton50HECleanedL1R + HLTSinglePhoton50CleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon50_NoHE_L1R = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton50L1R + HLTSinglePhoton50L1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon70_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton70HECleanedL1R + HLTSinglePhoton70CleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon110_NoHE_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPrePhoton110NoHECleanedL1R + HLTSinglePhoton110NoHECleanL1NonIsolatedHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoublePhoton5_CEP_L1R_v3 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG5 + hltPreDoublePhoton5CEPL1R + HLTDoublePhotonEt5Sequence + hltTowerMakerForHcal + hltHcalTowerFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoublePhoton17_SingleIsol_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG5 + hltPreSingleDoublePhoton17SingleIsolL1R + HLTDoublePhotonEt17SingleIsolL1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoublePhoton22_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG5 + hltPreDoublePhoton22L1R + HLTDoublePhotonEt22L1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_SingleIsoTau20_Trk15_MET25_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sSingleIsoTau20Trk15MET25 + hltPreSingleIsoTau20Trk15MET25 + HLTL2TauJetsSequence + hltFilterL2EtCutSingleIsoTau20Trk15MET25 + HLTL2TauEcalIsolationSequence + hltFilterL2EcalIsolationSingleIsoTau20Trk15MET25 + HLTMETWithTausSequence + hltFilterL2TauMET25 + HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTL25TauTrackReconstructionSequence + HLTL25TauSingleTrack15IsolationSequence + hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk15MET25 + HLTL3TauSingleTrack15ReconstructionSequence + HLTL3TauSingleTrack15IsolationSequence + hltL1HLTSingleIsoTau20Trk15MET25JetsMatch + hltFilterL3TrackIsolationSingleIsoTau20Trk15MET25 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_SingleIsoTau35_Trk15_MET25_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sSingleIsoTau35Trk15MET25 + hltPreSingleIsoTau35Trk15MET25 + HLTL2TauJetsSequence + hltFilterL2EtCutSingleIsoTau35Trk15MET25 + HLTL2TauEcalIsolationSequence + hltFilterL2EcalIsolationSingleIsoTau35Trk15MET25 + HLTMETWithTausSequence + hltFilterL2TauMET25 + HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTL25TauTrackReconstructionSequence + HLTL25TauSingleTrack15IsolationSequence + hltFilterL25LeadingTrackPtCutSingleIsoTau35Trk15MET25 + HLTL3TauSingleTrack15ReconstructionSequence + HLTL3TauSingleTrack15IsolationSequence + hltL1HLTSingleIsoTau35Trk15MET25JetsMatch + hltFilterL3TrackIsolationSingleIsoTau35Trk15MET25 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleIsoTau15_OneLeg_Trk5_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sDoubleOneLegIsoTau15Trk5 + hltPreDoubleOneLegIsoTau15Trk5 + HLTL2TauJetsSequence + hltFilterL2EtCutDoubleOneLegIsoTau15Trk5 + HLTL2TauEcalIsolationSequence + hltFilterL2EcalIsolationDoubleOneLegIsoTau15Trk5 + HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTL25TauTrackReconstructionSequence + HLTL25TauTrackIsolationSequence + hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch + hltFilterL25LeadingTrackPtCutDoubleOneLegIsoTau15Trk5 + HLTL3TauTrackReconstructionSequence + HLTL3TauTrackIsolationSequence + hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch + hltFilterL3TrackIsolationDoubleOneLegIsoTau15Trk5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleIsoTau15_Trk5_v4 = cms.Path( HLTBeginSequenceBPTX + hltL1sDoubleIsoTau15Trk5 + hltPreDoubleIsoTau15Trk5 + HLTL2TauJetsSequence + hltFilterL2EtCutDoubleIsoTau15Trk5 + HLTL2TauEcalIsolationSequence + hltFilterL2EcalIsolationDoubleIsoTau15Trk5 + HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTL25TauTrackReconstructionSequence + HLTL25TauTrackIsolationSequence + hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5 + HLTL3TauTrackReconstructionSequence + HLTL3TauTrackIsolationSequence + hltL1HLTDoubleIsoTau15Trk5JetsMatch + hltFilterL3TrackIsolationDoubleIsoTau15Trk5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagMu_DiJet10U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sBTagMuDiJet10U + hltPreBTagMuDiJet10U + HLTRecoJetSequenceU + hltBDiJet10U + HLTBTagMuSequenceL25U + hltBSoftMuonL25FilterUByDR + HLTBTagMuSequenceL3U + hltBSoftMuonL3FilterUByDR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagMu_DiJet20U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sBTagMuDiJet10U + hltPreBTagMuDiJet20U + HLTRecoJetSequenceU + hltBDiJet20U + HLTBTagMuSequenceL25U + hltBSoftMuonL25FilterUByDR + HLTBTagMuSequenceL3U + hltBSoftMuonL3FilterUByDR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagMu_DiJet30U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sBTagMuDiJet10U + hltPreBTagMuDiJet30U + HLTRecoJetSequenceU + hltBDiJet30U + HLTBTagMuSequenceL25U + hltBSoftMuonL25FilterUByDR + HLTBTagMuSequenceL3U + hltBSoftMuonL3FilterUByDR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagMu_DiJet20U_Mu5_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sBTagMuDiJet10U + hltPreBTagMuDiJet20UMu5 + HLTRecoJetSequenceU + hltBDiJet20U + HLTBTagMuSequenceL25U + hltBSoftMuonL25FilterUByDR + HLTBTagMuSelSequenceL3U + hltBSoftMuonSelL3FilterUByDR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagMu_DiJet30U_Mu5_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sBTagMuDiJet10U + hltPreBTagMuDiJet30UMu5 + HLTRecoJetSequenceU + hltBDiJet30U + HLTBTagMuSequenceL25U + hltBSoftMuonL25FilterUByDR + HLTBTagMuSelSequenceL3U + hltBSoftMuonSelL3FilterUByDR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_StoppedHSCP20_v3 = cms.Path( HLTBeginSequence + hltL1sL1SingleJet10UNotBptxOR + hltPreStoppedHSCP20 + hltHcalDigis + hltHbhereco + hltStoppedHSCPHpdFilter + hltStoppedHSCPTowerMakerForAll + hltStoppedHSCPIterativeCone5CaloJets + hltStoppedHSCP1CaloJetEnergy20 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_StoppedHSCP35_v3 = cms.Path( HLTBeginSequence + hltL1sL1SingleJet10UNotBptxOR + hltPreStoppedHSCP35 + hltHcalDigis + hltHbhereco + hltStoppedHSCPHpdFilter + hltStoppedHSCPTowerMakerForAll + hltStoppedHSCPIterativeCone5CaloJets + hltStoppedHSCP1CaloJetEnergy35 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu7_Photon13_Cleaned_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1Mu3EG5 + hltPreMu7Photon13CleanedL1R + HLTSinglePhoton13CleanL1NonIsolatedHLTNonIsoSequence + hltL1SingleMu3EG5L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu5EG5L2Filtered4 + HLTL3muonrecoSequence + hltSingleMu7EG5L3Filtered5 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_Ele13_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltL1sL1SingleMuOpenIgnorePrescale + hltPreMu5Ele13 + hltL1SingleMuOpenIgnorePrescaleL1Filtered0 + HLTL2muonrecoSequence + hltSingleMuIgnorePrescaleL2Filtered0 + HLTL3muonrecoSequence + hltSingleMuIgnorePrescaleL3Filtered5 + HLTSingleElectronEt13L1NonIsoHLTnonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_Ele17_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltL1sL1SingleMuOpenIgnorePrescale + hltPreMu5Ele17 + hltL1SingleMuOpenIgnorePrescaleL1Filtered0 + HLTL2muonrecoSequence + hltSingleMuIgnorePrescaleL2Filtered0 + HLTL3muonrecoSequence + hltSingleMuIgnorePrescaleL3Filtered5 + HLTMu5Ele17ElectronSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu8_Ele8_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleMu3 + hltPreMu8Ele8 + hltL1SingleMu3L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu5L2Filtered4 + HLTL3muonrecoSequence + hltSingleMu8L3Filtered5 + HLTSingleMu8Ele8L1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu11_Ele8_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleMu3 + hltPreMu11Ele8 + hltL1SingleMu3L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu5L2Filtered4 + HLTL3muonrecoSequence + hltSingleMu11L3Filtered5 + HLTSingleMu11Ele8L1NonIsoHLTNonIsoSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_Jet50U_v3 = cms.Path( HLTBeginSequence + hltL1sL1Mu3Jet10U + hltPreMu5Jet50U + hltL1Mu3Jet10UL1Filtered0 + HLTL2muonrecoSequence + hltL2Mu5Jet10UL2Filtered4 + HLTL3muonrecoSequence + hltL3Mu5Jet10UL3Filtered5 + HLTRecoJetSequenceU + hlt1jet50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_Jet70U_v3 = cms.Path( HLTBeginSequence + hltL1sL1Mu3Jet10U + hltPreMu5Jet70U + hltL1Mu3Jet10UL1Filtered0 + HLTL2muonrecoSequence + hltL2Mu5Jet10UL2Filtered4 + HLTL3muonrecoSequence + hltL3Mu5Jet10UL3Filtered5 + HLTRecoJetSequenceU + hlt1jet70U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_MET45_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu3 + hltL1sL1ETM20 + hltPreMu5MET45 + hltL1SingleMu3L1Filtered0 + HLTL2muonrecoSequence + hltSingleMu5L2Filtered4 + HLTL3muonrecoSequence + hltSingleMu5L3Filtered5 + HLTRecoMETSequence + hlt1MET45 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_HT70U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1Mu3Jet10U + hltPreMu5HT70U + hltL1Mu3Jet10UL1Filtered0 + HLTL2muonrecoSequence + hltL2Mu5Jet10UL2Filtered4 + HLTL3muonrecoSequence + hltL3Mu5Jet10UL3Filtered5 + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT70U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu5_HT100U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1Mu3Jet10U + hltPreMu5HT100U + hltL1Mu3Jet10UL1Filtered0 + HLTL2muonrecoSequence + hltL2Mu5Jet10UL2Filtered4 + HLTL3muonrecoSequence + hltL3Mu5Jet10UL3Filtered5 + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT100U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu3_HT50U_v3 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1DoubleMuOpen + hltPreDoubleMu3 + hltDiMuonL1Filtered0 + HLTL2muonrecoSequence + hltDiMuonL2PreFiltered0 + HLTL3muonrecoSequence + hltDiMuonL3PreFiltered3 + HLTRecoJetSequenceU + HLTDoJet20UHTRecoSequence + hltHT50U + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu3_Ele8_HT70U_v1 = cms.Path( HLTBeginSequence + hltL1sL1HTT50 + hltL1sL1SingleMuOpenIgnorePrescale + hltPreMu3Ele8HT70U + hltL1SingleMuOpenIgnorePrescaleL1Filtered0 + HLTL2muonrecoSequence + hltSingleMuIgnorePrescaleL2Filtered0 + HLTL3muonrecoSequence + hltSingleMuIgnorePrescaleL3Filtered3 + HLTSingleMu3Ele8HT70UL1NonIsoHLTNonIsoSequence + HLTRecoJetSequenceU + hltMCJetCorJetIcone5HF07Mu3Ele8HT70U + hltJet20UHtMu3Ele8HT70U + hltMu3Ele8HT70UHTFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele10_SW_HT70U_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle10HT70SWL1R + HLTSingleElectronEt10HT70L1NonIsoHLTNonIsoSequence + HLTRecoJetSequenceU + hltMCJetCorJetIcone5HF07Ele10Removed + hltJet20UHtEle10 + hltEle10HT70HTFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele10_SW_EleId_HT70U_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle10EleIdHT70SWL1R + HLTSingleElectronEt10L1NonIsoHLTTEleIdHT70Sequence + HLTRecoJetSequenceU + hltMCJetCorJetIcone5HF07Ele10EleIdRemoved + hltJet20UHtEle10EleId + hltEle10EleIdHT70HTFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele10_SW_HT100U_L1R_v2 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreEle10HT100SWL1R + HLTSingleElectronEt10HT100L1NonIsoHLTNonIsoSequence + HLTRecoJetSequenceU + hltMCJetCorJetIcone5HF07Ele10ForHT100Removed + hltJet20UHtEle10HT100 + hltEle10HT100HTFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleEle8_SW_HT70U_L1R_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG5 + hltPreDoubleEle8HT70SWL1R + HLTDoubleElectronEt8HT70L1NonIsoHLTnonIsoSequence + HLTRecoJetSequenceU + hltMCJetCorJetIcone5HF07DiEle8Removed + hltJet20UHtDiEle8 + hltDoubleEle8HT70HTFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu11_PFTau15_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreMu11PFTau15 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL3muonrecoSequence + hltSingleMu11L3Filtered11 + HLTRecoJetSequencePrePF + hltFilterMu11PFTau15CaloJet8 + HLTPFJetTriggerSequence + hltFilterMu11PFTau15PFJet15 + HLTPFTauSequence + hltFilterMu11PFTau15 + hltOverlapFilterMu11PFTau15 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu9_PFTau15_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1SingleMu7 + hltPreIsoMu9PFTau15 + hltL1SingleMu7L1Filtered0 + HLTL2muonrecoSequence + hltL2Mu7L2Filtered7 + HLTL2muonisorecoSequence + hltSingleMuIsoL2IsoFiltered7 + HLTL3muonrecoSequence + hltSingleMuIsoL3PreFiltered9 + HLTL3muonisorecoSequence + hltSingleMuIsoL3IsoFiltered9 + HLTRecoJetSequencePrePF + hltFilterIsoMu9PFTau15CaloJet8 + HLTPFJetTriggerSequence + hltFilterIsoMu9PFTau15PFJet15 + HLTPFTauSequence + hltFilterIsoMu9PFTau15 + hltOverlapFilterIsoMu9PFTau15 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoEle12_PFTau15_v3 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG8 + hltPreIsoEle12PFTau15 + HLTSingleElectronEt12L1NonIsoHLTTighterEleIdIsolSequence + HLTRecoJetSequencePrePF + hltFilterIsoEle12PFTau15CaloJet8 + hltPreOverlapFilterElectronTauCaloJet + HLTPFJetTriggerSequence + hltFilterIsoEle12PFTau15PFJet15 + HLTPFTauSequence + hltFilterIsoEle12PFTau15 + hltOverlapFilterIsoEle12PFTau15 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_ZeroBias = cms.Path( HLTBeginSequence + hltL1sZeroBias + hltPreZeroBias + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_ZeroBiasPixel_SingleTrack = cms.Path( HLTBeginSequence + hltL1sZeroBias + hltPreZeroBiasPixelSingleTrack + HLTDoLocalPixelSequence + HLTPixelTrackingForMinBiasSequence + hltPixelCandsForMinBias + hltMinBiasPixelFilter1 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MinBiasPixel_SingleTrack = cms.Path( HLTBeginSequence + hltL1sZeroBias + hltPreMinBiasPixelSingleTrack + hltL1TechBSCminBiasOR + HLTDoLocalPixelSequence + HLTPixelTrackingForMinBiasSequence + hltPixelCandsForMinBias + hltMinBiasPixelFilter1 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MultiVertex6_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1BscMinBiasORBptxPlusANDMinus + hltPreMultiVertex6 + HLTDoLocalPixelSequence + HLTRecopixelvertexingForMultiVertexSequence + hltVertexFilter6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MultiVertex8_L1ETT60_v2 = cms.Path( HLTBeginSequenceBPTX + hltL1sETT60 + hltPreMultiVertex8 + HLTDoLocalPixelSequence + HLTRecopixelvertexingForMultiVertexSequence + hltVertexFilter8 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1_BptxXOR_BscMinBiasOR = cms.Path( HLTBeginSequence + hltL1sL1BptxXORBscMinBiasOR + hltPreL1BptxXORBscMinBiasOR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_BSC_minBias_OR = cms.Path( HLTBeginSequence + hltL1sZeroBias + hltPreL1TechBSCminBiasOR + hltL1TechBSCminBiasOR + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_BSC_minBias = cms.Path( HLTBeginSequence + hltL1sZeroBias + hltPreL1TechBSCminBias + hltL1TechBSCminBias + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_BSC_halo = cms.Path( HLTBeginSequenceBPTX + hltL1sZeroBias + hltPreL1TechBSChalo + hltL1TechBSChalo + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_BSC_halo_forPhysicsBackground = cms.Path( HLTBeginSequenceBPTX + hltL1sZeroBias + hltPreL1TechBSChalo_forPhysicsBackground + hltL1TechBSChalo + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_BSC_HighMultiplicity = cms.Path( HLTBeginSequenceBPTX + hltL1sHighMultiplicityBSC + hltPreHighMultiplicityBSC + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_RPC_TTU_RBst1_collisions = cms.Path( HLTBeginSequenceBPTX + hltL1sL1TechRPCTTURBst1collisions + hltPreL1TechRPCTTURBst1collisions + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1Tech_HCAL_HF = cms.Path( HLTBeginSequenceBPTX + hltL1sZeroBias + hltPreL1HFTech + hltL1TechHCALHF + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_TrackerCosmics = cms.Path( HLTBeginSequence + hltL1sTrackerCosmics + hltPreTrackerCosmics + hltTrackerCosmicsPattern + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_RPCBarrelCosmics = cms.Path( HLTBeginSequence + hltL1sRPCBarrelCosmics + hltPreRPCBarrelCosmics + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PixelTracks_Multiplicity70 = cms.Path( HLTBeginSequenceBPTX + hltL1sETT60 + hltPrePixelTracksMultiplicity70 + HLTDoLocalPixelSequence + HLTRecopixelvertexingForHighMultSequence + hltPixelCandsForHighMult + hlt1HighMult70 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PixelTracks_Multiplicity85 = cms.Path( HLTBeginSequenceBPTX + hltL1sETT60 + hltPrePixelTracksMultiplicity85 + HLTDoLocalPixelSequence + HLTRecopixelvertexingForHighMultSequence + hltPixelCandsForHighMult + hlt1HighMult85 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PixelTracks_Multiplicity100 = cms.Path( HLTBeginSequenceBPTX + hltL1sL1ETT100 + hltPrePixelTracksMultiplicity100 + HLTDoLocalPixelSequence + HLTRecopixelvertexingForHighMultSequence + hltPixelCandsForHighMult + hlt1HighMult100 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_GlobalRunHPDNoise = cms.Path( HLTBeginSequence + hltL1sGlobalRunHPDNoise + hltPreGlobalRunHPDNoise + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_TechTrigHCALNoise = cms.Path( HLTBeginSequence + hltL1sTechTrigHCALNoise + hltL1sNotBptxPlusOrMinus + hltPreTechTrigHCALNoise + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1_BPTX = cms.Path( HLTBeginSequence + hltL1sL1BPTX + hltPreL1BPTX + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1_BPTX_MinusOnly = cms.Path( HLTBeginSequence + hltL1sL1BPTXMinusOnly + hltPreL1BPTXMinusOnly + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_L1_BPTX_PlusOnly = cms.Path( HLTBeginSequence + hltL1sL1BPTXPlusOnly + hltPreL1BPTXPlusOnly + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_LogMonitor = cms.Path( HLTBeginSequence + hltPreLogMonitor + hltLogMonitorFilter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLTriggerFinalPath = cms.Path( HLTBeginSequence + hltFEDSelector + hltTriggerSummaryAOD + hltTriggerSummaryRAW + hltBoolTrue )


HLTSchedule = cms.Schedule( *(HLTriggerFirstPath, HLT_Activity_CSC, HLT_L1Jet6U, HLT_L1Jet10U, HLT_Jet15U_v3, HLT_Jet30U_v3, HLT_Jet50U_v3, HLT_Jet70U_v3, HLT_Jet100U_v3, HLT_Jet140U_v3, HLT_Jet180U_v3, HLT_DiJetAve15U_v3, HLT_DiJetAve30U_v3, HLT_DiJetAve50U_v3, HLT_DiJetAve70U_v3, HLT_DiJetAve100U_v3, HLT_DiJetAve140U_v3, HLT_DoubleJet15U_ForwardBackward_v3, HLT_DoubleJet25U_ForwardBackward_v3, HLT_DoubleJet35U_ForwardBackward_v3, HLT_DiJet20U_Meff180U_v3, HLT_DiJet50U_PT50U_v3, HLT_ExclDiJet30U_HFAND_v3, HLT_ExclDiJet30U_HFOR_v3, HLT_QuadJet15U_v3, HLT_QuadJet20U_v3, HLT_QuadJet25U_v3, HLT_R010U_MR50U, HLT_R030U_MR100U, HLT_R033U_MR100U, HLT_RP025U_MR70U, HLT_L1ETT100, HLT_EcalOnly_SumEt160_v3, HLT_L1MET20, HLT_MET45_v3, HLT_MET45_DiJet30U_v3, HLT_MET65_CenJet50U_v3, HLT_MET80_CenJet50U_v3, HLT_MET100_v3, HLT_MET120_v3, HLT_HT50U_v3, HLT_HT100U_v3, HLT_HT130U_v3, HLT_HT140U_J30U_Eta3_v3, HLT_HT150U_v3, HLT_HT150U_Eta3_v3, HLT_HT160U_v3, HLT_HT160U_Eta3_v3, HLT_HT200U_v3, HLT_L1MuOpen_v2, HLT_L1MuOpen_DT_v2, HLT_L1Mu7_v1, HLT_L1Mu20, HLT_L2Mu0_NoVertex, HLT_L2Mu7_v1, HLT_L2Mu30_v1, HLT_Mu0_v2, HLT_Mu3_v2, HLT_Mu5, HLT_Mu7, HLT_Mu9, HLT_Mu11, HLT_Mu13_v1, HLT_Mu15_v1, HLT_Mu17_v1, HLT_Mu19_v1, HLT_Mu21_v1, HLT_Mu25_v1, HLT_IsoMu9_v4, HLT_IsoMu11_v4, HLT_IsoMu13_v4, HLT_IsoMu15_v4, HLT_IsoMu17_v4, HLT_Mu30_NoVertex_v1, HLT_L1DoubleMuOpen, HLT_L2DoubleMu0, HLT_L2DoubleMu20_NoVertex_v1, HLT_DoubleMu0, HLT_DoubleMu0_Quarkonium_v1, HLT_DoubleMu3_v2, HLT_DoubleMu5_v1, HLT_Mu5_L2Mu0, HLT_L1SingleEG8, HLT_Ele10_SW_L1R_v2, HLT_Ele12_SW_TighterEleId_L1R_v2, HLT_Ele17_SW_L1R_v2, HLT_Ele17_SW_Isol_L1R_v2, HLT_Ele17_SW_TighterEleIdIsol_L1R_v3, HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v2, HLT_Ele22_SW_L1R_v2, HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2, HLT_Ele22_SW_TighterEleId_L1R_v3, HLT_Ele32_SW_TighterEleId_L1R_v2, HLT_DoubleEle17_SW_L1R_v1, HLT_Photon10_Cleaned_L1R, HLT_Photon17_Isol_SC17HE_L1R_v1, HLT_Photon20_NoHE_L1R, HLT_Photon20_Cleaned_L1R, HLT_Photon20_Isol_Cleaned_L1R_v1, HLT_Photon22_SC22HE_L1R_v1, HLT_Photon30_Cleaned_L1R, HLT_Photon40_CaloId_Cleaned_L1R_v1, HLT_Photon40_Isol_Cleaned_L1R_v1, HLT_Photon50_Cleaned_L1R_v1, HLT_Photon50_NoHE_L1R, HLT_Photon70_Cleaned_L1R_v1, HLT_Photon110_NoHE_Cleaned_L1R_v1, HLT_DoublePhoton5_CEP_L1R_v3, HLT_DoublePhoton17_SingleIsol_L1R_v1, HLT_DoublePhoton22_L1R_v1, HLT_SingleIsoTau20_Trk15_MET25_v4, HLT_SingleIsoTau35_Trk15_MET25_v4, HLT_DoubleIsoTau15_OneLeg_Trk5_v4, HLT_DoubleIsoTau15_Trk5_v4, HLT_BTagMu_DiJet10U_v3, HLT_BTagMu_DiJet20U_v3, HLT_BTagMu_DiJet30U_v3, HLT_BTagMu_DiJet20U_Mu5_v3, HLT_BTagMu_DiJet30U_Mu5_v3, HLT_StoppedHSCP20_v3, HLT_StoppedHSCP35_v3, HLT_Mu7_Photon13_Cleaned_L1R_v1, HLT_Mu5_Ele13_v2, HLT_Mu5_Ele17_v2, HLT_Mu8_Ele8_v1, HLT_Mu11_Ele8_v1, HLT_Mu5_Jet50U_v3, HLT_Mu5_Jet70U_v3, HLT_Mu5_MET45_v3, HLT_Mu5_HT70U_v3, HLT_Mu5_HT100U_v3, HLT_DoubleMu3_HT50U_v3, HLT_Mu3_Ele8_HT70U_v1, HLT_Ele10_SW_HT70U_L1R_v2, HLT_Ele10_SW_EleId_HT70U_L1R_v2, HLT_Ele10_SW_HT100U_L1R_v2, HLT_DoubleEle8_SW_HT70U_L1R_v1, HLT_Mu11_PFTau15_v2, HLT_IsoMu9_PFTau15_v2, HLT_IsoEle12_PFTau15_v3, HLT_ZeroBias, HLT_ZeroBiasPixel_SingleTrack, HLT_MinBiasPixel_SingleTrack, HLT_MultiVertex6_v2, HLT_MultiVertex8_L1ETT60_v2, HLT_L1_BptxXOR_BscMinBiasOR, HLT_L1Tech_BSC_minBias_OR, HLT_L1Tech_BSC_minBias, HLT_L1Tech_BSC_halo, HLT_L1Tech_BSC_halo_forPhysicsBackground, HLT_L1Tech_BSC_HighMultiplicity, HLT_L1Tech_RPC_TTU_RBst1_collisions, HLT_L1Tech_HCAL_HF, HLT_TrackerCosmics, HLT_RPCBarrelCosmics, HLT_PixelTracks_Multiplicity70, HLT_PixelTracks_Multiplicity85, HLT_PixelTracks_Multiplicity100, HLT_GlobalRunHPDNoise, HLT_TechTrigHCALNoise, HLT_L1_BPTX, HLT_L1_BPTX_MinusOnly, HLT_L1_BPTX_PlusOnly, HLT_LogMonitor, HLTriggerFinalPath ))


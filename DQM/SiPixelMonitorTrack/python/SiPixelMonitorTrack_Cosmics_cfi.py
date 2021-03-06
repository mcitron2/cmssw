import FWCore.ParameterSet.Config as cms

SiPixelTrackResidualSource_Cosmics = cms.EDAnalyzer("SiPixelTrackResidualSource",
    src = cms.InputTag("siPixelTrackResiduals"),
    clustersrc = cms.InputTag("siPixelClusters"),                            
    debug = cms.untracked.bool(False),                          
    saveFile = cms.untracked.bool(False),
    outputFile = cms.string('Pixel_DQM_TrackResidual.root'),
    TrackCandidateProducer = cms.string('rsTrackCandidatesP5'),
    TrackCandidateLabel = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    modOn = cms.untracked.bool(False),
    reducedSet = cms.untracked.bool(True),
    ladOn = cms.untracked.bool(True),
    layOn = cms.untracked.bool(True),
    phiOn = cms.untracked.bool(True),
    ringOn = cms.untracked.bool(True),
    bladeOn = cms.untracked.bool(True),
    diskOn = cms.untracked.bool(True),

    trajectoryInput = cms.InputTag('rsWithMaterialTracksP5')              
)

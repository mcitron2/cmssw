import FWCore.ParameterSet.Config as cms

#from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import *
from RecoTauTag.RecoTau.TauDiscriminatorTools import requireLeadTrack

caloRecoTauDiscriminationByTauPolarization = cms.EDProducer("CaloRecoTauDiscriminationByTauPolarization",
    CaloTauProducer     = cms.InputTag('caloRecoTauProducer'), #tau collection to discriminate

    Prediscriminants    = requireLeadTrack,
    BooleanOutput       = cms.bool(True),

    rtau                = cms.double(0.8), # minimum value for the polarization variable

#    qualityCuts         = PFTauQualityCuts,# set the standard quality cuts
    PVProducer          = cms.InputTag('offlinePrimaryVertices'), # needed for quality cuts
)

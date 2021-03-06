import FWCore.ParameterSet.Config as cms

from Validation.RecoEgamma.tpSelection_cfi import *
from Validation.RecoEgamma.photonValidator_cfi import *
from Validation.RecoEgamma.tkConvValidator_cfi import *

from SimTracker.TrackAssociation.TrackAssociatorByHits_cfi import *
import SimTracker.TrackAssociation.TrackAssociatorByHits_cfi
TrackAssociatorByHits.Cut_RecoToSim = 0.5
TrackAssociatorByHits.Quality_SimToReco = 0.5



photonValidation.minPhoEtCut = 10
photonValidation.eMax  = 500
photonValidation.etMax = 250
eMax = photonValidation.etMax
etMax = photonValidation.etMax 
## same for all
photonValidation.convTrackMinPtCut = 1.
photonValidation.useTP = True
photonValidation.rBin = 48
photonValidation.eoverpMin = 0.
photonValidation.eoverpMax = 5.
#

# selectors go in separate "pre-" sequence
photonPrevalidationSequence = cms.Sequence(tpSelection*tpSelecForFakeRate*tpSelecForEfficiency)
photonValidationSequence = cms.Sequence(photonValidation*tkConversionValidation)


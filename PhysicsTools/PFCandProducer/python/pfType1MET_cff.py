import FWCore.ParameterSet.Config as cms

from PhysicsTools.PFCandProducer.pfMET_cfi  import *
from PhysicsTools.PFCandProducer.pfType1MET_cfi  import *

pfRawMET = pfMET.clone()
#pfRawMET.hfCalibFactor = 1.

pfType1MET.inputUncorMetLabel = 'pfRawMET'

pfCorMET = cms.Sequence( pfRawMET * pfType1MET )


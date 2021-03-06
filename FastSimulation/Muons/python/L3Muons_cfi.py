import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from RecoMuon.TrackingTools.MuonTrackLoader_cff import *
from RecoMuon.GlobalTrackingTools.GlobalTrajectoryBuilderCommon_cff import *

def l3muons(old):
    if (old):
        return  cms.EDProducer("FastL3MuonProducer",
                               MuonTrackLoaderForL3,
                               MuonServiceProxy,
                               L3TrajBuilderParameters = cms.PSet(
            GlobalTrajectoryBuilderCommon,
            MatcherOutPropagator = cms.string('SmartPropagator'),
            #	InputTag tkTrajLabel = hltL3Trajectory
            #	InputTag l3SeedLabel = hltL3TrajectorySeedFromL2
            ## TrackerTrajectories = cms.InputTag("hltL3TkTracksFromL2"),
            tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2"),
            TkTrackBuilder = cms.string('muonCkfTrajectoryBuilder'),
            TransformerOutPropagator = cms.string('SmartPropagatorAny'),
            KFFitter = cms.string('L3MuKFFitter')
            ),
                               MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
                               )
    else:
        import HLTrigger.Configuration.HLT_FULL_cff as trueHLT
        return trueHLT.hltL3Muons


L3Muons = l3muons(False)

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Message Logger
process.MessageLogger = cms.Service("MessageLogger",
#   default = cms.untracked.PSet( limit = cms.untracked.int32(0)),
   destinations = cms.untracked.vstring('cout')
)

process.load("L1TriggerConfig.L1GeometryProducers.l1CaloGeometry_cfi")
process.load("L1TriggerConfig.L1GeometryProducers.l1CaloGeomRecordSource_cff")

process.load("L1Trigger.GlobalMuonTrigger.gmtDigis_cff")

process.gmtDump = cms.EDAnalyzer("L1MuGMTDump",
    GMTInputTag = cms.untracked.InputTag("gmtDigis")
)
    
process.source = cms.Source("L1MuGMTHWFileReader",
    fileNames = cms.untracked.vstring("file:gmt_testfile.h4mu.dat")
)

process.gmtDigis.DTCandidates = "source:DT"
process.gmtDigis.CSCCandidates = 'source:CSC'
process.gmtDigis.RPCbCandidates = 'source:RPCb'
process.gmtDigis.RPCfCandidates = 'source:RPCf'
process.gmtDigis.MipIsoData = 'source'
process.gmtDigis.Debug = 9
process.gmtDigis.BX_min = -1
process.gmtDigis.BX_max = 1
process.gmtDigis.BX_min_readout = -1
process.gmtDigis.BX_max_readout = 1

#process.L1MuGMTParameters.SubsystemMask = 0

process.p = cms.Path(process.gmtDigis * process.gmtDump)

import FWCore.ParameterSet.Config as cms

process = cms.Process("EDMtoMEConvert")

process.load("DQMServices.Components.EDMtoMEConverter_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.options = cms.untracked.PSet(
 fileMode = cms.untracked.string('FULLMERGE')
)

process.source = cms.Source("PoolSource",
#    dropMetaData = cms.untracked.bool(True),
    processingMode = cms.untracked.string("RunsLumisAndEvents"),
    fileNames = cms.untracked.vstring('rfio:///?svcClass=cmscaf&path=/castor/cern.ch/cms/store/cmscaf/alca/alignment/CRUZET4-TkAlCosmics/57553/ALCARECOTkAlCosmics0T_1.root',
                                      'rfio:///?svcClass=cmscaf&path=/castor/cern.ch/cms/store/cmscaf/alca/alignment/CRUZET4-TkAlCosmics/57553/ALCARECOTkAlCosmics0T_2.root')
)

process.maxEvents.input = -1

process.source.processingMode = "RunsAndLumis"

process.DQMStore.referenceFileName = ''
process.dqmSaver.convention = 'Offline'
process.dqmSaver.workflow = '/GlobalCruzet4-A/CMSSW_2_1_4-Test_v1/ALCARECO'

# Merge different runs in one output ROOT file
#process.DQMStore.collateHistograms = True
#process.EDMtoMEConverter.convertOnEndLumi = False
#process.EDMtoMEConverter.convertOnEndRun = True
#process.dqmSaver.saveByRun = -1
#process.dqmSaver.saveAtJobEnd = True

# Produce one ROOT file per run
process.DQMStore.collateHistograms = False
process.EDMtoMEConverter.convertOnEndLumi = True
process.EDMtoMEConverter.convertOnEndRun = False

process.p1 = cms.Path(process.EDMtoMEConverter*process.dqmSaver)


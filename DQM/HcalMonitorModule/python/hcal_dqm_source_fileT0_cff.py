import FWCore.ParameterSet.Config as cms

#from DQMServices.Components.DQMEnvironment_cfi import *

dqmInfoHcal = cms.EDAnalyzer("DQMEventInfo",
    subSystemFolder = cms.untracked.string('Hcal')
)
from DQM.HcalMonitorModule.HcalMonitorModule_cfi import *
from DQM.HcalMonitorModule.ZDCMonitorModule_cfi import *
from DQM.HcalMonitorTasks.HcalMonitorTasks_cfi import *

hcalRawDataMonitor.online         = False
hcalDigiMonitor.online            = False
hcalRecHitMonitor.online          = False
hcalHotCellMonitor.online         = False
hcalDeadCellMonitor.online        = False
hcalBeamMonitor.online            = False
hcalTrigPrimMonitor.online        = False
hcalNZSMonitor.online             = False
hcalLSbyLSMonitor.online          = False

# The following tasks are not yet run online
hcalDetDiagLEDMonitor.online      = False
hcalDetDiagPedestalMonitor.online = False
hcalDetDiagLaserMonitor.online    = False
hcalDetDiagNoiseMonitor.online    = False

# Offline tasks should look at all events, I think
hcalRawDataMonitor.AllowedCalibTypes         =  []
hcalDigiMonitor.AllowedCalibTypes            =  []
hcalRecHitMonitor.AllowedCalibTypes          =  []
hcalHotCellMonitor.AllowedCalibTypes         =  []
hcalDeadCellMonitor.AllowedCalibTypes        =  []
hcalBeamMonitor.AllowedCalibTypes            =  []
hcalTrigPrimMonitor.AllowedCalibTypes        =  []
hcalNZSMonitor.AllowedCalibTypes             =  []
hcalLSbyLSMonitor.AllowedCalibTypes          =  []

# No need to skip out of order LS in offline, I think
hcalRawDataMonitor.skipOutOfOrderLS         =  False
hcalDigiMonitor.skipOutOfOrderLS            =  False
hcalRecHitMonitor.skipOutOfOrderLS          =  False
hcalHotCellMonitor.skipOutOfOrderLS         =  False
hcalDeadCellMonitor.skipOutOfOrderLS        =  False
hcalBeamMonitor.skipOutOfOrderLS            =  False
hcalTrigPrimMonitor.skipOutOfOrderLS        =  False
hcalNZSMonitor.skipOutOfOrderLS             =  False
hcalLSbyLSMonitor.skipOutOfOrderLS          =  False

# Make diagnostics where appropriate
hcalDeadCellMonitor.makeDiagnostics   = True
hcalRecHitMonitor.makeDiagnostics     = True
hcalDigiMonitor.makeDiagnostics       = True

# Require at least 1000 events for the dead cell monitor to process at end of lumi block?  Do we
# want this functionality in offline, or do we want to rely only on the never-present test?
hcalDeadCellMonitor.minDeadEventCount = 1000
# UPDATE 23 March 2010 -- so far, only never-present test used in offline

# Require at least 200 events in a lumi block when looking for persistent hot cells
hcalHotCellMonitor.minEvents = 200

#LSbyLSmonitor must require at least as many events/LS as dead cell monitor
hcalLSbyLSMonitor.minEvents = 1000

# Ignore checks on HO Ring2 channels in dead cell monitor (except for SiPM)
hcalDeadCellMonitor.excludeHORing2=True

hcalOfflineDQMSource = cms.Sequence(hcalMonitor
                                    + zdcMonitor
                                    + hcalMonitorTasksOfflineSequence
                                    + dqmInfoHcal)

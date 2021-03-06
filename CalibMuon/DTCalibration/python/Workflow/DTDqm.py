from tools import loadCmsProcess,writeCfg
from CmsswTask import *
import os

class DTDqm:
    def __init__(self, run, dir, dqm_files, result_dir, config):
        #basedir = 'Run%s/Ttrig' % run
        #self.dir = basedir + '/' + 'Exec'
        #self.result_dir = basedir + '/' + 'Results'
        self.runnumber = int(run)
        self.dir = dir
        self.result_dir = result_dir
        self.dqm_files = dqm_files

        self.pset_name = 'DTkFactValidation_2_DQM_cfg.py'
        self.pset_template = config.templatepath + '/config/DTkFactValidation_2_DQM_cfg.py'

        self.initProcess()
        self.configs = []
        self.configs.append(self.pset_name)
        self.task = CmsswTask(self.dir,self.configs)

    def initProcess(self):
        self.process = loadCmsProcess(self.pset_template)
        self.process.source.fileNames = self.dqm_files
        self.process.dqmSaver.dirName = os.path.abspath(self.result_dir)
        if self.process.DQMStore.collateHistograms: self.process.dqmSaver.forceRunNumber = self.runnumber

    def writeCfg(self):
        writeCfg(self.process,self.dir,self.pset_name) 
    
    def run(self):
        self.task.run()
        return

def runDQM(run,castor_dir,result_dir,template_path):
    from CalibMuon.DTCalibration.Workflow.tools import listFilesInCastor
    dqm_files = listFilesInCastor(castor_dir,'DQM')
    runDir = '.'
    class config: pass
    config.templatepath = template_path

    dtDqmFinal = DTDqm(run,runDir,dqm_files,result_dir,config)
    dtDqmFinal.writeCfg()
    dtDqmFinal.run()

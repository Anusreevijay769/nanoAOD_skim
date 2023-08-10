#!/usr/bin/env python
import os,sys

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from H4Lmodule import *
from H4LCppModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *

testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/3ED05633-EBB7-4A44-8F9D-CD956490BCFD.root"
#testfile1 = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/1B1D7372-F369-7C40-A85F-841308D42D2C.root"
#testfile2 = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/2BA7CCC9-BA73-3C45-9844-474A92E58A28.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M120_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/1D8ACDF9-FCA6-7649-95A4-487A132F318D.root"
#testfile1 = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M120_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/6EA35A9B-C42E-0447-ACED-E3AC70A7AD7E.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M124_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/1AAFFFBE-330D-EF42-B39E-BA70A7E90669.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M126_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/8198816C-2B6D-CB41-9B96-6B02BD81CAAE.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17NanoAODv9/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v2/2430000/13F76A9B-76DD-144B-B328-A8C207376C08.root"
#testfile1 = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/GluGluHToZZTo4L_M130_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/00305042-7CD7-2C46-8FD6-D1089E4C4163.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17NanoAODv9/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v2/260000/FD91C4F0-7DE3-4947-817D-3EA957A0BC50.root"
#testfile = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/80000/3F65CE54-8477-C64E-B0BB-BD77E870AB54.root"
entriesToRun = 0 # 0 if need to run over all entries else put number of entries to run
isMCTrueFalse = True
# Keep DownloadFileToLocalThenRun=True this should reduce the file read error from eos.
DownloadFileToLocalThenRun=True
if testfile.find("UL18") != -1:
    year = 2018
if testfile.find("UL17") != -1:
    year = 2017
H4LCppModule = lambda: HZZAnalysisCppProducer(year)
#p=PostProcessor(".",[testfile],"",None,[H4LCppModule()],provenance=True,fwkJobReport=False,haddFileName="nano_M125.root",maxEntries=entriesToRun,prefetch=DownloadFileToLocalThenRun,outputbranchsel="keep_and_drop.txt")
p=PostProcessor(".",[testfile],"",None,[H4LCppModule()],provenance=True,fwkJobReport=False,haddFileName="nano_M125_cpp.root",maxEntries=entriesToRun,prefetch=DownloadFileToLocalThenRun,outputbranchsel="keep_and_drop.txt")

p.run()
print "DONE"

#!   /usr/bin/env   python
import   os
import   glob
import   math
from   array   import   array
import   sys
import   time
import   subprocess

from   optparse   import   OptionParser

parser   =   OptionParser()

parser.add_option('--generateOnly',                  action='store_true',   dest='generateOnly',                  default=False,   help='generate   jobs   only,   without   submitting   them')

(options,   args)   =   parser.parse_args()

#ntupleName   =   "data-DoubleEG-Run2016BCD_ZSkim_12p9fb_multifit"
#ntupleName   =   "92X_dataRun2_Prompt_v9_SingleEle_harness_"
ntupleName   =   "Cal_Oct2017_Ped_v2_SingleEle"
#ntupleName   =   "Run2016BCDEFGH_WZSkim_Cal_Jan2017_ped_v1_multifit"
#ntupleName   =   "data-SingleElectron-Run2016BCD_WSkim_12p9fb_weights"
#options:   "data-Run2015D-25ns-multifit",   "data-Run2015D-25ns-multifit"   or   "data-Run2015D-25ns-stream".
folder   =   "/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/ntupleEoP/"
#categories   =   ["EB"]#,"EB_0_1","EB_1_1479"]#,"EE","EE_1479_2","EE_2_25","EEp","EEp_1479_2","EEp_2_25","EEm","EEm_1479_2","EEm_2_25","EEp_2_225","EEp_225_25","EEm_2_225","EEm_225_25"]
#yMIN   =   ["0.85"]#,"0.85","0.85"]#,"0.65","0.65","0.40","0.65","0.65","0.40","0.65","0.65","0.40","0.40","0.40","0.40","0.40"]
#categories = ["EE","EEp","EEm"]
categories = ["EE_1479_2","EE_2_25","EEp_1479_2","EEp_2_25","EEm_1479_2","EEm_2_25"]
yMIN   =   ["0.97", "0.97", "0.97","0.97", "0.97", "0.97"]
yMAX   =   ["1.02", "1.02", "1.02","1.02", "1.02", "1.02"]
events   =   ["10000", "10000", "10000","10000", "10000", "10000"]#,"10000","10000"]#,"10000","10000","10000","10000","10000","10000","10000","10000","10000","10000","10000","10000","10000"]
#yMIN   =   ["0.95","0.95","0.95","0.95","0.95","0.95","0.95","0.95","0.95","0.95","0.95","0.95"]
#categories   =   ["EEp","EEp_1479_2","EEp_2_25","EEm","EEm_1479_2","EEm_2_25"]
#yMIN   =   ["0.65","0.65","0.40","0.65","0.65","0.40"]

'''
ntuplelist   =   [
"SingleElectron-Run2016B-WSkim-Prompt_v2-273150-275376",
"SingleElectron-Run2016C-WSkim-Prompt_v2-275420-276283",
"SingleElectron-Run2016D-WSkim-Prompt_v2-276315-276811",
"SingleElectron-Run2016E-WSkim-Prompt-v2-276830-277420",
"SingleElectron-Run2016F-WSkim-Prompt-v1-277820-278808",
"SingleElectron-Run2016G-WSkim-Prompt-v1-278817-280385",
"SingleElectron-Run2016H-WSkim-Prompt-v2-281207-284035",
"SingleElectron-Run2016H-WSkim-Prompt-v3-284036-284068"
]
'''
'''
folderlist=[
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016B-WSkim-Prompt_v2/273150-275376/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016C-WSkim-Prompt_v2/275420-276283/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016D-WSkim-Prompt_v2/276315-276811/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016E-WSkim-Prompt-v2/276830-277420/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016F-WSkim-Prompt-v1/277820-278808/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016G-WSkim-Prompt-v1/278817-280385/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016H-WSkim-Prompt-v2/281207-284035/271036_284044-23Sep2016/newNtuples/",
"/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Jan2017_ref/SingleElectron-Run2016H-WSkim-Prompt-v3/284036-284068/271036_284044-23Sep2016/newNtuples/"
]
'''
'''
folderlist = [
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017B-WSkim-Prompt-v1/297046-297723/294927-302654_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017B-WSkim-Prompt-v2/298678-299329/294927-302654_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017C-WSkim-Prompt-v1/299368-299649/294927-302654_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017C-WSkim-Prompt-v2/299929-300676/294927-302654_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017C-WSkim-Prompt-v3/300742-302029/294927-302654_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Sep2017_ref/SingleElectron-Run2017D-WSkim-Prompt-v1/302030-302663/294927-302654_Prompt_v1/newNtuples/"
]
'''
'''
ntuplelist = [
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017B-WSkim-Prompt-v1/297046-297723/294927-302654_Prompt_v1/newNtuples/SingleElectron-Run2017B-WSkim-Prompt-v1-297046-297723.root",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017B-WSkim-Prompt-v2/298678-299329/294927-302654_Prompt_v1/newNtuples/SingleElectron-Run2017B-WSkim-Prompt-v2-298678-299329.root",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017C-WSkim-Prompt-v1/299368-299649/294927-302654_Prompt_v1/newNtuples/SingleElectron-Run2017C-WSkim-Prompt-v1-299368-299649.root",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017C-WSkim-Prompt-v2/299929-300676/294927-302654_Prompt_v1/newNtuples/splitNtuples4/SingleElectron-Run2017C-WSkim-Prompt-v2-299929-300676.root",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017C-WSkim-Prompt-v3/300742-302029/294927-302654_Prompt_v1/newNtuples/SingleElectron-Run2017C-WSkim-Prompt-v3-300742-302029.root",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/92X_dataRun2_Prompt_v9/SingleElectron-Run2017D-WSkim-Prompt-v1/302030-302663/294927-302654_Prompt_v1/newNtuples/SingleElectron-Run2017D-WSkim-Prompt-v1-302030-302663.root"
]
'''
'''
ntuplelist = [
"SingleElectron-Run2017B-WSkim-Prompt-v1-297046-297723.root",
"SingleElectron-Run2017B-WSkim-Prompt-v2-298678-299329.root",
"SingleElectron-Run2017C-WSkim-Prompt-v1-299368-299649.root",
"SingleElectron-Run2017C-WSkim-Prompt-v2-299929-300676.root",
"SingleElectron-Run2017C-WSkim-Prompt-v3-300742-302029.root",
"SingleElectron-Run2017D-WSkim-Prompt-v1-302030-302663.root"
]
'''

ntuplelist = [
"SingleElectron-Run2017B-WSkim-Prompt-v1-297046-297723.root",
"SingleElectron-Run2017B-WSkim-Prompt-v2-298678-299329.root",
"SingleElectron-Run2017C-WSkim-Prompt-v1-299368-299649.root",
"SingleElectron-Run2017C-WSkim-Prompt-v3-300742-302029.root",
"SingleElectron-Run2017D-WSkim-Prompt-v1-302030-302663.root",
"SingleElectron-Run2017E-WSkim-Prompt-v1-303574-304797.root",
"DoubleEG-Run2017B-ZSkim-Prompt-v1-297046-297723.root", 
"DoubleEG-Run2017B-ZSkim-Prompt-v2-298678-299329.root", 
"DoubleEG-Run2017C-ZSkim-Prompt-v1-299368-299649.root", 
"DoubleEG-Run2017C-ZSkim-Prompt-v2-299929-300676.root", 
"DoubleEG-Run2017C-ZSkim-Prompt-v3-300742-302029.root", 
"DoubleEG-Run2017D-ZSkim-Prompt-v1-302030-302663.root", 
"DoubleEG-Run2017E-ZSkim-Prompt-v1-303574-304797.root"
]

folderlist=[
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017B-WSkim-Prompt-v1/297046-297723/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017B-WSkim-Prompt-v2/298678-299329/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017C-WSkim-Prompt-v1/299368-299649/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017C-WSkim-Prompt-v3/300742-302029/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017D-WSkim-Prompt-v1/302030-302663/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/SingleElectron-Run2017E-WSkim-Prompt-v1/303574-304797/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017B-ZSkim-Prompt-v1/297046-297723/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017B-ZSkim-Prompt-v2/298678-299329/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017C-ZSkim-Prompt-v1/299368-299649/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017C-ZSkim-Prompt-v2/299929-300676/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017C-ZSkim-Prompt-v3/300742-302029/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017D-ZSkim-Prompt-v1/302030-302663/294927-304120_Prompt_v1/newNtuples/",
"/eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/Cal_Oct2017_Ped_v2/DoubleEG-Run2017E-ZSkim-Prompt-v1/303574-304797/294927-304120_Prompt_v1/newNtuples/"
]


EBm   =   1

currentDir   =   os.getcwd();
CMSSWDir   =   currentDir+"/../";

os.system("mkdir   Job_monitoring_"+ntupleName+"SingleAndDouble")

ietamin   =   0
iphimax=   1
ietamax   =   0
iphimin   =   0

#etaRingMin = [0,5,10,15,20,25,30,35]
etaRingMin = [-1]

for i in range(len(categories)):
   for k in range(len(etaRingMin)):
       etaRingMax = etaRingMin[k]# +5
       #fn   =   "Job_monitoring_"+ntupleName+"/Job_"+categories[i]+"_etaRingMin_"+str(etaRingMin[k])+"_etaRingMax_"+str(etaRingMax)+"_1nw"; 
       #fn   =   "Job_monitoring_"+ntupleName+"/Job_"+categories[i]+"_etaRingMin_"+str(etaRingMin[k])+"_etaRingMax_"+str(etaRingMax)+"_2nw"; 
       #fn   =   "Job_monitoring_"+ntupleName+"/Job_"+categories[i]+"_notRings_1nw";
       fn   =   "Job_monitoring_"+ntupleName+"/Job_"+categories[i]+"_notRings_2nw"; 
       outScript   =   open(fn+".sh","w");
       command   =   "ZFitter.exe   -f   /afs/cern.ch/user/v/vciriolo/work/private/EOverP/CMSSW_8_0_24_patch1/src/Calibration/ZFitter/data/validation/"+ntupleName+".dat   --evtsPerPoint   "+events[i]+"   --laserMonitoringEP   --EBEE   "+categories[i]+"   --yMIN   "+yMIN[i]+"   --yMAX   "+yMAX[i]+"   --LUMI   17.8   --dayMin   15-03-2016   --dayMax   30-12-2017   --noPU"#  --etaRing_min  "+str(etaRingMin[k])+"    --etaRing_max  "+str(etaRingMax)
       #command   =   "ZFitter.exe   -f   /afs/cern.ch/user/v/vciriolo/work/private/EOverP/CMSSW_8_0_24_patch1/src/Calibration/ZFitter/data/validation/"+ntupleName+".dat   --evtsPerPoint   "+events[i]+"   --laserMonitoringEP   --EBEE   "+categories[i]+"   --yMIN   "+yMIN[i]+"   --yMAX   "+yMAX[i]+"   --LUMI   17.8   --dayMin   15-03-2016   --dayMax   30-12-2017   --noPU   --IetaMax   "+   str(ietamax*(1))   +   "   --IetaMin   "   +   str(ietamin*(1))   +   "      --IphiMin   "   +   str(iphimin)   +   "   --IphiMax   "   +   str(iphimax)   #default,   to   be   run   for   E/p   vs   time  
       print   command;
         
       outScript.write('#!/bin/bash');
       outScript.write("\n"+'cd   '+CMSSWDir);
       outScript.write("\n"+'eval   `scram   runtime   -sh`');
       outScript.write("\n"+'cd   -');
       outScript.write("\necho   $PWD");
       outScript.write("\nmkdir   "+categories[i]+"__");
       outScript.write("\nll");

       for   j   in   range(len(ntuplelist)):
          outScript.write("\necho   \"copy   main   tree\"   ");
          #outScript.write("\ncp   "+folderlist[j]+""+ntuplelist[j]+".root   ./")
          #outScript.write("\ncp   "+folderlist[j]+""+ntuplelist[j]+"   ./")
          #outScript.write("\ncp   "+ntuplelist[j]+"   ./")
          outScript.write("\ncp   "+folderlist[j]+""+ntuplelist[j]+"   ./")
          
#          outScript.write("\necho   \"copy   extracalib   tree\"   ");
#          outScript.write("\ncmsStage   "+folderlist[j]+"extraCalibTree-"+ntuplelist[j]+".root   ./")

       outScript.write("\necho   \"copia13\"   ");
#                                                                        outScript.write("\ncp   -v   /afs/cern.ch/user/l/lbrianza/work/public/ntupleEoP/*   .")
         #outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EB_pTk.root   ./")
       outScript.write("\necho   \"copia14\"   ");
       #outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EB_scE.root   ./")
       outScript.write("\necho   \"copia15\"   ");
         #outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EE_pTk.root   ./")
       outScript.write("\necho   \"copia14\"   ");
       #outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EE_scE.root   ./")
       outScript.write("\necho   \"copia15\"   ");
       #outScript.write("\ncmsStage   "+folder+"EoverPmonitoring_batch_"+ntupleName+".dat   ./")
       outScript.write("\necho   \"fine   copia\"   ");
         
       outScript.write("\nls")
       outScript.write("\necho   \"eseguo:   "+command+"\"   ")
       outScript.write("\n"+command);
       outScript.write("\nls")
         #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   "+currentDir+"/"+categories[i]+"_"+ntupleName+"_ietamin_"+str(ietamin*(1))+"_ietamax_"+str(ietamax*(1))+"_iphimin_"+str(iphimin)+"_iphimax_"+str(iphimax)+"/")
         #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   "+currentDir+"/"+categories[i]+"_"+ntupleName+"_ietamax_"+str(ietamin*(-1))+"_ietamin_"+str(ietamax*(-1))+"_iphimin_"+str(iphimin)+"_iphimax_"+str(iphimax)+"/")
         #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   "+currentDir+"/"+categories[i]+"_"+ntupleName+"_"+run[j]+"_ietamax_"+str(ietamax*(1))+"_ietamin_"+str(ietamin*(1))+"_iphimin_"+str(iphimin)+"_iphimax_"+str(iphimax)+"/")
       outScript.write("\nexport EOS_MGM_URL=root://eosuser.cern.ch")
         
       #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/"+categories[i]+"_"+ntupleName+"_etaRingMin_"+str(etaRingMin[k])+"_etaRingMax_"+str(etaRingMax)+"/")
       #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/1nw/"+categories[i]+"_"+ntupleName+"_etaRingMin_"+str(etaRingMin[k])+"_etaRingMax_"+str(etaRingMax)+"/")
       #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/2nw/"+categories[i]+"_"+ntupleName+"_etaRingMin_"+str(etaRingMin[k])+"_etaRingMax_"+str(etaRingMax)+"/")
       #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/"+categories[i]+"_"+ntupleName+"_notRings/")
       #outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/1nw/"+categories[i]+"_"+ntupleName+"_notRings/")
       outScript.write("\ncp   -v   -r   "+categories[i]+"__/   /eos/user/v/vciriolo/EoP_monitoring/harness2017/Cal_Oct2017/SingleAndDouble/Cal_Oct2017_Ped_v2/2nw/"+categories[i]+"_"+ntupleName+"_notRings/")
       outScript.close();
       os.system("chmod   777   "+currentDir+"/"+fn+".sh");
       #command2   =   "bsub   -q   cmscaf1nw   -cwd   "+currentDir+"   "+currentDir+"/"+fn+".sh";
       #command2   =   "bsub   -q   1nw   -cwd   "+currentDir+"   "+currentDir+"/"+fn+".sh";
       command2   =   "bsub   -q   2nw   -cwd   "+currentDir+"   "+currentDir+"/"+fn+".sh";
       if   not   options.generateOnly:
                    os.system(command2);
       print   command2

            




'''
fn   =   "Job_monitoring_"+ntupleName+"/Job_"+"EE";
outScript   =   open(fn+".sh","w");
command   =   "ZFitter.exe   -f   EoverPcalibration_batch_"+ntupleName+".dat   --evtsPerPoint   50000   --laserMonitoringEPvsPU   --EBEE   EE   --yMIN   0.6   --yMAX   1.15   --LUMI   12.9   --dayMin   15-03-2016   --dayMax   01-08-2016"
print   command;
outScript.write('#!/bin/bash');
outScript.write("\n"+'cd   '+CMSSWDir);
outScript.write("\n"+'eval   `scram   runtime   -sh`');
outScript.write("\n"+'cd   -');
outScript.write("\necho   $PWD");
outScript.write("mkdir   EE__");
outScript.write("\nll");


outScript.write("\necho   \"copia1\"   ");
outScript.write("\ncmsStage   "+folder+ntupleName+".root   ./")
outScript.write("\necho   \"copia2\"   ");
outScript.write("\ncmsStage   "+folder+"extraCalibTree-"+ntupleName+".root   ./")

outScript.write("\necho   \"copia13\"   ");
#                                                                        outScript.write("\ncp   -v   /afs/cern.ch/user/l/lbrianza/work/public/ntupleEoP/*   .")
outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EE_pTk.root   ./")
outScript.write("\necho   \"copia14\"   ");
outScript.write("\ncmsStage   "+folder+"momentumCalibration2015_EE_scE.root   ./")
outScript.write("\necho   \"copia15\"   ");
outScript.write("\ncmsStage   "+folder+"EoverPcalibration_batch_"+ntupleName+".dat   ./")
outScript.write("\necho   \"fine   copia\"   ");

outScript.write("\nls")
outScript.write("\necho   \"eseguo:   "+command+"\"   ")
outScript.write("\n"+command);
outScript.write("\nls")
outScript.write("\ncp   -v   -r   EE__/   "+currentDir+"/EE_"+ntupleName+"/")
outScript.close();
os.system("chmod   777   "+currentDir+"/"+fn+".sh");
command2   =   "bsub   -q   cmscaf1nd   -cwd   "+currentDir+"   "+currentDir+"/"+fn+".sh";
if   not   options.generateOnly:
            os.system(command2);
print   command2
'''






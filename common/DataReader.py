import os
from common.Types import LogData, Cfg, DataReaderCallBack
import sys

class DataReader:
    cfg = None;
    callback:DataReaderCallBack = None

    def __init__(self, cfg:Cfg, cb:DataReaderCallBack=None):
        self.cfg = cfg;
        self.i=0
        self.callback=cb;
        self.files =0;

    def readFileContents(self,filename):
        print(filename)
        self.files+=1;
        #if(self.i==0):
        #   self.i=1;
        #   return;
        file = open(filename,'r')
        lastPacket=None
        for line in file:
            if line.startswith("#"): continue
            line = line.strip('\n')
            #print(line)
            logData = LogData(line)
            #print (logData)
            if lastPacket==None: lastPacket =logData
            elif (lastPacket.micros > logData.micros and logData.micros != -1):
                    print("Dataset not clear (micros), parse in java spliter first", file=sys.stderr);
            elif (lastPacket.date > logData.date and logData.micros != -1):
                print("Dataset not clear (date), parse in java spliter first", file=sys.stderr);
            if self.callback != None :
                self.callback.pushLogData(logData)

        file.close();

    def readDataSet(self):
        path = './data/sets/'+ self.cfg.dataset
        print ("Reading DataSet: "+path)

        for filename in sorted(os.listdir(path)):
            self.readFileContents (path+"/"+    filename)

    def printFiles(self):
        print("Files: "+str(self.files))


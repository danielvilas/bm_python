import datetime
import sys

from typing import List

##Objects
class LogData:
    micros=None
    a0=None
    a1=None
    date=None
    deltaMicros=None

    def __init__(self, line):
        tokens = line.split(',')
        strMicros = tokens[0]
        strA0 = tokens[1]
        strA1 = tokens[2]
        strDate = tokens[3]
        strDelta = tokens[4]

        self.a0=int(strA0)
        self.a1=int(strA1)
        self.micros=int(strMicros,16)
        if(strMicros.startswith('-') and self.micros!=-1):
            print("Dataset not clear (-), parse in java spliter first",file=sys.stderr);
        self.date=datetime.datetime.fromtimestamp(int(strDate)/1000, tz=datetime.timezone.utc)
        self.deltaMicros=int(strDelta)

class LogPacket:
    packets:List[LogData]=[];

    def __init__(self):
        self.packets=[]

    def addLogData(self,logData:LogData):
        self.packets.append(logData)

    def __len__(self):
        return len(self.packets)

class ParsedPacket:
    date:datetime
    tv:float
    bluray:float
    appleTv:float
    ipTv:float

    def __init__(self, date:datetime, result):
        self.date=date
        self.tv=result[0]
        self.bluray=result[1]
        self.appleTv=result[2]
        self.ipTv=result[3]

class Cfg:
    server = None;
    continous = None;
    dataset = None;
    protocol = None;

    def __str__(self):
        return 'Server: '+self.server + '\nContinous: '+str(self.continous) +'\nDataSet: '+self.dataset+ '\nProtocol: '+str(self.protocol)

##Callbacks
class DataReaderCallBack:
    def pushLogData(self, logData:LogData):
        return

class PacketReaderCallBack:
    def pushLogPacket(self, logPacket:LogPacket):
        return

class Protocol:
    def sendPacket(self,parsedPacket:ParsedPacket):
        return
    def initProtocol(self,cfg:Cfg):
        return
    def close(self):
        return
import common.DataReader
import common.PacketReader
import processbasic.ProcessBasic
from fann2 import libfann
from common.Types import Protocol
import time

class BmPyton:
    def __init__(self, cfg, client):
        self.cfg =cfg;
        self.client:Protocol = client;

    def read(self):
        start = time.process_time();
        self.client.initProtocol(self.cfg)
        ann=libfann.neural_net()
        ann.create_from_file("./data/net_16000.net")

        proccess = processbasic.ProcessBasic.ProcessBasic(ann,self.client)
        packetReader =common.PacketReader.PacketReader(proccess);
        dataReader = common.DataReader.DataReader(self.cfg, packetReader);
        dataReader.readDataSet();

        dataReader.printFiles();
        packetReader.printSamples();
        proccess.printPackets();
        self.client.close();
        end = time.process_time();

        print("Time: "+str((end-start)*1000)+"ms" );
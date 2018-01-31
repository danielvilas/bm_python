import common.DataReader
import common.PacketReader
import processbasic.ProcessBasic
from fann2 import libfann
from common.Types import Protocol

class BmPyton:
    def __init__(self, cfg, client):
        self.cfg =cfg;
        self.client:Protocol = client;

    def read(self):
        self.client.initProtocol(self.cfg)
        ann=libfann.neural_net()
        ann.create_from_file("./data/net_16000.net")

        proccess = processbasic.ProcessBasic.ProcessBasic(ann,self.client)
        packetReader =common.PacketReader.PacketReader(proccess);
        dataReader = common.DataReader.DataReader(self.cfg, packetReader);
        dataReader.readDataSet();

        self.client.close()
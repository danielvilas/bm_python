from common.Types import DataReaderCallBack,LogData,LogPacket,PacketReaderCallBack

class PacketReader(DataReaderCallBack):
    packets:LogPacket=LogPacket()
    callback:PacketReaderCallBack=None

    def __init__(self, cb:PacketReaderCallBack=None):
        self.callback=cb

    def pushLogData(self, logData:LogData):
        self.packets.addLogData(logData);
        if len(self.packets)==1024:
            cb:PacketReaderCallBack=self.callback
            if cb != None: cb.pushLogPacket(self.packets)
            self.packets=LogPacket()

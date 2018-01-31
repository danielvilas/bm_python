from common.Types import ParsedPacket,Protocol,Cfg
import paho.mqtt.client as mqtt

class MqttProtocol(Protocol):
    client:mqtt.Client
    def initProtocol(self,cfg:Cfg):
        self.client =mqtt.Client("BmPython_mqtt")
        self.client.connect(cfg.server)
        #todo change port

    def sendPacket(self,parsedPacket:ParsedPacket):
        tmp = "\"date\": \"{}\",\"tv\": {},\"bluray\": {},\"appleTv\": {},\"ipTv\":  {}"
        json = tmp.format(parsedPacket.date.isoformat(),parsedPacket.tv,parsedPacket.bluray,parsedPacket.appleTv,parsedPacket.ipTv)

        self.client.publish("AppliancesBucket","{"+json+"}")

    def close(self):
        self.client.disconnect()
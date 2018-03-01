from common.Types import ParsedPacket,Protocol,Cfg
import paho.mqtt.client as mqtt

class MqttProtocol(Protocol):
    client:mqtt.Client

    def onPublish(self,client, userdata, mid):
        self.pendingMsg-=1;

    def initProtocol(self,cfg:Cfg):
        self.client =mqtt.Client("BmPython_mqtt")
        self.client.connect(cfg.server)
        #todo change port
        self.pendingMsg=0;
        self.client.on_publish=self.onPublish

    def sendPacket(self,parsedPacket:ParsedPacket):
        super().sendPacket(parsedPacket)
        tmp = "\"date\": \"{}\",\"tv\": {},\"bluray\": {},\"appleTv\": {},\"ipTv\":  {}"
        json = tmp.format(parsedPacket.date.isoformat(),parsedPacket.tv,parsedPacket.bluray,parsedPacket.appleTv,parsedPacket.ipTv)
        self.pendingMsg+=1;
        self.client.publish("AppliancesBucket","{"+json+"}")

    def close(self):
        self.client.disconnect()
        super().close()
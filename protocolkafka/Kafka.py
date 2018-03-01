from common.Types import ParsedPacket,Protocol,Cfg
from kazoo.client import KazooClient
import json
import kafka

class KafkaProtocol(Protocol):
    zk:KazooClient
    producer:kafka.producer
    def initProtocol(self,cfg:Cfg):

        self.zk = KazooClient(hosts=cfg.server+":2181")
        self.zk.start()

        endpoints=[]

        children = self.zk.get_children("/brokers/ids")
        print("There are %s children with names %s" % (len(children), children))
        for child in children:
            childData, sats=self.zk.get("/brokers/ids/"+child)
            jsonData =childData.decode('UTF-8')
            jsonData= json.loads(jsonData)
            print(jsonData)
            endpoints.append(jsonData['host']+':'+str(jsonData['port']))
        self.zk.stop()
        self.producer=kafka.KafkaProducer(bootstrap_servers=endpoints)

    def sendPacket(self,parsedPacket:ParsedPacket):
        super().sendPacket(parsedPacket)
        tmp = "\"date\": \"{}\",\"tv\": {},\"bluray\": {},\"appleTv\": {},\"ipTv\":  {}"
        json = tmp.format(parsedPacket.date.isoformat(),parsedPacket.tv,parsedPacket.bluray,parsedPacket.appleTv,parsedPacket.ipTv)

        #self.client.publish("AppliancesBucket","{"+json+"}")
        json="{"+json+"}"
        self.producer.send("AppliancesBucket",value=json.encode("UTF-8"))
        #self.producer.flush()


    def close(self):
        self.producer.flush() #Waits until all messages are sent (ACK)
        super().close()
        self.producer.close()
from common.Types import ParsedPacket,Protocol,Cfg
import requests

class RestProtocol(Protocol):
    url:str
    def initProtocol(self,cfg:Cfg):
        self.url ="http://"+cfg.server+":9090/api/addPacket"
        #todo change port

    def sendPacket(self,parsedPacket:ParsedPacket):
        tmp = "\"date\": \"{}\",\"tvSeconds\": {},\"bluraySeconds\": {},\"appleTvSeconds\": {},\"ipTvSeconds\":  {}"
        json = tmp.format(parsedPacket.date.isoformat(),parsedPacket.tv,parsedPacket.bluray,parsedPacket.appleTv,parsedPacket.ipTv)

        data = "{"+json+"}"

        headers=dict()
        headers['content-type']='application/json'
        response = requests.post(self.url, data=data,headers=headers)
        #print(response)
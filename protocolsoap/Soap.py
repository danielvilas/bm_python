from common.Types import ParsedPacket,Protocol,Cfg
import requests

class SoapProtocol(Protocol):
    url:str
    def initProtocol(self,cfg:Cfg):
        self.url ="http://"+cfg.server+":9090/ws"
        #todo change port

    def sendPacket(self,parsedPacket:ParsedPacket):
        super().sendPacket(parsedPacket)
        tmp = "\"date\": \"{}\",\"tvSeconds\": {},\"bluraySeconds\": {},\"appleTvSeconds\": {},\"ipTvSeconds\":  {}"

        tmp='''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:data=\"http://daniel.es/outputgui/data">
           <soapenv:Header/>
           <soapenv:Body>
              <data:AddPacketRequest>
                 <data:packet>
                    <data:date>{}</data:date>
                    <data:tvSeconds>{}</data:tvSeconds>
                    <data:bluraySeconds>{}</data:bluraySeconds>
                    <data:appleTvSeconds>{}</data:appleTvSeconds>
                    <data:ipTvSeconds>{}</data:ipTvSeconds>
                 </data:packet>
              </data:AddPacketRequest>
           </soapenv:Body>
        </soapenv:Envelope>
        '''


        xml = tmp.format(parsedPacket.date.isoformat(),parsedPacket.tv,parsedPacket.bluray,parsedPacket.appleTv,parsedPacket.ipTv)

        data = xml

        headers=dict()
        headers['content-type']='text/xml'
        response = requests.post(self.url, data=data,headers=headers)
       #print(response)
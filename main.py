from common import cmd,bmpyton;
from protocolmqtt import Mqtt
from protocolkafka import Kafka
from protocolrest import Rest
from protocolsoap import Soap
args = cmd.parseArgs(True)
print (args)

client=None

if "MQTT" == args.protocol: client= Mqtt.MqttProtocol()
if "KAFKA"== args.protocol: client= Kafka.KafkaProtocol()
if "REST"== args.protocol: client= Rest.RestProtocol()
if "WS"== args.protocol: client= Soap.SoapProtocol()

bmpyton = bmpyton.BmPyton(args,client)
bmpyton.read()

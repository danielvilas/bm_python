import argparse
from common import Types

def parseArgs( isFull=False):
    parser = argparse.ArgumentParser(description='Phyton BenchMark IoT')

    parser.add_argument('-d','--dataset', help='DataSet to use', type = str, required=True)
    parser.add_argument('-s','--server', help='Server IP to use', type = str, default='server.local')
    parser.add_argument('-c','--continous', help='Continuos mode', type = bool, default = False)
    if(isFull):
        parser.add_argument('-p', '--protocol', help='Client to use MQTT|WS|KAFKA|REST', choices=['MQTT','WS','KAFKA','REST'] ,type=str, required=True)

    args = parser.parse_args()

    cfg = Types.Cfg();
    cfg.continous=args.continous
    if(isFull):
        cfg.protocol=args.protocol
    cfg.dataset=args.dataset
    cfg.server=args.server

    return cfg


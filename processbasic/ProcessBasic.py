from common.Types import PacketReaderCallBack,LogPacket,ParsedPacket,Protocol
import numpy.fft
from fann2 import libfann
from math import floor

class ProcessBasic(PacketReaderCallBack):

    ann:libfann.neural_net=None
    callback:Protocol=None

    def __init__(self, ann:libfann.neural_net,callback:Protocol=None):
        self.ann=ann
        self.callback=callback
        self.packets=0;


    def getMagnitude(self,fft:numpy.fft, freq):
        #freqs = numpy.fft.fftfreq(300,1/1000)
        i= freq * (300 / 2) / 500
        i= floor(i)
        return numpy.absolute(fft[i]) #*300/2

    def proccesSamples(self,logPacket:LogPacket, offset:int):
        a0=numpy.empty(300)
        average = 0.0
        for i in range(0,299) :
            value=logPacket.packets[offset+i].a0
            value=float(value-512)/512.0
            a0[i]=value
            average+=abs(value)
        average /= 300
        fft = numpy.fft.fft(a0)
        return [self.getMagnitude(fft,50),
                self.getMagnitude(fft, 150),
                self.getMagnitude(fft, 250),
                self.getMagnitude(fft, 350),
                average]


    def pushLogPacket(self, logPacket:LogPacket):
        self.packets+=1
        data0=self.proccesSamples(logPacket, 0)
        data3=self.proccesSamples(logPacket, 3)
        data6=self.proccesSamples(logPacket, 6)
        data9=self.proccesSamples(logPacket, 1023-300)

        res0 = self.ann.run(data0)
        res3 = self.ann.run(data3)
        res6 = self.ann.run(data6)
        res9 = self.ann.run(data9)

        out=[0.0, 0.0, 0.0, 0.0]
        for i in range(0,4):
            out[i]=(res0[i]+res3[i]+res6[i]+res9[i])/4
        parsedPacket= ParsedPacket(logPacket.packets[0].date,out)
        if self.callback!=None : self.callback.sendPacket(parsedPacket)

    def printPackets(self):
        print("Packets: " + str(self.packets))

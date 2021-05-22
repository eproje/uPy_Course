#kutuphane olusturmak
from machine import ADC, Pin
import time

#yeni bir class olusturma
class LDR:
    value=55
    
    def __init__ (self,pin):
        self.adc= ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)
    def read_avr(self,sample):
        toplam=0
        for x in range(sample):
            toplam += self.adc.read()
            
        return int(toplam / sample)
    def read(self):
        # +,- 16 histerisiz
        for x in range(128):
            temp=self.read_avr(8)#
            #histerisiz
            if temp > self.value + 4:
                self.value +=1
            elif self.value > temp + 4:
                self.value -=1
            #histerisiz
        return self.value
    
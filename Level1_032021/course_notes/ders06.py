import time
import machine

from machine import Pin
Led1=Pin(22, Pin.OUT)
Led2=Pin(23, Pin.OUT)

def YakSondur(pinNo,sure,tekrar):
    for i in range (tekrar * 2 ):# kitap sayfa 73
        pinNo.value(1 - pinNo.value()) # toogle değerin tersini alır
        time.sleep(sure)
 
try:
    #program çalışırken yapılacak işler
    while (True):
        YakSondur(Led1,0.05,3)
        YakSondur(Led2,0.05,3)
except KeyboardInterrupt:
    #program durdurulduğunda yapılacak işler
    Led1.value(0)
    Led2.value(0)
    
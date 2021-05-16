# DHT11 sicaklik ve nem sensoru
# DHT11    ESP32
# sinyal   2
# VCC      3V
# GND      G
# kaynak: https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
#
# https://docs.micropython.org/en/latest/library/uerrno.html

import machine
from machine import Pin
import dht
import time
import uerrno

#dht_pin = Pin(2, Pin.IN)
#DHTsensor= dht.DHT11(dht_pin)
#veya
DHTsensor= dht.DHT11( Pin(2, Pin.IN) )
#hatalar
# IndentationError (girinti hatası)
# OSError:ETIMEDOUT (haberleşme zaman aşımı)

dht_okuma_zamani=0

def DHT_OKU():
    global dht_okuma_zamani    
    try:
        DHTsensor.measure()
        sicaklik= DHTsensor.temperature() # santigrad cinsinde
        nem=DHTsensor.humidity() # % cinsinden nem degeri
        print ("sıcaklik ", sicaklik, " nem ", nem)
        time.sleep(dht_okuma_zamani)
        
    except Exception as hata:
        print (hata)
        #print (hata.args[0])
        # ETIMEDOUT hatasi slave cihazdan verilen zaman içinde veri gelmiyor
        # EX print(uerrno.errorcode[uerrno.EEXIST])
        if (hata.args[0]==uerrno.ETIMEDOUT) : #ETIMEDOUT
            print ("DHT11 zaman asimi")
            dht_okuma_zamani+=0.1
            print("DHT_time=",dht_okuma_zamani)
try:
    while True:
        DHT_OKU()
        
except KeyboardInterrupt:
    print ("Program Sonlandirildi")

except OSError:
    print ("Sistem hatasi")

except Exception as e:
    print (e)























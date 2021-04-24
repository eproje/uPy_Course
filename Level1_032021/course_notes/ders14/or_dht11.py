# DHT11 sicaklik ve nem sensoru
# DHT11    ESP32
# sinyal   2
# VCC      3V
# GND      G
# kaynak: https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html

import machine
from machine import Pin
import dht
import time

#dht_pin = Pin(2, Pin.IN)
#DHTsensor= dht.DHT11(dht_pin)
#veya
DHTsensor= dht.DHT11( Pin(2, Pin.IN) )

try:
    while True:
        DHTsensor.measure()
        sicaklik= DHTsensor.temperature() # santigrad cinsinde
        nem=DHTsensor.humidity() # % cinsinden nem degeri
        print ("sıcaklik ", sicaklik, " nem ", nem)
        time.sleep(1)
        # ETIMEDOUT hatasi slave cihazdan verilen zaman içinde veri gelmiyor
except:
    print ("Bir olay algilandi")
    #print ("makine resetlenecek")
    #machine.reset()
    #gelecek ders hata cozumleme yapacagiz.

# odev: OLED ekranda mesafe, sicaklik ve nem degerleri gosterilecek
# mesafe <10cm ise neopixel ledler kirmizi degilse yesil yanacak
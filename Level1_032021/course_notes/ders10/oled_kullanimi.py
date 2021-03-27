# OLED EKRAN KULLANIMI
"""
ESP32    OLED

3.3V --> VCC
G    --> GND
18   --> SCL
19   --> SDA

"""
"""
upip kullanimi (paket yükleyicisi,PIP karşılığıdır
upip kullanarak ssd1306 paketini esp32 ye yukluyoruz

import upip
dir(upip)
upip.install('micropython-ssd1306')

"""

import network
wifi=network.WLAN(network.STA_IF)

import aga_baglan
import machine
from machine import Pin, I2C

Led_status= Pin (22,Pin.OUT)
i2c = I2C(scl=Pin(18), sda=Pin(19), freq=400000)

#oled test
import ssd1306
oled=ssd1306.SSD1306_I2C(128,64,i2c)
oled.text("merhaba",0,0)
oled.show()


#timer objesi olusturmak
def tmr1_kesmesi(timer):
    #aga baglımıyım testi
    if wifi.isconnected():
        Led_status.value(1 - Led_status.value())#yanık
    else:
        Led_status.value(1)#sonuk
 
from machine import Timer
tmr1 = Timer(-1) # sanal zamanlayici olustur
tmr1.init(period=500, mode=Timer.PERIODIC, callback=tmr1_kesmesi)
#timer objesi olusturmak


    


    


    
    
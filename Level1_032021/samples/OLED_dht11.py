# author: h.serimer 03.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# OLED DHT11

from machine import Pin,I2C
import machine
import ssd1306
import dht    
import time
 
i2c = I2C(0)      #i2c hardware olarak baslatildi ESP32 icin scl=18, sda=19 
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3c) 
 
dht_pin=Pin(2, Pin.IN)
d=dht.DHT11(dht_pin)           
 
while True:
    d.measure()       #dht11 den sicaklik ve nem bilgisini olcer
    t=d.temperature() #Celsius cinsinden sicaklik degerini okur
    h=d.humidity()    #relative humidity cinsinden nem degerini okur
    print('Temperature=', t, 'C', 'Humidity=', h, '%')
    time.sleep(1)     #1sn bekler
    oled.fill(0)      #ekrani silmek icin
    oled.text("Temperature",20,10)
    oled.text(str(t),40,20)
    oled.text("*C", 60,20)
    oled.text("Humidity",30,40)
    oled.text(str(h),40,55)
    oled.text("%", 60,55)
    oled.show()   
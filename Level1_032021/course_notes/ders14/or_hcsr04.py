# HCSR04 mesafe sensoru
# Kutuphane : https://github.com/eproje/uPy_Course
# https://github.com/eproje/uPy_Course/tree/master/Level1_032021/upy_lib/hcsr04.py
# HCSR04    ESP32
# VCC       3V
# TRIG      13
# ECHO      15
# GND       G



from hcsr04 import HCSR04 # import hcsr04
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import time

import neopixel
led_sayisi=8
np = neopixel.NeoPixel(Pin(4) , led_sayisi)

oled = SSD1306_I2C(128,64,I2C(0)) #i2c hardware olarak kullaniliyor

MesafeSensoru = HCSR04(trigger_pin=13, echo_pin=15, echo_timeout_us=1000000)

while True:
    mesafe= int(MesafeSensoru.distance_cm())
    
    print(mesafe, " cm")
    
    oled.fill(0)
    oled.text("Mesafe",30,20)
    oled.text(str(mesafe),30,40) # degiskenler once string'e cevirilmelidir
    oled.show()
    
    if mesafe < 10:
        for n in range( led_sayisi ):
            np[n]= (32,0,0)
        
    else:
        for n in range( led_sayisi ):
            np[n]= (0,32,0)
    
    np.write()           
    time.sleep(0.1)













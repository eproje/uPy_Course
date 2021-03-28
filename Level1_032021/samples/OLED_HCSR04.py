from hcsr04 import HCSR04
from machine import Pin,I2C
import ssd1306
import time
 
i2c = I2C(0)      #i2c hardware olarak baslatildi ESP32 icin scl=18, sda=19 
oled=ssd1306.SSD1306_I2C(128,64,i2c) 
 
sensor = HCSR04(trigger_pin=13, echo_pin=15,echo_timeout_us=1000000)
 
try:
  while True:
    distance = sensor.distance_cm()
    print(distance)
    oled.fill(0)
    oled.text("Distance:",30,20) 
    oled.text(str(distance),30,40)
    oled.show()
    time.sleep(0.1)
except KeyboardInterrupt:
       pass    
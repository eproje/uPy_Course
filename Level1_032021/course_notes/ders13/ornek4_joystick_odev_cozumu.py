# Joystick ornegidir
# X ve Y degerlerini kullanarak ekrana hareketli sekil cizer


# joystick    ESP
# GND         GND
# 5V          3V
# VRX         34
# VRY         35
# SW          32

# https://docs.micropython.org/en/latest/esp32/quickref.html
# p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor

JOYSTICK_XPIN = 34
JOYSTICK_YPIN = 35
JOYSTICK_SWPIN =32
BUZZER_PIN = 5
NEOPIXEL_PIN = 4

from machine import * #Pin, ADC, I2C
from time import sleep
import ssd1306
oled = ssd1306.SSD1306_I2C(128,64,I2C(0, freq=800000)) #hardware
 
Joystic_x = ADC (Pin(JOYSTICK_XPIN)) # ADC giris 16bit
Joystic_y = ADC (Pin(JOYSTICK_YPIN))  # ADC giris 16bit
Joystic_sw = Pin(JOYSTICK_SWPIN, Pin.IN, Pin.PULL_UP) # dijital giris 1bit

Joystic_x.atten(ADC.ATTN_11DB)
Joystic_y.atten(ADC.ATTN_11DB)

y_list = [63] * 128 #dizi degiskeni
oled.fill(0) # oled i sil
oled.show() # oled e yaz


    
#while True:
#    #okuma islemleri
#    Joystic_xValue= Joystic_x.read()
#    Joystic_yValue= Joystic_y.read()
#    #Joystic_swValue = Joystic_sw.value()
#    #
#    y = 63 - int((Joystic_yValue * 63) / 4095)
#    y_list[127] = y
#    for x in range (0,127):
#        oled.pixel(x,y_list[x],0) #oncekini siler
#        y_list[x] = y_list[x+1] # 1 pixel kaydır
#        oled.pixel(x,y_list[x],1) # yeni degeri yukle
#    oled.show()
    

#odev Joystick ile ekranda hareket ettirilen daire yapılacak
# cozum
#kaynak https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/
# GFX kutuphanesi
import gfx
oled_width = 128
oled_height = 64

graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

while True:
    #joystick okuma 
    Joystic_xValue= Joystic_x.read()
    Joystic_yValue= Joystic_y.read()
    oled.fill(0)
    x=127 - int((Joystic_xValue * 127) / 4095)
    y=63 - int((Joystic_yValue * 63) / 4095)

# 1 pixel ile (basit yol)
    #oled.pixel(x,y,1) # en basiti 1 pixel
#GFX kutuphanesi ile, once GFX yukle
    graphics.fill_circle(x, y, 5, 1)
#
    oled.show()

    
        
        
    

    
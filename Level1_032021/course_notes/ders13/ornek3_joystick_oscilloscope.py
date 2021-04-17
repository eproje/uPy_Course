# Joystick ornegidir
# Y degeri osilaskop gibi gosterilir

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
oled = ssd1306.SSD1306_I2C(128,64,I2C(0, freq=400000)) #hardware
 
Joystic_x = ADC (Pin(JOYSTICK_XPIN)) # ADC giris 16bit
Joystic_y = ADC (Pin(JOYSTICK_YPIN))  # ADC giris 16bit
Joystic_sw = Pin(JOYSTICK_SWPIN, Pin.IN, Pin.PULL_UP) # dijital giris 1bit

Joystic_x.atten(ADC.ATTN_11DB)
Joystic_y.atten(ADC.ATTN_11DB)

y_list = [63] * 128 #dizi degiskeni
oled.fill(0) # oled i sil
oled.show() # oled e yaz
freq(240000000)
while True:
    #okuma islemleri
    #Joystic_xValue= Joystic_x.read()
    Joystic_yValue= Joystic_y.read()
    #Joystic_swValue = Joystic_sw.value()
    #
    y = 63 - int((Joystic_yValue * 63) / 4095)
    y_list[127] = y
    for x in range (0,127):
        oled.pixel(x,y_list[x],0) #oncekini siler
        y_list[x] = y_list[x+1] # 1 pixel kaydır
        oled.pixel(x,y_list[x],1) # yeni degeri yukle
    oled.show()
    
        
        
    

    
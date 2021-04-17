# Joystick ornegidir
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

from machine import Pin, ADC
from time import sleep

Joystic_x = ADC (Pin(JOYSTICK_XPIN)) # ADC giris 16bit
Joystic_y = ADC (Pin(JOYSTICK_YPIN))  # ADC giris 16bit
Joystic_sw = Pin(JOYSTICK_SWPIN, Pin.IN, Pin.PULL_UP) # dijital giris 1bit

Joystic_x.atten(ADC.ATTN_11DB)
Joystic_y.atten(ADC.ATTN_11DB)

while True:
    #okuma islemleri
    Joystic_xValue= Joystic_x.read()
    Joystic_yValue= Joystic_y.read()
    Joystic_swValue = Joystic_sw.value()
    
#    print("X=",Joystic_xValue, " Y=", Joystic_yValue, " SW=", Joystic_swValue )
    if Joystic_xValue < 100 :
        print("Sag")
    if Joystic_xValue > 4000 :
        print("Sol")
    if Joystic_yValue < 100 :
        print("Asagi")
    if Joystic_yValue > 4000 :
        print("Yukari")
    if Joystic_swValue == 0 :
        print("Basili")
        
    sleep(0.05)
    
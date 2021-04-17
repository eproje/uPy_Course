"""
neopixel baglantisi
PIXEL  ESP32
GND  - G
DIN  - 4
4-7V - 3V3

"""
import neopixel
import utime
#import machine
from machine import Pin
led_sayisi=8
np = neopixel.NeoPixel(Pin(4) , led_sayisi)
#buzzer kullanimi icin
# PIN5  - BUZZER +
# GND   - BUZZER -
from machine import PWM
buzzer_pin=5
beeper=PWM(Pin(buzzer_pin))

#BUZZER TEST
#beeper.freq(500)
#beeper.duty(512)
#utime.sleep(1)
#beeper.deinit()


"""
np[0]= (255,0,0) #renk sayisi 255*255*255 kadardır, sıralama Red, Green, Blue
np[1]= (0,255,0)
np[2]= (0,0,255)
np[3]= (23,210,230)
np.write()
"""

def Clear():
    for n in range( led_sayisi ):
        np[n]= (0,0,0)
    np.write()

def Polis():
    while True:
        for j in range(3):
            for i in range(4):
                np[i]= (255,0,0)
            np.write()
            #
            utime.sleep(0.05)
            Clear()
            utime.sleep(0.05)
            #
            
        for j in range(3):
            for i in range(4,8):
                np[i]= (0,0,255)
            np.write()
            #
            utime.sleep(0.05)
            Clear()
            utime.sleep(0.05)
            #

#MULTITASKING coklu gorev yonetimi
import _thread
_thread.start_new_thread (Polis,())

#program calistigi surece
try:
    while True:
        #Polis()
        #print("merhaba")
        beeper.duty(512)#0...1023
        beeper.freq(950)
        utime.sleep(0.3)
        beeper.freq(700)
        utime.sleep(0.3)
#program herhangi bir sebeple durduğunda
except:
    beeper.deinit()#buzzeri kapat
    Clear()#neopixel ledleri sondur
            
            
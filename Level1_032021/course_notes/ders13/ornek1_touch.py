# https://mpython.readthedocs.io/en/master/library/micropython/machine/machine.TouchPad.html

from machine import TouchPad, Pin # hafıza tüketimi az  
#from machine import * # kütüphane içind#eki büyün alt class ları alır (hafıza tüketimi fazla)
from time import sleep

Touch1 =TouchPad (Pin(12))

while True:
    Touch1_value = Touch1.read()
    print("Touch1=",Touch1_value)
    sleep(0.5)
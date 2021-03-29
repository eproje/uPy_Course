#simple DAC
from machine import DAC
from machine import Pin

dac0=DAC(Pin(25))
dac1=DAC(Pin(26))

dac0.write(128)#1.75V
dac1.write(64)#0.9V
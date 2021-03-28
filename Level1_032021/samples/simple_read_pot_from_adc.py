# author: h.serimer 03.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# read POT from ADC input
# ESP32 ADC functionality is available on Pins 32-39.
# REF: https://docs.micropython.org/en/latest/esp32/quickref.html

# POT  ESP32
# PIN1 3V3
# PIN2 ADC_PIN
# PIN3 GND


from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(39))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)
# author: h.serimer 03.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# blink LED

from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)#build in LED

while True:
  led.value(not led.value())
  sleep(0.5)
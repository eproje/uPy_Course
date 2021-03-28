# author: h.serimer 03.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# simple touch
# There are ten capacitive touch-enabled pins that can be used on the ESP32: 0, 2, 4, 12, 13 14, 15, 27, 32, 33.
# Trying to assign to any other pins will result in a ValueError.
# REF: https://docs.micropython.org/en/latest/esp32/quickref.html


from machine import TouchPad, Pin
from time import sleep

touch_pin1 = TouchPad(Pin(12))
touch_pin2 = TouchPad(Pin(14))

while True:
  touch_value1 = touch_pin1.read()
  touch_value2 = touch_pin2.read()
  print(touch_value1,"-",touch_value2)
  sleep(0.5)
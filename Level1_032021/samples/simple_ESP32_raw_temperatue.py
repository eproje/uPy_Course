# author: h.serimer 03.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# read internal HALL sensor from esp32 chip
# REF: https://docs.micropython.org/en/latest/library/esp32.html

from time import sleep
import esp32

#ref
#esp32.hall_sensor()     # read the internal hall sensor
#esp32.raw_temperature() # read the internal temperature of the MCU, in Farenheit
#esp32.ULP()             # access to the Ultra-Low-Power Co-processor

while True:
  print(esp32.raw_temperature())
  sleep(0.1)
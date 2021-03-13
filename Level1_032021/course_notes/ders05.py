import time
import machine

from machine import Pin
Led1=Pin(22, Pin.OUT)
Led2=Pin(19, Pin.OUT)

while (True):
   Led1.value(1)
   Led2.value(0)
   time.sleep(0.5)
   Led1.value(0)
   Led2.value(1)
   time.sleep(0.5)

#ödev 0.1sn aralikla LED1 5 kez yanıp sönsün ardından sönsün
# devamında 0.1sn aralikla LED2 5 kez yanıp sönsün ardından sönsün
# program tekrarlansın
# ipucu POLİS LAMBASI
# şartlar: yazılan program fonksiyon olmalı

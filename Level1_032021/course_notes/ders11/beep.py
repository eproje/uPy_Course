# beep ornegi
# 5 numaralı uca baglı hoparlörden BEEP sesi yapacak

from machine import Pin, PWM
import utime

BuzzerPin=5

def beep(frekans, time):
    beeper = PWM(Pin(BuzzerPin,Pin.OUT), freq=frekans, duty=512)
    utime.sleep(time)
    beeper.deinit()


beep(1000,0.1)
beep(800,0.1)
beep(600,0.1)

# sozluk tipi degisken
notalar= { 'c' : 262, 'd' : 294, 'e' : 330, 'f': 349, 'g': 392, 'a':440, 'b':494, 'C':523, ' ':0}  
print(notalar)

melodi = ' cdefgabC'
for nota in melodi:
   beep(notalar[nota],0.1) 
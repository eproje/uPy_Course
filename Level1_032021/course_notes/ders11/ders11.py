# time ve ntptime ile saat yapımı

import network
wifi=network.WLAN(network.STA_IF)

import aga_baglan
import machine
from machine import Pin, I2C
import ssd1306
import utime
import ntptime


Led_status= Pin (22,Pin.OUT)
#i2c = I2C(scl=Pin(18), sda=Pin(19), freq=400000)#software I2C
i2c= I2C(0) # hardware I2C

oled=ssd1306.SSD1306_I2C(128,64,i2c)
oled.fill(0)
oled.show()

#GLOBAL degiskenler
SAATFARKI=3
dakikasayaci=0
haftaninGUNU=('Pazartesi','Sali','Carsamba','pPersembe','Cuma','Cumartesi','Pazar')


def ntpGuncelle():
    ntptime.settime()
    print("Saat guncellendi")
    
def ntpOLEDyazdir():
    localtime = utime.localtime(utime.time() + SAATFARKI * 3600)
    print(localtime)#tuple degisken cıktı: (2021, 4, 3, 14, 12, 49, 5, 93)
    #print(localtime[0]) #cıktı : 2021
    #deger=haftaninGUNU[localtime[6]]
    # odev **** ekranı ortala fonksiyonu yaz
    deger=int (127 - ((len(haftaninGUNU[localtime[6]])*16)/2))
    print(deger)
    #hatalı print( ( (127 - len(deger))*16 / 2) ) #işlem önceliği
    #print ( 127 - ((len(deger)*16)/2) )
    #print(haftaninGUNU[localtime[6]])
    #print('{0:04d}-{1:02d}-{2:02d}'.format(*localtime)) # cikti=2021-04-03
    #print('{3:02d}:{4:02d}:{5:02d}'.format(*localtime)) 
    #
    oled.fill(0)
    oled.text(haftaninGUNU[localtime[6]], 8,8)
    oled.text('{0:04d}-{1:02d}-{2:02d}'.format(*localtime),8,24)
    oled.text('{3:02d}:{4:02d}:{5:02d}'.format(*localtime),8,40)
    #
    oled.show()    
    
#timer objesi olusturmak
def tmr1_kesmesi(timer):
    global dakikasayaci# global degiskeni localde kullanmak için
    
    dakikasayaci=dakikasayaci+1 # bu daha kısa yazılabilir mi?
    if dakikasayaci >= 59:
        ntpGuncelle()
        dakikasayaci=0
        
    
    ntpOLEDyazdir()
    #aga baglımıyım testi
    if wifi.isconnected():
        Led_status.value(1 - Led_status.value())#yanık
    else:
        Led_status.value(1)#sonuk
 
from machine import Timer
tmr1 = Timer(-1) # sanal zamanlayici olustur
tmr1.init(period=1000, mode=Timer.PERIODIC, callback=tmr1_kesmesi)
#timer objesi olusturmak
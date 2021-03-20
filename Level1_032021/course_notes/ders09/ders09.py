"""
Bu derste ESP32 Upy bagimsiz(bilgisayar baglantisi olmadan) calistirmayi deniyoruz.

uPy ESP32 resetlendiğinde otomatik olarak boot.py dosyasını çalıştırır

daha fazla bilgi: http://docs.micropython.org/ 

otomatik calismasını istedigimiz dosyayı boot.py icine

import ders09

seklinde yaziyoruz
"""

#kutuphaneler
import network
import urequests as requests
import ujson

from machine import Pin
role1=Pin(16, Pin.OUT)
role2=Pin(17, Pin.OUT)


print("Ders09 basladi")

#degiskenler
aio_key = "io keyiniz"
aio_username= "io kullanici adiniz"
headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}

#aga baglanmak icin gerekenler
print("aga baglaniliyor...") #debug satiri

wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('wifi adiniz', 'wifi sifreniz')

#aga baglanincaya kadar bekle
while not wifi.isconnected():
    pass

print("aga baglandi") #debug satiri


# API	https://io.adafruit.com/api/v2/Cezeri/feeds/lamba1
def LambaDegeriGetir(feedname):
    url = "https://io.adafruit.com/api/v2/" + aio_username +  "/feeds/" + feedname + "/data/last"
    response = requests.get(url,headers=headers)
    parsed = ujson.loads(response.text)
    value= parsed['value']
    
    print (feedname, value)#debug satiri
    
    if value=="OFF":
        return False
    else:
        return True
    
    
while (True):
    role1.value (1 - LambaDegeriGetir('lamba1'))
    role2.value (1 - LambaDegeriGetir('lamba2'))

"""

yasadiginiz sorunlari not etmeyi unutmayin.
bir sonraki ders sorunlar-cozumler isledikten sonra,
sistemimize OLED ekran baglayacak ve
bir baska web sitesinden saat bilgisi okuyacagiz

"""
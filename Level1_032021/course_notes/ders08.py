"""
1. https://io.adafruit.com
adresine giderek uye olun
2. yeni bir "dashboard" tanimlayin
3. yeni bir "feed" yanimlayin
	bunun icin "create new block" sekmesini kullanin
	bu ornekte lamba1 ve lamba2 isminde 2 adet feed tanimliyoruz
4. dashboard ekranindan "My Key" menusunu kullanarak USERNAME ve IO_KEY bilgilerinizi alin ve not edin.

or:
ADAFRUIT_IO_USERNAME = "Cezeri"
ADAFRUIT_IO_KEY = "aio_ATQH26cyTl2R2MhZrBqMtwbKD11m"

5. api baglanti linkinin nasil olacagini gorun.
bunun icin tanimladiginiz feed uzerine tiklayarak detaylar bolumune gecin
ardindan "Feed Info" seceneginden 
	Name, Key ve link bilgilerini ogrenin

or:
Name: Lamba1
Key : lamba1
API	: https://io.adafruit.com/api/v2/Cezeri/feeds/lamba1



"""
#kutuphaneler
import network
import urequests as requests
import ujson

from machine import Pin
Led1=Pin(22, Pin.OUT)
Led2=Pin(23, Pin.OUT)

#degiskenler
#aio_key=ADAFRUIT_IO_USERNAME
#aio_username= ADAFRUIT_IO_KEY
# kendi bilgilerinizi kullanin
# ornekteki bilgiler sizi baska kullaniciya baglar


aio_key = "aio_ATQH26cyTl2R2MhZrBqMtwbKD11m"
aio_username= "Cezeri"

headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}

#wifi aginiza baglanin

wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('FB007', 'Cezeri1049')
while not wifi.isconnected():
    pass

# veri okumak icin URL bilgisini olusturun
# bundan faydalanin
# API	https://io.adafruit.com/api/v2/Cezeri/feeds/lamba1
def LambaDegeriGetir(feedname):
    url = "https://io.adafruit.com/api/v2/" + aio_username +  "/feeds/" + feedname + "/data/last"
    response = requests.get(url,headers=headers)
    parsed = ujson.loads(response.text)
    value= parsed['value']
    
    print (feedname, value)
    if value=="OFF":
        return False
    else:
        return True
    
    
while (True):
    Led1.value (LambaDegeriGetir('lamba1'))
    Led2.value (LambaDegeriGetir('lamba2'))

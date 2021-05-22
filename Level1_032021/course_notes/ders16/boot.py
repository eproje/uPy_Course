# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()



#https://docs.micropython.org/en/latest/library/usocket.html?highlight=usocket
try:
  import usocket as socket
except:
  import socket


from machine import Pin

import network# esp32 nin wifi ağlarına bağlanma araçlarını içerir
# https://docs.micropython.org/en/latest/library/esp.html?highlight=esp#module-esp
# https://docs.micropython.org/en/latest/library/esp32.html?highlight=esp#module-esp32

# hata ayıklama modülü kapalı kalsın, hafızada yer kazanılır
import esp
esp.osdebug(None)

# garbage collect
# tüm değişken ve işlemler RAM(yaz/boz rasgele erişimli bellek) de yapılır
# çalışan her komut hafızada birşeyler bırakır
# gc.collect() fonksiyonu hafızayı y-temizler
import gc
gc.collect()

# wifi
# 1 dogrudan
# 2 erişim noktası AP (Access Point)
print('Start')

# 1
#ssid = 'upykursu'
#sspassword = '12345678'
#station = network.WLAN(network.STA_IF)# AP baslatılır
#station.active(True)# AP aktif yapılır
#station.connect(ssid, sspassword)# # AP adı ve şifresi belirlenir
#while station.isconnected() == False:
#    pass
#print('Baglanti olusuruldu')
#print(station.ifconfig())

#2
APid = 'upykursu'
APpassword = '12345678'
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=APid, password=APpassword)
ap.config(authmode=3)#şifreleme kullan

while ap.active() == False:
  pass
print('AP olusuruldu')
print(ap.ifconfig())


led = Pin(22, Pin.OUT)
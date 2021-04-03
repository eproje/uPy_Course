# author: h.serimer 04.2021 https://github.com/eproje/uPy_Course
# Board: Lolin32 Lite
# OLED ile basit osiloskop

from machine import * #machine kutuphanesindeki tum objeler
import ssd1306
import gc

#hardware I2C-0, overclock(1.2Mhz)
oled = ssd1306.SSD1306_I2C(128, 64, I2C(0,freq=1200000))
#ADC input
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

freq(240000000) #overclock, normalde 160Mhz
y_list = [63] * 128 #128 elemanli baslangic degeri 63 olan dizi OSC gorunumu icin

oled.fill(0)#oled buffer temizlensin onceki calismalardan birseyler kalmis olabilir

print("Program basladi")

while True:
    y = 63-int((pot.read() * 63)/4095)
    y_list[127] = y
    for x in range(0, 127):
        oled.pixel(x,y_list[x],0) #oncekini sil
        y_list[x] = y_list[x+1]   #1 pixel kaydir
        oled.pixel(x,y_list[x], 1)#yeniyi yukle
    oled.show()#oled tazele/yazdir
    gc.collect()#hafiza temizlensin



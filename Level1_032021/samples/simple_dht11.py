# REF :  https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
# works on all pins | tüm pinlerde kullanilabilir.

import dht
import machine
from time import sleep
#ornekler
#d = dht.DHT11(machine.Pin(4))
#d.measure()
#d.temperature() # eg. 23 (°C)
#d.humidity()    # eg. 41 (% RH)

#d = dht.DHT22(machine.Pin(4))
#d.measure()
#d.temperature() # eg. 23.6 (°C)
#d.humidity()    # eg. 41.3 (% RH)

sensor = dht.DHT11(machine.Pin(2))
while True:
    try:
        sleep(2)
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
#        print('Sicaklik: %3.1f C' %t)
#        print('Nem: %3.1f %%' %h)
        print('Sicaklik=', t, 'C', 'Nem=', h, '%')
    except OSError as e:
        print('Sensor okuma hatasi')
    

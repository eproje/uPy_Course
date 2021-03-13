"""
esp32 Upy kartımızı internetere bağlıyoruz

"""
import network
wifi=network.WLAN(network.STA_IF)
wifi.active(True)
# wifi.ifconfig() #IP bilgilerimizi ogrenmek icin
aglar=wifi.scan() # cevredeki wifi ağları tarar

print ( len(aglar) , " adet network bulundu") # listelenen ağların sayısı
# ağlar listesini tek tek yazdıralım
for net in aglar: # in sayfa 71
    print(net)
# kendi ağımıza bağlanıyoruz    
wifi.connect('FB007', 'Cezeri1049')
while not wifi.isconnected():
    pass

print ("bagli")
print ("Config=", wifi.ifconfig()) #bağlı olduğumuz ağın bilgileri 





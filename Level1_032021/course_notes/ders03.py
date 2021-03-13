#ders02
"""
Koşullu ifadeler
IF ELIF ELSE
fonksiyon oluşturma, fonfiyon kavramı
"""
#fonksiyonlar
def merhaba_yazdir(kim):
    print( "merhaba ", kim, " hoşgeldin")

#********************************************************************
   
def karsilastir():
    sayi1 = input ("sayi1 nedir? ")
    sayi2 = input ("sayi2 nedir? ")

    if sayi1   <   sayi2 :
        print("sayi1 küçüktür sayi2")
    elif sayi1 > sayi2 :
        print("sayi1 büyüktür sayi2")
    else:
        print("sayi1 eşittir sayi2")

#ana program burada baslıyor
        
print ("Programım başladi")
merhaba_yazdir(input("Sen kimsin ?"))
karsilastir()
print ("Programım bitti")



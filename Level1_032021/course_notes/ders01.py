# bu ilk programımdır
# dairenin cevresini ve alananını hesaplar
# cevre = 2 pi r
# alan = pi r kare

#degiskenler
pi=3.14
cevre=0
alan=0
yaricap=0

#program

yaricap= input("Yaricap nedir? (mm) = ")

cevre= 2 * float(pi) * float(yaricap)
alan= pi * float(yaricap) * float(yaricap)

print("Cevre=", cevre, " mm dir")
print("Alan=", alan, " mm2 dir")

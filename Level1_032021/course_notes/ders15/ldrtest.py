from ldr import LDR

import time

ldr1 = LDR(39) # __init__ calisir

while True:
    
    isik=ldr1.read() # read calisir
    
#    for n range(128):
#        toplam += isik=ldr1.read()
#    isik=int(toplam/128)        
    print ("ldr degeri=",isik)
    #time.sleep(0.1)
    

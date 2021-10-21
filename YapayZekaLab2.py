# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:06:20 2021

@author: furka
"""

#birinci soru
try:
    print("3 tane değer giriniz")
    birinciAci=int (input('Birinci aci: '))
    ikinciAci=int (input('İkinci aci: '))
    UcuncuAci=int (input('Üçüncü aci: '))

    kontrol1=birinciAci+ikinciAci
    kontrol2=kontrol1+UcuncuAci

    if kontrol1== 90 and UcuncuAci >90:
        print("Bu bir üçgen değildir")
     
    if kontrol2>180:
        print("Bu bir üçgen değildir")

    if kontrol2<180:
        print("Bu bir üçgen değildir")
        
    if kontrol2==180:
        print("Bu bir üçgendir")
        if birinciAci == ikinciAci == UcuncuAci:
            print("Bu bir eşkenar üçgendir")
        elif birinciAci == 90 and ikinciAci != 90 and UcuncuAci != 90:
            print("Bu bir dik üçgendir")
        else: 
            print("Bu bir geniş üçgendir")
    else:
        print("Bu bir üçgen değildir")
except:
    print("Lütfen tam sayı girin")


#--------------------------------------------------

#ikinci soru

print("Uzaylı renklerini girin: kırmızı, yeşil, sarı")

RenkAl= input("Rengi giriniz: ")
#RenkAl=RenkAl.lower
if RenkAl =="kırmızı" or RenkAl == "yeşil" or RenkAl=="sarı":

    if RenkAl=="yeşil":
        print("Tebrikler, yeşil uzaylıya ateşettiğiniz için 5 puan kazandınız")
    else :
        print("Tebrikler, yeşilolmayan uzaylıya ateş ettiğiniz için 10 ve üstü bir puan kazandınız")
        
    #ucuncu soru
    if RenkAl=="yeşil":
        print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
    elif RenkAl=="sarı":
        print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")
    elif RenkAl=="kırmızı":
        print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız")
else:
    print("Kırmızı, yeşil veya sarı renklerinden birini girmelisiniz")
#-----------------------------------------------------


#-------------------------------------------------------
#dördüncü soru
try:
    
        yas=int(input("Bir kişinin yaşını girin: "))
        if yas<2:
            print("Bebek")
        elif yas>=2 and yas<4:
            print("Bu kişi yeni yürümeye başlayan çocuktur")
        elif yas>=4 and yas<13:
            print("Bu kişi çocuktur")
        elif yas>=13 and yas<20:
            print("Bu kişi ergendi")
        elif yas>=20 and yas<65:
            print("Bu kişi yetişkindir")
        elif yas>=65:
            print("Bu kişi yaşlıdır")
        else:
            print("Bulunamadı")

except:
    print("Lütfen integer bir değer girin")


#------------------------------------------------
# beşinci soru
favori_meyveler=["elma","çilek","muz","domates","salatalık"]
sepet=["elma", "armut", "karpuz", "kavun", "muz", "portakal", "çilek", "vişne", "kiraz", "mandalina"]
for nesne in sepet:
    if nesne in favori_meyveler:
        print(nesne)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


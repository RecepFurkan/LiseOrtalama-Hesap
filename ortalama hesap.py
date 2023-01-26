
print("sayı girmesseniz program %100 çöker")
#############################################
#sınıftan geçme ders notu heaplayıcı kısmı##
def ysonort():
#kullanıcı değerleri#
   print("1. dönem not")
   d1=int(input())
   print("2. dönem not")
   d2=int(input())
#Hesap kısmı#
   noteort=(d1+d2)/2
   print(noteort)
   s=100-noteort
#taktir teşekkür hesap 1. döem lise
   def lis():
      print("belge durumu")
      if 70<=d1<85:
         print("1. döenem teşekkür")
      if 85<=d1:
         print("1. dönem taktir")
      else:
         print("1. dönem hiçbirşey yok")
#taktir teşekkür 2. dönem 
      if 70<=d2<85:
         print("2. dönem teşekkür")
      if 85<=d2:
         print("2. dönem taktir")
      else:
         print("2. dönem hiçbirşey yok")
   lis()


#taktir teşekkür hesap 1. döem ortokul !!!çalışmıyor!!!
   def lis():
      print("belge durumu")
      if 75<=d1<85:
         print("1. döenem teşekkür")
      if 85<=d1:
         print("1. dönem taktir")
      else:
         print("1. dönem hiçbirşey yok")
#taktir teşekkür 2. dönem ort okul
   def ort():
      if 75<=d2<85:
         print("2. dönem teşekkür")
      if 85<=d2:
         print("2. dönem taktir")
      else:
         print("2. dönem hiçbirşey yok")

#eyitim düzeyi seç
#   def snf():
#      print("sınıf düzeyi seç\norta-lise")
#     print("1     2")
#      global snf
#      snf=int(input()) #kullanıcı değeri snf#
#karar kısmı
#   if 0==snf or snf>2:
#      print("1 yada 2 sayısını girin lütfen")
#      snf()
#karar kısmı#
#  if snf==1:
#      lis()
#   else: 
#      snf==2
#      ort()

#Karar verme kısmı#
   if noteort>=50:
      print("sınıf dan geçtin")
      
      
   else:
      print("sınıf dan kaldın \n Geçmek için bu kadar puan lazım")
      print(s)
      print("  ^  ")
      sec()

#ders notu ort hesaplama kısmı#
def orthesap():
    print("kaç ders notun var 1-4")
    print("not: yazdığın kadar not gir geri kalanlarını 0 yaz")
    def P():
        global p
        p=int(input()) #not sayısı#
#karar kısmı#
        if 0==p or p>4:
          print("lütfen 0 ile 4 arasında bir sayı giriniz")
          P()
    P()

#Kullanıcı değerleri#
    print("1. YAZILI")
    a=int(input())   #1.not#
    print("2. YAZILI")
    b=int(input())   #2.not#
    print("1 sözlü")
    c=int(input())   #3.not#
    print("2. sözlü")
    d=int(input())   #4.not#
#Hesap Kısmı#
    e=(a+b+c+d)  #sayıların top#
    o=e/p
    t=(200-e)

    if p==4:
      k=4
    else:
      k=p-4

    u=t/k


    print("ortalaman")
#Karar kısmı
    if o>= 100:
     print(100)
    else:
        print(o)

    if o>=50:
        print("Dersten geçtin")

    else:
        print(" DERSTEN KALDIN \n Geçmek için gereken puan ")
        print(abs(u))

#seçim ekranı
print("ders notu-yıl sonu ort  " )
print("    1           2        ")

def sec():
   global x
   x=int(input()) #kullanıcı değeri x#
#karar kısmı
   if 0==x or x>2:
      print("1 yada 2 sayısını girin lütfen")
      sec()
sec()
#karar kısmı#
if x==1:
   orthesap()
else: 
   x==2
   ysonort()
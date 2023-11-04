import math
radyan = math.radians(36)

def hesap(n):

    toplam = 0

    for i in range(n):
        cos_taylor = ((-1) ** i) *(radyan ** (2*i)) / math.factorial(2 * i)# cos fonksiyonun taylor formülünün yazımı
        toplam = toplam + cos_taylor #her n degerinin taylor degrini toplama sürekli ekler
    return toplam #sonuc degrini dönderir


gercekDeger = math.cos(radyan)

n = 1
i=1
print("Gerçek değer",gercekDeger)


while n<3:
    deger = hesap(n)
    hata = abs(gercekDeger - deger)
    n+=1
    print( i,"terimli değer",deger)
    print(i,"terimli kesme hatası",hata)
    i+=1
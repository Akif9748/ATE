
kütüp = {}

isim = input("Adın? ")
yas = int(input("Yasın? "))

kütüp[isim] = yas

print("Kayıt başarılı:", "", "Tüm liste:", kütüp, sep="*****")
print("Yaşın:", kütüp[isim])

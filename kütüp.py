# kütüphaneyi anlatiyim

kütüp = {
    "ATE": 14,
    "MAY": 15
}


kütüp["ÖFU"] = 14

isim = input("İsmin ne? ")

if isim in kütüp:
    print("Yaşın:", kütüp[isim])
else:
    print("İsim listede yok")

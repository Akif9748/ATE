"""
Burada senden istediğim, önce ismi alacaksın, sonra yaşı alacaksın.
sonra kontrol edecek kütüphanedeki yaş ile uyuyor mu diye
tamemen pratik
"""

kütüp = {
    "ATE": 14,
    "MAY": 15
}

kütüp["ÖFU"] = 14
isim = input("İsmin ne? ")

if isim in kütüp:
    yas = int(input("Yaşın ne? "))
    yas2 = kütüp[isim]

    if yas==yas2:
        print("Hoş Geldin")
    else:
        print("Uyuşturamadık :(")    

else: 
    print("İsim listede yok")


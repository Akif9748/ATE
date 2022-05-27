# burada mesela 1den istenilen sayiya kadar sayiların karelerini yazdirt nereden

# üssü diye değişen tanımla simdi, kaçıncı dereceden üssü olacağını inputla al

sayi = int(input("Kaça kadar? "))
üs=float(input("Kaçıncı dereceden üssü? "))

for i in range (sayi):
    print(pow(i,üs))



sayi = int(input("Sayiyi gir>> "))
bol = []

for i in range(1,sayi+1):
    if sayi%i==0:
        bol.append(i)

toplam=0
for i in bol:
    toplam+=i/2
    
if toplam==sayi:
    print("Mükemmelsin.")
else:
    print("Mükemmel değilsin.")

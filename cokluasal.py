limit = int(input("> "))

asallar = []

for sayi in range(limit):
    bol=[]

    for i in range(1,sayi+1):
        if sayi%i==0:
            bol.append(i)

    if len(bol)==2:
        asallar.append(sayi)

print(asallar)
   


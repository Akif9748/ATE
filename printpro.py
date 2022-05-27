sayi =10
cumle = "ATE"

for i in range(0,sayi,2):  
    print(" " * i,cumle)   
    
for i in range(0,sayi,2):
    print(" "*  abs(sayi - i) ,cumle)

for i in range(-sayi, sayi):
    print(" "*abs(i),cumle)       
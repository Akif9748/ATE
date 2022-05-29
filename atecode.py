kilo = int(input("Kilonu gir: "))
boy = float(input("Boyunu gir: "))

if boy > 3: 
    boy /= 100

vki = kilo / boy ** 2

print("Vücüt kitle endeksiniz",vki , "'dir")

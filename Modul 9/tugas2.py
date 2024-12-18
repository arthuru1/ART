import math
# Faktorial
x = int(input("Masukkan bilangan untuk menghitung faktorial: "))
if x >= 0:
    faktorial = math.factorial(x)
    print(f"Faktorial dari {x} adalah: {faktorial}")
else:
    print("Faktorial tidak didefinisikan untuk bilangan negatif.")

# Akar kuadrat
y = float(input("Masukkan bilangan untuk menghitung akar kuadrat: "))
if y >= 0:
    akar = math.sqrt(y)
    print(f"Akar kuadrat dari {y} adalah: {akar:.2f}")
else:
    print("Bilangan negatif tidak memiliki akar kuadrat riil.")

# Pangkat
a = float(input("Masukkan bilangan basis: "))
b = float(input("Masukkan bilangan pangkat: "))
pangkat = a**b
print(f"{a} dipangkatkan ke {b} adalah: {pangkat:.2f}")

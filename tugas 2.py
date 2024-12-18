def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return ("Tidak dapat dibagi dengan nol")
    else:
        return x / y

#Angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Pilih operasi (+, -, *, /): ")

#Operasi
if operator == '+':
    hasil = tambah(angka1, angka2)
elif operator == '-':
    hasil = kurang(angka1, angka2)
elif operator == '*':
    hasil = kali(angka1, angka2)
elif operator == '/':
    hasil = bagi(angka1, angka2)
else:
    print("Operator tidak valid")

#Hasil
if isinstance(hasil, str):
    print(hasil)
else:
    print("Hasil:", hasil)
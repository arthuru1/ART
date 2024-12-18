a = int(input("Masukkan nilai a : "))
try:
    b = int(input("Masukkan nilai b : "))
    if b == 0:
        raise ZeroDivisionError
except ZeroDivisionError as e:
    print ("Kesalahan : nilai b tidak boleh 0")
else:
    c = a / b
    print ("Hasil : ", c)

class NegativeNumberError(Exception):
    pass
while True:
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        
        if a < 0 or b < 0:
            raise NegativeNumberError("Angka tidak boleh negatif!")
        hasil = a - b
        print(f"Hasil pengurangan dari {a} dan {b} adalah {hasil}")
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
    except NegativeNumberError as e:
        print(e)
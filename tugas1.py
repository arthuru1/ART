while True:
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        c = input("Masukkan operator ( +, -, *, / ): ")
        if c == '+' : 
            hasil = a + b
            print(f"Hasil penjumlahan dari {a} dan {b} adalah {hasil}")
        elif c == "-" :
            hasil = a - b
            print(f"Hasil pengurangan dari {a} dan {b} adalah {hasil}")
        elif c == "*" :
            hasil = a * b
            print(f"Hasil perkalian dari {a} dan {b} adalah {hasil}")
        elif c == "/" :
            hasil = a / b
            print(f"Hasil pembagian dari {a} dan {b} adalah {hasil}")
        break
        
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
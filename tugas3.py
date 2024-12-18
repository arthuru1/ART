data = {'nama': 'Fatchur','umur': 20,'pekerjaan': 'Mahasiswa'}
try:
    key = input("Masukkan kunci yang ingin dicari (nama, umur, pekerjaan): ")
    print(f"Nilai dari '{key}' adalah: {data[key]}")
except KeyError:
    print(f"KeyError: Kunci '{key}' tidak ditemukan dalam data.")
finally:
    print("Program selesai.")
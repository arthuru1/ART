# BUKU DALAM TIPE DATA LIST
buku1 = ["Henry Manampiring", "Filosofi Teras", "PT Kompas Media Nusantara", 2018]

# OUTPUT
print("Pengarang :", buku1[0])
print("Judul     :", buku1[1])
print("Penerbit  :", buku1[2])
print("Tahun     :", buku1[3])
print()

# MENGUBAH MENJADU 1 VARIABEL MENGGUNAKAN DICTIONARY
buku1 = {
    "pengarang": "Henry Manampiring",
    "judul": "Filosofi Teras",
    "penerbit": "PT Kompas Media Nusantara",
    "tahun": 2018
}

# OUTPUT
print("Pengarang :", buku1["pengarang"])
print("Judul     :", buku1["judul"])
print("Penerbit  :", buku1["penerbit"])
print("Tahun     :", buku1["tahun"])
print()

# Tampilkan judul buku dan pengarang dengan sebuah kalimat
print("Buku", buku1["judul"] , "ditulis oleh", buku1["pengarang"])
print()
# Tampilkan judul buku, penerbit dan tahun dengan sebuah kalimat
print("Buku", buku1["judul"] , "diterbitkan oleh", buku1["penerbit"] , "pada tahun", buku1["tahun"])
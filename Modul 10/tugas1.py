file = open("biodata.txt", "w")
file.write("Nama: Fatchur \n")
file.write("Usia: 20 tahun\n")
file.write("Alamat: Surakarta\n")
file.write("Pekerjaan: Mahasiswa\n")
file.write("Hobi: Membaca dan bermain game\n")
tambahan_data_prodi = input("Masukkan Prodi : ")
file.write(f"Prodi : {tambahan_data_prodi}\n")
tambahan_data_univ = input("Masukkan Universitas : ")
file.write(f"Universitas : {tambahan_data_univ}\n")
tambahan_data_matkul = input("Masukkan Matkul : ")
file.write(f"Mata Kuliah : {tambahan_data_matkul}\n")
print("File biodata.txt berhasil dibuat.")
print (tambahan_data_matkul[0:10])
file = open("biodata.txt", "r")
for line in file : 
    print (line.strip())
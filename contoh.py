# Menginput data pasien
nama = input("Masukkan nama pasien: ")
umur = int(input("Masukkan umur pasien: "))
kelamin = input("Masukkan jenis kelamin pasien (Laki-laki/Perempuan): ")
alamat = input("Masukkan alamat pasien: ")
nomor = int(input("Masukkan nomor telepon pasien: "))

# Menampilkan data pasien
print("----Data Pasien ------")
print(f"Nama            : {nama}")
print(f"Umur            : {umur} tahun")
print(f"Jenis Kelamin   : {kelamin}")
print(f"Alamat          : {alamat}")
print(f"Nomor Telepon   : {nomor}")
# Input Nilai
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))
tugas1 = float(input("Masukkan Nilai Tugas 1: "))
tugas2 = float(input("Masukkan Nilai Tugas 2: "))
quiz = float(input("Masukkan Nilai Quiz: "))

# Prosentase 
bobot_uts = 0.25
bobot_uas = 0.35
bobot_tugas1 = 0.20
bobot_tugas2 = 0.10
bobot_quiz = 0.10

# NILAI AKHIR
nilai_akhir = (uts * bobot_uts) + (uas * bobot_uas) + (tugas1 * bobot_tugas1) + (tugas2 * bobot_tugas2) + (quiz * bobot_quiz)

# PRINT NILAI AKHIR
print(f"Nilai akhir mahasiswa adalah: {nilai_akhir:.2f}")
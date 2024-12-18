#Modul Math
import math
r = float(input ("Masukkan jari - jari : "))
L = math.pi*(r**2)
print (f"Luas lingkaran adalah :  {L:.2f}")

#Modul Time
import time
bulan = ("Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember")
hari = ("Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Ahad",)
sekarang = time.time()
infowaktu = time.localtime(sekarang)

print ("Saat Sekarang : ")
print ("Tanggal ",infowaktu[2],bulan[infowaktu[1]-1],infowaktu[0])
print ("Hari ",hari[infowaktu[6]])
print ("Jam ", str(infowaktu[3])+":"+ str(infowaktu[4]) +":"+ str(infowaktu[5]))

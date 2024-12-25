def cekfile(nama_berkas) :
    ada = True
    try:
        f = open (nama_berkas)
    except IOError:
        ada = False
    return ada
cek = input("Input nama berkas : ")
if cekfile(cek):
    print("File ada")
else:
    print("File tidak ada")

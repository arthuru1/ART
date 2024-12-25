with open ("python1.txt", "r") as file :
    file = file.read()
print (file)
with open ("python1.txt", "w") as file :   
    file.write ("Operasi file dengan with\n")
    file.write("Alhamudillah, selesai")
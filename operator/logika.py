print("Operasi AND")
print("True and True \t:", True and True)
print("True and False \t:", True and False)
print("False and True \t:", False and True)
print("False and False\t:", False and False)

print("\nOperasi OR")
print("True or True \t:", True or True)
print("True or False \t:", True or False)
print("False or True \t:", False or True)
print("False or False \t:", False or False)

print("\nOperasi NOT")
print("not True \t:", not True)
print("not False \t:", not False)

#operator logika
# not and or

#Operator NOT
nilai1 = True
hasil = not nilai1
print("==============NOT============")
print("Data Nilai 1", nilai1)
print("Hasil Operator NOT", hasil)

#Operator AND
#Ketika keduanya True maka True selain dari itu False
nilai1 = True
nilai2 = True
hasil = nilai1 and nilai2
print("==============AND============")
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator AND", hasil)
nilai1 = True
nilai2 = False
hasil = nilai1 and nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator AND", hasil)
nilai1 = False
nilai2 = True
hasil = nilai1 and nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator AND", hasil)
nilai1 = False
nilai2 = False
hasil = nilai1 and nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator AND", hasil)


#Operator OR
#Ketika nilainya ada yang True maka hasilnya True
nilai1 = True
nilai2 = True
hasil = nilai1 or nilai2
print("==============OR============")
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator OR", hasil)
nilai1 = True
nilai2 = False
hasil = nilai1 or nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator OR", hasil)
nilai1 = False
nilai2 = True
hasil = nilai1 or nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator OR", hasil)
nilai1 = False
nilai2 = False
hasil = nilai1 or nilai2
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Hasil Operator OR", hasil)

#Operator AND 3 perbandingan
#Ketika keduanya atau lebih  True maka True selain dari itu False
nilai1 = True
nilai2 = True
nilai3 = False
hasil = nilai1 and nilai2
print("==============AND 3 Perbandingan============")
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Data Nilai 3", nilai3)
print("Hasil Operator AND", hasil)

#Operator OR 3 perbandingan
#Ketika nilainya ada yang True maka hasilnya True
nilai1 = True
nilai2 = True
nilai3 = False
hasil = nilai1 or nilai2
print("==============OR 3 Perbandingan============")
print("Data Nilai 1", nilai1)
print("Data Nilai 2", nilai2)
print("Data Nilai 3", nilai3)
print("Hasil Operator OR", hasil)
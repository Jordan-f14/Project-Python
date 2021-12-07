#contoh menentukan bil prima
print("============Bilangan Prima===========")
angka_awal = int(input('Masukan angka awal: '))
angka_akhir = int(input('Masukan angka akhir: '))
 
list_angka = [i for i in range(angka_awal, angka_akhir +1 )]
 
bilangan_prima = []
for i in list_angka:
    if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
        bilangan_prima.append(i)
 
print(bilangan_prima)

#contoh menentukan umur
print("============Umur===========")
umur = input("masukan umur: ")
if int(umur) < 45:
    keterangan = 'masih muda'
else: 
    keterangan = 'sudah tua'
 
print('anda memasukan umur {}, artinya {}'.format(umur, keterangan))

print("===========Kalkulator===========")
def tambah(x, y):
    return x + y
 
def kurang(x, y):
    return x - y
 
def kali(x, y):
    return x * y
 
def bagi(x, y):
    return x / y
 
 
print('Menu operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian')
 
operasi = int(input('silahkan masukan operasi pilihan (dalam angka): '))
x = int(input('masukan angka pertama: '))
y = int(input('masukan angka ke dua: '))
 
if operasi == 1:
    print(tambah(x, y))
elif operasi == 2:
    print(kurang(x, y))
elif operasi == 3:
    print(kali(x, y))
elif operasi == 4:
    print(bagi(x, y))

print("============Nilai===========")
print("81 – 100 : nilai A")
print("61 – 80  : nilai B")
print("41 – 60  : nilai C")
print("21 – 40  : nilai D")
print(" 0 – 20   : nilai E")
nilai = int(input('masukan nilai dalam angka 1-100: '))
 
hasil = None
if nilai <= 100 and nilai > 80:
    hasil = 'A'
elif nilai <= 80 and nilai > 60:
    hasil = 'B'
elif nilai <= 60 and nilai > 40:
    hasil = 'C'
elif nilai <= 40 and nilai > 20:
    hasil = 'D'
elif nilai <=20 and nilai >= 0:
    hasil = 'E'
else:
    print('inputan salah')
 
print('Nilai {} =  {}'.format(nilai, hasil))

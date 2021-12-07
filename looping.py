a = int(input("masukkan jumlah anak ayam: "))
print("tek kotek kotek kotek")
if a>=2:
     while a>1:
         print("anak ayam turun %d mati 1 tinggal %d"%(a,a-1))
         a = a - 1
         if a<=1:
            print("anak ayam turun %d mati 1 tinggal induknya"%(a))
else:
    print(",anak ayam turun berkotek, anak ayam turunlah %d ,mati 1 tinggalah induknya"%(a))

string = ""

x = int(input("Masukkan angka :"))
bar = x
# Looping Baris
while bar >= 0:
	# Looping Kolom Spasi Kosong
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri < (x - (bar-1)):
		string = string + " $ "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " $ "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
	
print (string)

n = int(input("Masukan Bilangan/karakter : "))
#Lakukan perulangan nested for untuk menghasilkan pola siku-siku 
for i in range(0, n):
    for j in range(0, i + 1):
        print(' * ', end='')
    print('')

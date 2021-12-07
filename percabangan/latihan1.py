#input
nama=input("Nama Pembeli : ")
kd_baju=input("Masukkan Kode Baju [SP/AD] :")
ukuran=input("Masukka Ukuran [S/M] :")

#proses
if kd_baju == "SP" or kd_baju == "sp": 
    merk="SuperDry"
    if ukuran == 'S' or ukuran == 's':
        harga=65000
    elif ukuran == 'M' or ukuran == 'm':
        harga=70000
    else:
        harga =0
elif kd_baju == "AD" or kd_baju == "ad":
    merk="Adidas"
    if ukuran == 'S' or ukuran == 's':
        harga=75000
    elif ukuran == 'M' or ukuran == 'm':
        harga=80000
    else:
        harga=0
else:
    merk = "Kode Salah"
    harga = 0
#output
print("=========================================")
print("\tData Baju")
print("=========================================")
print("Nama Pembeli : ",nama)
print("Merk Baju    : ",merk)
print("Harga Baju   : ",harga)
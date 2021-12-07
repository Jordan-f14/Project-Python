print("===========Menghitung Gaji Salesman==========")
BanyakProduk = int(input("Banyak Produk ="))
HargaSatuan = int(input("Harga Satuan ="))
GajiPokok = 5000000
omsetlebih = 20/100 * GajiPokok
omsetkurang = 10/100 * GajiPokok

if BanyakProduk > 100 :
    TotalJual = (BanyakProduk * HargaSatuan)
    TotalGaji = ((GajiPokok + omsetlebih) + TotalJual)
    print("Total Gaji Pegawai adalah", TotalGaji)

elif BanyakProduk < 100 :
    TotalJual = (BanyakProduk * HargaSatuan)
    TotalGaji = ((GajiPokok + omsetkurang) + TotalJual)
    print("Total Gaji Pegawai adalah", TotalGaji)


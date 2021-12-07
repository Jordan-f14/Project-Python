print("              COFFEE SHOP HITS       ")
print("          Jalan Palmerah Barat No.12      ")
print("                 JAKARTA BARAT      ")

print("="*42)
nama = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")

# membuat daftar menu
print("\n                -MENU-              ")
print("1. Cappuccino                   Rp 18.000")
print("2. Vanilla latte                Rp 18.000")
print("3. Americano                    Rp 20.000")
print("4. Espresso                     Rp 15.000")
print("5. Macchiato                    Rp 15.000")
print("="*42)


menu_pembelian = int(input("Nomor Menu : "))

if menu_pembelian == 1:
    harga = 18000
elif menu_pembelian == 2:
    harga = 18000
elif menu_pembelian == 3:
    harga = 20000
elif menu_pembelian == 4:
    harga = 15000
elif menu_pembelian == 5:
    harga = 15000
else:
    while True:
        print("Menu Tidak Tersedia, Silahkan Pilih Menu Lain!!")
        menu_pembelian = int(input("Nomor Menu : "))
        if menu_pembelian == 1 or menu_pembelian == 2 or menu_pembelian == 3 or menu_pembelian == 4 or menu_pembelian == 5:
            if menu_pembelian == 1:
                harga = 18000
            elif menu_pembelian == 2:
                harga = 18000
            elif menu_pembelian == 3:
                harga = 20000
            elif menu_pembelian == 4:
                harga = 15000
            elif menu_pembelian == 5:
                harga = 15000
            break


jumlah_pembelian = int(input("Jumlah Pembelian : "))
bayar = jumlah_pembelian * harga
pajak = bayar * 0.1
total_bayar = bayar + pajak
print("="*42)
print("Subtotal   : \t\t\tRp ",bayar)
print("Pajak 10 % : \t\t\tRp ", pajak)

print("\nTotal : \t\t\tRp {}".format(total_bayar))
tunai = int(input("Tunai : \t\t\tRp "))
uangkembali = tunai - total_bayar
print("="*42)
print("Uang Kembali : \t\t\tRp {}".format(uangkembali))
print("Terima Kasih - Silahkan datang lagi!")

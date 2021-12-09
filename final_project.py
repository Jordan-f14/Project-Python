# Kop struk berisi nama usaha, alamat, dan lainnya
print("="*48)
print("               COFFEE SHOP HITS                  ")
print("       Jalan Kemanggisan Utama Raya No.12        ")
print("             Palmerah Jakarta Barat              ")
print("               Telp. 021-22126300                ") # fungsi print digunakan untuk mencetak agar ditampilkan pada output
print("="*48)

# Untuk memanggil operasi yang berhubungan dengan waktu disini menggunakan salah satu modul yang ada yaitu datetime
from datetime import datetime
saat_ini = datetime.now()
tgl_jam = saat_ini.strftime("%d %b %y\t\t\t\t%H:%M:%S") # format dd/mm/yyyy dan h/m/s
print(tgl_jam)

# Fungsi input digunakan untuk menginput nama pelanggan dan nomer pesanan
pesanan = input("[Dine In/Take Away] : ")
input("Nama Pelanggan : ")
nomer = input("Nomer Pesanan : ")

# Membuat daftar menu menggunakan def agar nantinya dapat kita panggil kembali 
def menu():
    print("\n                  - OUR MENU -             ")
    print("-"*48)
    print("| Kode |       Drinks       |       Harga      |")
    print("-"*48)
    print("| 1    | Cappuccino         |     Rp 18.000    |")
    print("| 2    | Vanilla Latte      |     Rp 18.000    |")
    print("| 3    | Americano          |     Rp 20.000    |")
    print("| 4    | Expresso           |     Rp 15.000    |")
    print("| 5    | Macchiato          |     Rp 15.000    |")
    print("|      |--------------------|                  |")
    print("|      |       Snacks       |                  |")
    print("|      |--------------------|                  |")
    print("| 6    | Sandwich           |     Rp 15.000    |")
    print("| 7    | Cinnamon Roll      |     Rp 20.000    |")
    print("| 8    | Coffee Bun         |     Rp 13.000    |")
    print("| 9    | French Fries       |     Rp 15.000    |")
    print("| 10   | Spaghetti          |     Rp 20.000    |")
    print("-"*48)
menu()

# Daftar variabel
jumlah_beli = int(input("Jumlah Pesanan : "))
kode_menu = []
nama_menu = []
masukan_jumlah = []
total_pesanan = []
uang_kembali = []
harga = []
jumlah = []

# Input
i = 0
while i < jumlah_beli:
    print("Menu Ke -", i+1)
    kode_menu.append(input("Masukan Kode Menu : "))
    masukan_jumlah.append(int(input("Total Item : ")))
    if kode_menu[i] == "1":
        nama_menu.append("Cappucino")
        harga.append("18.000")
        jumlah.append(masukan_jumlah[i]*int(18000))
    elif kode_menu[i] == "2":
        nama_menu.append("Vanilla Latte")
        harga.append("18.000")
        jumlah.append(masukan_jumlah[i]*int(18000))
    elif kode_menu[i] == "3":
        nama_menu.append("Americano")
        harga.append("20.000")
        jumlah.append(masukan_jumlah[i]*int(20000))
    elif kode_menu[i] == "4":
        nama_menu.append("Espresso")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    elif kode_menu[i] == "5":
        nama_menu.append("Macchiato")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    elif kode_menu[i] == "6":
        nama_menu.append("Sandwich")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    elif kode_menu[i] == "7":
        nama_menu.append("Cinnamon Roll")
        harga.append("20.000")
        jumlah.append(masukan_jumlah[i]*int(20000))
    elif kode_menu[i] == "8":
        nama_menu.append("Coffee Bun")
        harga.append("13.000")
        jumlah.append(masukan_jumlah[i]*int(13000))
    elif kode_menu[i] == "9":
        nama_menu.append("French Fries")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    elif kode_menu[i] == "10":
        nama_menu.append("Spaghetti")
        harga.append("20.000")
        jumlah.append(masukan_jumlah[i]*int(20000))
    else :
        nama_menu.append("Menu Tidak Tersedia Silahkan Pilih Menu Lain")
        harga.append("0")
        jumlah.append(masukan_jumlah[i]*int("0"))
    i = i+1

print("-"*48)
print("COFFEE SHOP HITS", pesanan, "No.", nomer)
print("-"*48)
print("ITEM & TOTAL")

# Proses
total_pesanan = 0
a = 0
while a < jumlah_beli:
    total_pesanan = total_pesanan +jumlah[a]
    print ("   %i\t%s\t\t\t: %i"%(masukan_jumlah[a], nama_menu[a], jumlah[a]))
    a += 1

# Output
print("-"*48)
print("\t        Subtotal : \t\tRp",total_pesanan)
pajak = total_pesanan * 0.1
total_bayar = total_pesanan + pajak
print("\t        Pajak 10 % : \t\tRp",int(pajak))
print("\t        Total : \t\tRp",int(total_bayar))
bayar = int(input("\t        Tunai : \t\tRp "))
uang_kembali = bayar - total_bayar
print("\t        Uang Kembali : \t\tRp",int(uang_kembali))
print("="*48)
print("\n\t\t  Terima Kasih")
print("\t      Silahkan datang lagi!~")
print("\n================================================")
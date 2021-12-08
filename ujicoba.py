print("              COFFEE SHOP HITS       ")
print("          Jalan Palmerah Barat No.12      ")
print("               JAKARTA BARAT      ")

print("="*42)
nama = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")

# membuat daftar menu
def menu():
    print("\n                -MENU-              ")
    print("Kode Menu |    Nama Menu     |   Harga")
    print("C         |  Cappuccino      | Rp 18.000")
    print("V         |  Vanilla Latte   | Rp 18.000")
    print("A         |  Americano       | Rp 20.000")
    print("E         |  Expresso        | Rp 15.000")
    print("M         |  Macchiato       | Rp 15.000")
    print("="*42)
menu()

jumlah_beli = int(input("Masukan Jumlah Pesanan: "))
kode_menu =[]
nama_menu= []
masukan_jumlah =[]
total_pesanan =[]
uang_kembali =[]
harga =[]
jumlah =[]

i = 0
while i < jumlah_beli:
    print("Menu Ke -", i+1)
    kode_menu.append(input("Masukan Kode Menu : "))
    masukan_jumlah.append(int(input("Masukan Jumlah Pesanan: ")))
    if kode_menu[i] == "C" or kode_menu [i] == "c":
        nama_menu.append("Cappucino")
        harga.append("18.000")
        jumlah.append(masukan_jumlah[i]*int(18000))
    elif kode_menu[i] == "V" or kode_menu [i] == "v":
        nama_menu.append("Vanilla Latte")
        harga.append("18.000")
        jumlah.append(masukan_jumlah[i]*int(18000))
    elif kode_menu[i] == "A" or kode_menu [i] == "a":
        nama_menu.append("Americano")
        harga.append("20.000")
        jumlah.append(masukan_jumlah[i]*int(20000))
    elif kode_menu[i] == "E" or kode_menu [i] == "e":
        nama_menu.append("Espresso")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    elif kode_menu[i] == "M" or kode_menu [i] == "m":
        nama_menu.append("Macchiato")
        harga.append("15.000")
        jumlah.append(masukan_jumlah[i]*int(15000))
    else :
        nama_menu.append("Menu Salah")
        harga.append("0")
        jumlah.append(masukan_jumlah[i]*int("0"))
    i = i+1


print("\nCOFFEE SHOP HITS".center(60, ' '))
print("="*60)
print("No   |     Menu     |    Harga    |   Jumlah   |   Subtotal")
print("="*60)

#proses bayar

total_pesanan = 0
a = 0
while a < jumlah_beli:
    total_pesanan = total_pesanan +jumlah[a]
    print (" %i      %s       %s          %i          %i"%(a+1, nama_menu[a], harga[a], masukan_jumlah[a], jumlah[a]))
    a += 1

print("-"*60)
print("\t\t\t\t\tTotal : ",total_pesanan)
bayar = int(input("\t\t\t\t\tTunai :  "))
uang_kembali = bayar - total_pesanan
print("\t\t\t\t Uang Kembali : ", uang_kembali)
print("\t~Terima Kasih - Silahkan datang lagi!~")
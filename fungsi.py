def garis():
    print("="*40)

def kuliah():
    print("BSI Slipi")

def sapa(nama,kabar="Baik",usia=25):
    print("Hi " +nama+ " Apa kabar? " +kabar)
    print("Kuliah dimana? ")
    kuliah()
    print("Berapa usianya? " ,str(usia))

# garis()
# sapa(nama="Jordan")
# garis()
# sapa(nama="Dendi",kabar="Tidak baik", usia="17")

def print_ulang(nilai, *vartuple):
    print("Outputnya adalah: ")
    print(nilai)
    for var in vartuple:
        print(var)


print_ulang(12)
garis()
print_ulang(12,14, 20,15)

print("="*40)
def sum ( arg1, arg2 ):
    total = arg1 + arg2;
    print("Di dalam fungsi nilai total : ", total)
    return total

# sum(10, 20 )
# print("Di luar fungsi, nilai total : ", total )
datalist = [3,5,7,2,4,9,8,4]
print(datalist[2:5]) 
#Memotong anggota list dari index ke 2 sampai anggota ke 5
print(datalist[:5])
#Memotong anggota list dari index ke 0 sampai anggota ke 5
print(datalist[3:]) 
#Memotong anggota list dari index ke 3 sampai anggota list terakhir
datalist2= ["Saya","Suka","Programming"]
datalist3= datalist2 * 2
print(datalist3)

# Mengurutkan Anggota List
print("="*30)
abjad=["d","e","a","b","g"]
print(datalist)
datalist.sort() #mengurutkan datalist dari kecil ke besar
print(datalist)
abjad.sort()
print(abjad)
datalist.reverse()
print(datalist)
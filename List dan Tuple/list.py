elektronik = ["Televisi","Rice Cooker","Handphone"]
elektronik.insert(1,"Laptop") # Menambahkan item Laptop sesuai dengan index ke 1
print(elektronik)
print("="*30)
elektronik.append("Kulkas") # Menambahkan Item Kulkas di akhir list
print(elektronik)
print("="*30)
del elektronik[3] # Menghapus item di index ke 3
print(elektronik)
print("="*30)
elektronik.remove("Televisi") # Menghapus item dengan paramater Televisi
print(elektronik)
print("="*30)

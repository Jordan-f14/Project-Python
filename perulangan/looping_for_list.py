#For sederhana dengan list
elektronik=["Televisi","Rice Cooker","Handphone","Laptop","Kulkas","Speaker"]
cari=input("Elektronik yang di cari : ")
for i, data in enumerate(elektronik):
    if data.lower == cari.lower:
        print(i,"Elektronik yang di cari pada index :", i)
        break
    else:
        print("Data Elektronik tidak ada")


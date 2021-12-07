def InsertionSort(val):
    for index in range(1,len(val)):
        a = val[index]
        b = index
    while b>0 and val[b-1]>a:
        val[b]=val[b-1]
        b = b-1
    val[b]=a
Angka = [22,10,15,3,8,2]
InsertionSort(Angka)
print(Angka)

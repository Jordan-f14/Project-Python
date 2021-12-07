nilai_tugas=[70,80,90,"Keterangan Lulus"]
print("Nilai Tugas: \n",nilai_tugas)

array=[["Teknik","Kedokteran","MIPA"],[1,2,3]]
print(array)

matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4):
    for j in range(4):
        if i==j:
            matriks[i][j]=1
        if i<j:
            matriks[i][j]=3
        if i>j:
            matriks[i][j]=0

for i in range(4): 
    print(matriks[i])

nilai = [1, 2, 3, 4 ]
for i in range(len(nilai)): 
    nilai[i]=2*i+1 
    print(nilai[i])
print("================Matriks Penjumlahan===============")
MatA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
MatB = [
    [3, 3, 4],
    [1, 0, 5],
    [9, 3, 2],
]
for x in range(0, len(MatA)):
    for y in range(0, len(MatA[0])):
        print (MatA[x][y] + MatB[x][y], end=' '),
    print ()

print("================Matriks Pengurangan===============")
MatA = [
    [3, 2, 3],
    [0, 6, 5],
    [9, 0, 3],
]
MatB = [
    [3, 3, 4],
    [1, 0, 5],
    [9, 3, 2],
]
for x in range(0, len(MatA)):
    for y in range(0, len(MatA[0])):
        print (MatA[x][y] - MatB[x][y], end=' '),
    print ()
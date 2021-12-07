GajiPokok = int(input("Gaji Pokok ="))
JamKerja = int(input("Jam Kerja ="))
JamNormal = 200
Tunjangan = 20/100 * GajiPokok
Pajak = 10/100 * GajiPokok
UangLembur = 20000

if JamKerja > 200 :
    TotalLembur = ((JamKerja - JamNormal) * UangLembur)
    TotalGaji = ((GajiPokok + Tunjangan + TotalLembur) - Pajak)
    print("Total Gaji Pegawai adalah", TotalGaji)

elif JamKerja == 200 :
    TotalGaji = ((GajiPokok + Tunjangan) - Pajak)
    print("Total Gaji Pegawai adalah", TotalGaji)

else :
    TotalGaji = (GajiPokok + Tunjangan)
    print("Total Gaji Pegawai adalah", TotalGaji)

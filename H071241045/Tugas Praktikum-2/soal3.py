nilai_akhir = int(input("Masukkan nilai akhir: "))
if nilai_akhir > 100:
    predikat = "tidak valid"
elif nilai_akhir < 0:
    predikat = "tidak valid"
else:
    persentase_kehadiran = int(input("Masukkan persentase kehadiran: "))
    if 85 <= nilai_akhir <= 100 and persentase_kehadiran >= 75:
        predikat = "Lulus dengan predikat A"
    elif 70 <= nilai_akhir <= 84 and persentase_kehadiran >= 75:
        predikat = "Lulus dengan predikat B"
    elif 60 <= nilai_akhir <= 69 and persentase_kehadiran >= 75:
        predikat = "Lulus dengan predikat C"
    else:
        predikat = "Tidak lulus"

print("Lulus dengan predikat:", predikat)

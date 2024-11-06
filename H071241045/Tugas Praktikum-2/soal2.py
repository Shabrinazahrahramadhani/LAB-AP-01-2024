usia = int(input("masukkan usia : "))
if usia <= 0 :
    print("inputan tidak valid")
elif usia < 5 :
    harga_tiket = 0

    print(f"harga tiket : Rp. {int(harga_tiket)}")
else :
    status = input("apakah anda anggota (ya/tidak): ")
    if usia <= 12 :
        harga_tiket = 50000
    elif usia <= 59 :
        harga_tiket = 10000
    else :
        harga_tiket = 70000
    hasil = harga_tiket - ((harga_tiket*20) / 100) if status == "ya" else harga_tiket
    print(f"harga tiket: Rp. {int(hasil)}")
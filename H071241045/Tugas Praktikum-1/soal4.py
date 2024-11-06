total_harga = int(input("masukkan total harga :"))
uang_diberikan = int(input("masukkan uang yang diberikan :"))
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang_diberikan - total_harga
if total_harga > uang_diberikan: 
    print("uang anda kurang")
    exit()
for pecahan in pecahan_uang :
    jumlah_lembar = kembalian // pecahan 
    if jumlah_lembar > 0 :
        print(f"{jumlah_lembar} lembar Rp. {pecahan: }")
        kembalian %= pecahan    
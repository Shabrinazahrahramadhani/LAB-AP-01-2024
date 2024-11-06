pengguna_data = int(input("masukkan jumlah data yang digunakan (GB) : "))
waktu_penggunaan = input("apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? : ")
jenis_penggunaan = input("apakah anda pengguna personal atau bisnis? : ")

if  pengguna_data < 10 and waktu_penggunaan == 'off peak' and jenis_penggunaan == 'personal' :
    paket = "paket A"
elif pengguna_data >= 10 and pengguna_data <=50 and waktu_penggunaan == "peak" and jenis_penggunaan == "personal" :
    paket = "paket B"
elif pengguna_data > 50 and waktu_penggunaan == "peak" and jenis_penggunaan == "personal" or "bisnis" :
    paket = "paket C"
elif pengguna_data > 50 and waktu_penggunaan == "off-peak" and jenis_penggunaan == "bisnis" :
    paket = "paket D"

else :
    paket = "tidak ada paket yang cocok"
print(f"paket yang sesuai adalah : {paket}")     
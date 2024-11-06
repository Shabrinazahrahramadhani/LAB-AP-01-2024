
import random

angka_rahasia = random.randint(1, 100)
percobaan = 5

for i in range(percobaan):
    try:
        tebakan = int(input("Masukkan tebakan anda (0 untuk berhenti): "))
    except ValueError:
        print("Input harus angka")
        continue

    if tebakan == 0:
        print("permainan dihentikan.")
        break

    if tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")

if tebakan != angka_rahasia:
    print(f"Maaf, kesempatan habis. Angka rahasia adalah {angka_rahasia}.")
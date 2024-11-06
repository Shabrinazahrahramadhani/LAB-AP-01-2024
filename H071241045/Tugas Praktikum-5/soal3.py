# def jumlah_minimum_penghapusan_karakter(s1, s2):
#     count1 = Counter(s1)
#     count2 = Counter(s2)

#     penghapusan = sum((count1 - count2).values()) + sum((count2 - count1).values())

#     print(penghapusan)

# jumlah_minimum_penghapusan_karakter('bacdc', 'dcbac')
# jumlah_minimum_penghapusan_karakter('bacdc', 'dcbad')

def hitung_frekuensi(s):
    frekuensi = {}
    for char in s:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    return frekuensi

def hitung_minimum_penghapusan(s1, s2):
    frek_s1 = hitung_frekuensi(s1)
    frek_s2 = hitung_frekuensi(s2)
    
    total_penghapusan = 0
    
    # Hitung selisih frekuensi dari s1
    for char in frek_s1:
        if char in frek_s2:
            total_penghapusan += abs(frek_s1[char] - frek_s2[char])
        else:
            total_penghapusan += frek_s1[char]
    
    # Hitung selisih frekuensi dari s2 untuk karakter yang tidak ada di s1
    for char in frek_s2:
        if char not in frek_s1:
            total_penghapusan += frek_s2[char]
    
    return total_penghapusan

# Contoh penggunaan
s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

hasil = hitung_minimum_penghapusan(s1, s2)
print(f"Jumlah minimum penghapusan karakter untuk membuat kedua string menjadi anagram: {hasil}")
n = int(input("N : "))
m = int(input("M : "))

if n < 0:
    n = -n
    arah_baris = -1
else:
    arah_baris = 1
if m < 0:
    m = -m 
    arah_kolom = -1
else:
    arah_kolom = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(f"MOVE to ({i*arah_baris}, {j*arah_kolom})")
    else:
        for j in range(m -1, -1, -1):
            print(f"MOVE to ({i*arah_baris}, {j*arah_kolom})")
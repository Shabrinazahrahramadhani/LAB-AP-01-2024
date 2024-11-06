print("selamat datang di kalkulator sederhana!")

def kalkulator():
    if operasi == '+' :
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        if b != 0:
            return a / b
        else:
            print("Pembagian dengan nol tidak diperbolehkan")
            return None
    
    else:
        print("Operasi tidak valid")
        return None
    
try:

    a = int(input("angka pertama: "))
    b = int(input("angka kedua: "))
except ValueError :
    print("Input tidak valid: could not convert string to float: 'a' " )
    exit()

operasi = input("operasi (+, -, *, /): ")  

hasil = kalkulator()

print(f"hasil: {hasil}")

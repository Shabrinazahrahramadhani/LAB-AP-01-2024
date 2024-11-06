import re
def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z]+[0-9]*@[a-z]+\.(com|co\.id)$"
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.[a-z])(?=[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(pattern, password)


username = input("masukkan username: ")

if is_valid_username(username):
    email = input("masukkan email: ")

    if is_valid_email(email):
        password = input("masukkan password: ")

        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Halo {username}")
        else:
            print(f"\nPassword yang kamu input beresiko dihack. Registrasi gagal.")

    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal.")

else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal")

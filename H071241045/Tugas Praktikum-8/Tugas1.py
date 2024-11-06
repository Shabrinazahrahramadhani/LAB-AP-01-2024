import re

def valid_string(s):
    if len(s) != 45:
        return False
    
    pattern = r"^[A-Za-z02468\s]{40}$"
    if not re.match(pattern, s[:40]):
        return "40 karakter pertama harus terdiri dari huruf atau digit genap"
    
    pattern = r"^[13579\s]{5}$"
    if not re.match(pattern, s[40:]):
        return "5 karakter terakhir harus terdiri dari digit ganjil atau whitespace"
    
    return True

user_input = input("masukkan string: ")
result = valid_string(user_input)
print(result)
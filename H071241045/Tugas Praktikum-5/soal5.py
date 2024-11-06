# def caesar_cipher(text, shift):
#     encryted = []
#     for char in s:
#         if char.isalpha():
#             offset = 65 if char.isupper() else 97
#             encryted.append(chr((ord(char) - offset + shift) % 26 + offset))
#         else:
#             encryted.append(char)

#     print(''.join(encryted))

# caesar_cipher('abcd', 4)
# caesar_cipher('abcd!23$', 3)

def caesar_cipher(text, shift):
    result = "" 
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

print(f"Text : {text}")
print(f"Shift: {shift}")
print(f"Cipher: {caesar_cipher(text, shift)}")
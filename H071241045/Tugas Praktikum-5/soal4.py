def substring(s):
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            print(s[i:i+length])

text = input('input your string: ')
print('====================')
substring(text)
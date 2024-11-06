def palindrome (s):
    s = s.lower()
    if s == s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
palindrome('ibu ratna antar ubi')
palindrome('sistem informasi 2024')
palindrome('negara kesatuan republik indonesia')
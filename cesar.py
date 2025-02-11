#crypt.py
def crypt():
    key = int(input('Enter your key: '))
    inp = input("Enter a word you would like to crypt: ")
    crypted = []
    for char in inp:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
        else:
            new_char = char
        crypted.append(new_char)
    return ''.join(crypted)
print(crypt())
#decrypt.py
def decrypt():
    key = int(input('Enter your key: '))
    inp = input("Enter a word to decrypt: ")
    decrypted = []
    for char in inp:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - key) % 26 + base)
        else:
            new_char = char
        decrypted.append(new_char)
    return ''.join(decrypted)
print(decrypt())
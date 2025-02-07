#crypt.py
def crypt():
    key = int(input('Enter your key: '))
    inp = input("Enter a world would you like to crypt: ")
    crypted = []
    for i in range(len(inp)):
        crypted.append(ord(inp[i]) + key)
    return crypted
print(crypt())
#decrypt.py
def decrypt():
    key = int(input('Enter your key: '))
    inp = input("Enter a numbers with comma: ")
    crypted = []
    for i in inp.split(','):
        crypted.append(int(i))
    decrypted = ''
    for i in range(len(crypted)):
        decrypted += chr(crypted[i] - key)
    return decrypted
print(decrypt())
#crypt.py
def crypt():
    inp = input("Enter a world would you like to crypt: ")
    crypted = []
    for i in range(len(inp)):
        crypted.append(ord(inp[i]))
    return crypted
print(crypt())
#decrypt.py
def decrypt():
    inp = input("Enter a numbers with comma: ")
    crypted = []
    for i in inp.split(','):
        crypted.append(int(i))
    decrypted = ''
    for i in range(len(crypted)):
        decrypted += chr(crypted[i])
    return decrypted
print(decrypt())
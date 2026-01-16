import os

def Decryption(ciphertext, key):
    key = key %256
    decrypt_text = []
    for char in ciphertext:
        decrypted_value = (ord(char) - key) % 256
        decrypt_text.append(chr(decrypted_value))
    return "".join(decrypt_text)

file = 'ciphertext.txt'

if not os.path.exists(file):
    print("File not exsits.")
    exit()
try:
    with open(file, 'r') as f:
        ciphertext= f.read()
except Exception as e:
    print("An error occured", e)
    exit()


if not ciphertext:
    print("Cipher text file is empty...")
    exit()
else:
    print("Cipher Text Loaded Successfully...")

input_key = input("Enter the key for decryption (integer): ")
key = int(input_key)
plaintext = Decryption(ciphertext, key)
print("Plain Text Created Successfully")
with open('decryptedtext.txt', 'w') as f:
    f.write(plaintext)
print("Decrypted file created successfully as 'decryptedtext.txt'")
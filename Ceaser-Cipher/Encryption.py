import os

def ceaser_encryption(text, key):
    cipher = []
    key = key % 256
    for char in text: 
        cipher_text =  ((ord(char) + key)) % 256
        cipher.append(chr(cipher_text))
    return "".join(cipher)

file = 'plaintext.txt'

if not os.path.exists(file):
    print("The file doesn't exists")
    exit()
try:
    with open(file, 'r') as f:
        text = f.read()
except Exception as e:
    print("An error occered",e )
    exit()

if not text:
    print("the file is empty...")
    exit()

print("Plain Text Loaded Successfully...")
input_key = input("Enter the key for encryption (integer): ")
key = int(input_key)

ciphertext = ceaser_encryption(text, key)
print("Cipher Text Created Successfully")

with open('ciphertext.txt', 'w') as f:
    f.write(ciphertext)
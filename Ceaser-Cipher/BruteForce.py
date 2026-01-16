# Asking the user for every key value
import os

def bruteforce2(cipher_text):

    for key in range(0,255):
        text = []
        for char in cipher_text:
            decrypt_value  = (ord(char) - key) % 256
            actualtext = chr(decrypt_value)
            text.append(actualtext)
            s = "".join(text)
    

        print(s)
        option = str(input("is this a correct word?(y/n): "))
        if option == 'y':
            print("Key: ", key)
            break
        



file_path = './ciphertext.txt'
with open(file_path, 'r') as f:
    cipher_text = f.read()



bruteforce2(cipher_text)


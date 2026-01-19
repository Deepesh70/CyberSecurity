## without human intervention match the string with dictionary , should be > 70% matching

import nltk

from nltk.corpus import words

dictionary = set()

for w in words.words():
    dictionary.add(w.lower())

def bruteforce3(cipher_text):

    for key in range(256):
        text = []
        for char in cipher_text:
            decrypt_value = (ord(char) - key) % 256
            decrypt_text = chr(decrypt_value)
            text.append(decrypt_text)
        s = "".join(text)
        # print(s)
        words_found = s.split()
           
        if not words_found:
            continue
    
        count = 0
        for word in words_found:
            clean_word = word.strip(".,?!:;\"'()[]{}").lower()
            if clean_word in dictionary:
                count = count + 1
    
        percent = count/len(words_found)
        if percent > 0.7:
            return key,percent,s
        # print(s)
    return None, 0, None

path = './ciphertext.txt'

with open(path, 'r') as f:
    cipher_text = f.read()

r = bruteforce3(cipher_text)
if r[0] is not None:
    print("Key: ", r[0])
    print(r[2])
    print("Percentage mtched: ",r[1]*100)
else:
    print("Percent matching: ", r[1]*100)
    print("Key Not found")
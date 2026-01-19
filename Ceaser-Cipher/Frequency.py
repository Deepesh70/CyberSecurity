import nltk
from nltk.corpus import words
from collections import Counter
# nltk.download('words')

dictionary = set()
for w in words.words():
    dictionary.add(w.lower())


def frequency_analysis(cipher_text):
    frequency = Counter(cipher_text).most_common()
    return frequency



def frequency_based_decryption(cipher_text):
    for char in most_common:
        for key in range(256):
            text = []
            for c in cipher_text:
                decrypt_value = (ord(c) - key) % 256
                decrypt_text = chr(decrypt_value)
                text.append(decrypt_text)
            s = "".join(text)
            words = s.split()
            if not words:
                continue
            count = 0
            for word in words:
                clean_word = word.strip(".,?!:;\"'()[]{}").lower()
                if clean_word in dictionary:
                    count = count + 1
            
            percent = count / len(words)
            if percent > 0.5:
                return key, percent, s
        
        return None, 0, None
          

path = './ciphertext.txt' 
with open(path, 'r') as f:
    cipher_text = f.read()

s = frequency_analysis(cipher_text)
print(s)
most_common = [' ', 'e', 't', 'a', 'o', 'i']
    

result = frequency_based_decryption(cipher_text)
if result[0] is not None:
    print("Key: ", result[0])
    print(result[2])
    print("Percentage matched: ", result[1]*100)
else: 
    print("Percentage matched: ", result[1]*100)
    print("Key Not found")
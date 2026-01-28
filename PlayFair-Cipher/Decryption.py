def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = []

    for char in key:
        if char not in combined and char in alphabets:
            combined.append(char)
    for char in alphabets:
        if char not in combined:
            combined.append(char)
    matrix = []
    for i in range(0,25,5):
        matrix.append(combined[i: i+5])
    return matrix


def play_fair_decrypt(matrix, ciphertext):
    decrypt_text = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i+1])
        if row1 == row2:
            decrypt_text = decrypt_text + matrix[row1][(col1 -1) % 5]
            decrypt_text = decrypt_text + matrix[row1][(col2 - 1) % 5]
        elif col1 == col2:
            decrypt_text = decrypt_text + matrix[(row1- 1)% 5][col1]
            decrypt_text = decrypt_text + matrix[(row2 - 1) % 5][col2]
        else:
            decrypt_text = decrypt_text + matrix[row1][col2]
            decrypt_text = decrypt_text + matrix[row2][col1]
    
    for char in decrypt_text:
        if char == 'X':
            decrypt_text = decrypt_text.replace(char, '')
    return decrypt_text

if __name__ == "__main__":
    key = input("Enter the key for Decryption: ")
    matrix = create_matrix(key)
    encrypted_text = "DPRPIR"
print("Decrypted text: ", play_fair_decrypt(matrix, encrypted_text))
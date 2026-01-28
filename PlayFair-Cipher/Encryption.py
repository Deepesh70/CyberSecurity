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
    # print(combined)

    for char in alphabets:
        if char not in combined:
            combined.append(char)
    
    matrix = []
    for i in range(0,25,5):
        matrix.append(combined[i:i+5])
    return matrix


def playfair_encrypt(matrix, plaintext):
    text = plaintext.upper().replace(" ", "").replace("J","I")
    prepared_text = ""
    i = 0
    while i< len(text):
        a = text[i]
        if (i+1) < len(text):
            b = text[i+1]
            if a==b:
                prepared_text = prepared_text + a + 'X'
                i = i + 1
            else:
                prepared_text = prepared_text + a + b
                i = i +2
        else:
            prepared_text = prepared_text + a + 'X'
            i = i + 1
       

    ciphertext = ""
    for j in range(0, len(prepared_text) , 2):
        row1, col1 = find_position(matrix, prepared_text[j])
        row2, col2 = find_position(matrix , prepared_text[j+1])

        if row1 == row2:
            ciphertext= ciphertext + matrix[row1][(col1 + 1) % 5]
            ciphertext  = ciphertext + matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            ciphertext = ciphertext + matrix[(row1 + 1) %5][col1]
            ciphertext = ciphertext + matrix[(row2 + 1) %5][col2]

        else:
            ciphertext = ciphertext + matrix[row1][col2]
            ciphertext = ciphertext + matrix[row2][col1]
    return ciphertext

if __name__ == "__main__":
    key = input("Enter the key: ")
    matrix = create_matrix(key)
    # print("Playfair Matrix:", matrix)

encryptied_text = playfair_encrypt(matrix, 'HELLO')
print("Encrypted Text:", encryptied_text)


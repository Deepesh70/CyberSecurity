def matrix_formation(plain_text, key_length):
    # Padding logic to make sure the grid is a perfect rectangle
    remainder = len(plain_text) % key_length
    if remainder != 0:
        space_length = key_length - remainder
        plain_text = plain_text + "X" * space_length
    
    matrix = []
    # Create the grid row by row
    for i in range(0, len(plain_text), key_length):
        row = list(plain_text[i : i + key_length])
        matrix.append(row)
    return matrix

def transpose(matrix, key_indices):
    transposed = []
    # Read columns based on the key order
    for i in key_indices:
        column = []   # create empty list for this column
        for row in matrix:
            if i < len(row):
                column.append(row[i])
        transposed.append(column)
    return transposed

def Encryption_transposition(plain_text, key):
    # 1. Prepare Key
    key_str = str(key)
    key_length = len(key_str)
    
    # 2. Key Indices (e.g. key=4312 -> indices=[3, 2, 0, 1])
    key_indices = []
    for char in key_str:
        key_indices.append(int(char) - 1)
        
    # 3. Create Matrix
    plain_text_no_space = plain_text.replace(" ", "").upper()
    matrix = matrix_formation(plain_text_no_space, key_length)
    
    # 4. Transpose (scramble columns)
    matrix_transpose = transpose(matrix, key_indices)
    
    # 5. Build Ciphertext string
    cipher_text = ""
    for c in matrix_transpose:
        cipher_text = cipher_text + ''.join(c)
        
    return cipher_text

def Decryption_transposition(cipher_text, key):
    # Step 1: Calculate the grid height (rows)
    key_str = str(key)
    cols = len(key_str)
    rows = len(cipher_text) // cols

    # Step 2: Split the Ciphertext into Columns
    jumbled_columns = []
    for i in range(0, len(cipher_text), rows):
        chunk = cipher_text[i : i + rows]
        jumbled_columns.append(chunk)

    # Step 3: Rearrange columns to the correct order (1, 2, 3...)
    sorted_columns = [""] * cols
    
    current_col_idx = 0
    for digit in key_str:
        target_index = int(digit) - 1
        sorted_columns[target_index] = jumbled_columns[current_col_idx]
        current_col_idx = current_col_idx + 1

    # Step 4: Read the grid row-by-row
    plain_text = ""
    for r in range(rows):
        for col in sorted_columns:
            plain_text = plain_text + col[r]
            
    return plain_text

def main():
    while True:
        print("\nTransposition Cipher Menu")
        print("1. Encrypt (read from plaintext.txt -> write to ciphertext.txt)")
        print("2. Decrypt (read from ciphertext.txt -> write to Recovertxt.txt)")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                # Read Plaintext
                file = open("plaintext.txt", "r")
                plain_text = file.read()
                file.close()

                # Get Key
                key = input("Enter encryption key (numbers only, e.g. 4312): ")
                
                # Encrypt
                cipher_text = Encryption_transposition(plain_text, key)
                
                # Write Ciphertext
                file_out = open("ciphertext.txt", "w")
                file_out.write(cipher_text)
                file_out.close()
                
                print("Encryption Successful! Check 'ciphertext.txt'")
                
            except FileNotFoundError:
                print("Error: 'plaintext.txt' not found. Please create it first.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '2':
            try:
                # Read Ciphertext
                file = open("ciphertext.txt", "r")
                cipher_text = file.read()
                file.close()
                
                # Get Key
                key = input("Enter decryption key: ")
                
                # Decrypt
                decrypted_text = Decryption_transposition(cipher_text, key)
                
                # Write Recovered Text
                file_out = open("Recovertxt.txt", "w")
                file_out.write(decrypted_text)
                file_out.close()
                
                print("Decryption Successful! Check 'Recovertxt.txt'")
                
            except FileNotFoundError:
                print("Error: 'ciphertext.txt' not found. Please encrypt something first.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

'''def rail_fence_encrypt(text, rails):
    rail_fence = [[' ' for _ in range(len(text))] for _ in range(rails)]

    row, col = 0, 0
    direction = 1

    for char in text:
        rail_fence[row][col] = char 
        col += 1

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    encrypted_text = ''.join(char for row in rail_fence for char in row if char != ' ')
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails):
    rail_fence = [[' ' for _ in range(len(encrypted_text))] for _ in range(rails)]

    row, col = 0, 0
    direction = 1

    for char in encrypted_text:
        rail_fence[row][col] = '*'
        col += 1

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if rail_fence[i][j] == '*' and index < len(encrypted_text):
                rail_fence[i][j] = encrypted_text[index]
                index += 1

    plain_text = ''
    row, col = 0, 0
    direction = 1

    for _ in range(len(encrypted_text)):
        plain_text += rail_fence[row][col]
        col += 1

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    return plain_text

text = input("Enter the String: ")
rails = 3

# Encryption
encrypted_text = rail_fence_encrypt(text, rails)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)'''

'''Transposition Cipher - Row Column'''
def encrypt_transposition_cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = int(key)

    num_rows = (len(plaintext) + key - 1) // key

    grid = [[''] * key for _ in range(num_rows)]

    idx = 0
    for col in range(key):
        for row in range(num_rows):
            if idx < len(plaintext):
                grid[row][col] = plaintext[idx]
                idx += 1

    ciphertext = ""
    for row in range(num_rows):
        for col in range(key):
            ciphertext += grid[row][col]

    return ciphertext

def decrypt_transposition_cipher(ciphertext, key):
    key = int(key)

    num_rows = (len(ciphertext) + key - 1) // key

    num_cols = key

    num_empty_cells = num_rows * num_cols - len(ciphertext)

    grid = [[''] * num_cols for _ in range(num_rows)]

    idx = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if idx < len(ciphertext):
                grid[row][col] = ciphertext[idx]
                idx += 1

    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            if num_empty_cells > 0:
                num_empty_cells -= 1
            else:
                plaintext += grid[row][col]

    return plaintext

plaintext = input("Enter the String: ")
key = 4

# Encryption
encrypted_text = encrypt_transposition_cipher(plaintext, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_transposition_cipher(encrypted_text, key)
print("Decrypted:", decrypted_text)



import string

def generate_vigenere_matrix():
    matrix = []
    for i in range(26):
        shifted_alphabet = string.ascii_uppercase[i:] + string.ascii_uppercase[:i]
        matrix.append(list(shifted_alphabet))
    return matrix

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    matrix = generate_vigenere_matrix()
    encrypted_text = ""

    key_index = 0
    for char in plaintext:
        if char in string.ascii_uppercase:
            row = ord(key[key_index]) - ord('A')
            col = ord(char) - ord('A')
            encrypted_char = matrix[row][col]
            encrypted_text += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.upper()

    matrix = generate_vigenere_matrix()
    decrypted_text = ""

    key_index = 0
    for char in ciphertext:
        if char in string.ascii_uppercase:
            row = ord(key[key_index]) - ord('A')
            col = matrix[row].index(char)
            decrypted_char = chr(col + ord('A'))
            decrypted_text += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char

    return decrypted_text

if __name__ == "__main__":
    plaintext = "Information and Security"
    key = "Network Network Network"

    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)
import numpy as np

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))

def pad_plaintext(plaintext, key_length):
    remainder = len(plaintext) % key_length
    if remainder != 0:
        padding = key_length - remainder
        plaintext += 'X' * padding
    return plaintext 

def split_into_blocks(text, block_size):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

def encrypt_block(block, key_matrix):
    block_vector = [letter_to_number(letter) for letter in block]
    encrypted_vector = np.dot(key_matrix, block_vector) % 26
    encrypted_block = [number_to_letter(num) for num in encrypted_vector]
    return ''.join(encrypted_block)

def hill_cipher_encrypt(plaintext, key):
    key_matrix = np.array([[letter_to_number(key[0]), letter_to_number(key[1]), letter_to_number(key[2])]])
    plaintext = plaintext.replace(" ", "").upper()
    key_length = len(key)
    plaintext = pad_plaintext(plaintext, key_length)
    blocks = split_into_blocks(plaintext, key_length)
    encrypted_blocks = [encrypt_block(block, key_matrix) for block in blocks]
    return ''.join(encrypted_blocks)
  
plaintext = "Information"
key = "INS"

ciphertext = hill_cipher_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext
  
ciphertext = "SHIVAM SINGH"
shift = 5
plaintext = decrypt_caesar(ciphertext, shift)
print("Decrypted text:", plaintext)

def monoalphabetic_cipher(text):
    mapping = {'A': 'C', 'B': 'D', 'C': 'Z'}

    cipher_text = ''
    for char in text:
        if char.upper() in mapping:
            cipher_text += mapping[char.upper()]
        else:
            cipher_text += char

    return cipher_text


plaintext = input("Enter the plaintext: ")
ciphertext = monoalphabetic_cipher(plaintext)
print("Ciphertext ", ciphertext) 
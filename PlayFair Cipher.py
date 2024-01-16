import string
def generate_playfair_matrix(key):
    alphabet = string.ascii_uppercase.replace('J','')
    key = key.upper().replace('J','I')
    key += alphabet

    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix
def find_position(matrix,char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i,j
def print_playfair_matrix(matrix):
    for now in matrix:
        print(' '.join(now))
    print()

def encrypt_playfair(plaintext,key):
    playfair_matrix = generate_playfair_matrix(key)
    ciphertext = ''

    plaintext = plaintext.upper().replace('J','I')

    i = 0

    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = ''
        if i+1 < len(plaintext):
            char2 = plaintext[i+1]
        else:
            char2 = 'X'

        row1, col1 = find_position(playfair_matrix, char1)
        row2, col2 = find_position(playfair_matrix, char2)

        if row1 == row2:
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5]
            ciphertext += playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1]
            ciphertext += playfair_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += playfair_matrix[row1][col2]
            ciphertext += playfair_matrix[row2][col1]

        i += 2

    return ciphertext
plaintext = "HELLO"
key = "INS"
ciphertext = encrypt_playfair(plaintext, key)

playfair_matrix = generate_playfair_matrix(key)

print("Playfair Matrix:")
print_playfair_matrix(playfair_matrix)

print("Ciphertext:", ciphertext)
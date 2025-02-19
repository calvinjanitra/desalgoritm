# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table (Inverse of IP)
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion Table (32 bits to 48 bits)
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# Substitution Boxes (S-Boxes)
S_BOXES = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Permutation function
def permute(block, table):
    return ''.join(block[i-1] for i in table)

# XOR two binary strings
def xor(bin1, bin2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))

# Feistel function (simplified for this example)
def feistel(block, key):
    expanded_block = permute(block, E)  # Expansion from 32 to 48 bits
    xored_block = xor(expanded_block, key)
    return xored_block[:32]  # Simplified, take only the first 32 bits
# Key generation (simplified for this example)
def key_generator(key):
    subkeys = []
    for i in range(16):
        # Generate a 48-bit subkey by shifting and selecting bits from the main key
        subkey = key[i:i+48]  # Slice the first 48 bits for now (simplified)
        if len(subkey) < 48:  # Ensure subkey is always 48 bits
            subkey = subkey.zfill(48)
        subkeys.append(subkey)
    return subkeys

# Function to XOR two binary strings
def xor_bin(bin1, bin2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))

# DES encryption function (with CBC mode)
def des_encrypt_cbc(plain_text, key, iv):
    # Initial Permutation
    permuted_block = permute(plain_text, IP)
    # Split block into left and right halves
    left, right = permuted_block[:32], permuted_block[32:]

    # Generate 16 subkeys
    subkeys = key_generator(key)
    
    # CBC-specific: XOR with the IV for the first block
    right = xor_bin(right, iv)

    # Perform 16 rounds of DES
    for i in range(16):
        new_right = xor(left, feistel(right, subkeys[i]))
        left = right
        right = new_right
    
    # Combine left and right halves and apply Final Permutation
    combined = right + left
    cipher_text = permute(combined, FP)
    
    return cipher_text

# DES decryption function (with CBC mode)
def des_decrypt_cbc(cipher_text, key, iv):
    # Initial Permutation
    permuted_block = permute(cipher_text, IP)
    # Split block into left and right halves
    left, right = permuted_block[:32], permuted_block[32:]
    
    # Generate 16 subkeys
    subkeys = key_generator(key)
    
    # Perform 16 rounds of DES in reverse order
    for i in range(15, -1, -1):
        new_right = xor(left, feistel(right, subkeys[i]))
        left = right
        right = new_right

    # Combine left and right halves and apply Final Permutation
    combined = right + left
    decrypted_block = permute(combined, FP)

    # CBC-specific: XOR with the IV for the first block after decryption
    decrypted_block = xor_bin(decrypted_block, iv)
    
    return decrypted_block

# Conversion functions
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].upper()

# Main encryption and decryption process (CBC mode)
def des_process_cbc(data, key, iv, mode="encrypt"):
    # Convert hexadecimal key to binary (64-bit)
    key_bin = hex_to_bin(key)
    iv_bin = hex_to_bin(iv)  # IV must be a 64-bit block as well

    if mode == "encrypt":
        # Convert plaintext to binary (64-bit)
        data_bin = hex_to_bin(data)
        encrypted_bin = des_encrypt_cbc(data_bin, key_bin, iv_bin)
        return bin_to_hex(encrypted_bin)

    elif mode == "decrypt":
        # Convert ciphertext to binary (64-bit)
        data_bin = hex_to_bin(data)
        decrypted_bin = des_decrypt_cbc(data_bin, key_bin, iv_bin)
        return bin_to_hex(decrypted_bin)

# Example usage of DES in CBC mode
plain_text_hex = "0123456789ABCDEF"
key_hex = "133457799BBCDFF1"
iv_hex = "AABB09182736CCDD"  # Example IV (must be unique and random for each encryption)

# Encrypt
cipher_text = des_process_cbc(plain_text_hex, key_hex, iv_hex, mode="encrypt")
print(f"Encrypted (Cipher Text in CBC mode): {cipher_text}")

# Decrypt
decrypted_text = des_process_cbc(cipher_text, key_hex, iv_hex, mode="decrypt")
print(f"Decrypted (Plain Text in CBC mode): {decrypted_text}")

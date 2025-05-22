# Exercise: Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

print(f"chars: {chars}")
print(f"keys : {keys}")


# Encrypt
def encrypt():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += keys[index]

    print(f"Original: {plain_text}")
    print(f"Encrypt : {cipher_text}")


# Decrypt
def decrypt():
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = keys.index(letter)
        plain_text += chars[index]

    print(f"Encrypt : {cipher_text}")
    print(f"Original: {plain_text}")


def main():
    encrypt()
    decrypt()


if __name__ == "__main__":
    main()

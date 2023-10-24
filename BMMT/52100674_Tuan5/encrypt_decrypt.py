def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()  
    key_index = 0

    for char in plaintext:
        if char.isalpha():  
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext
  
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()  
    key_index = 0

    for char in ciphertext:
        if char.isalpha():  
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter the option number: ")

        if choice == "1":
            plaintext = input("Enter the plaintext to encrypt: ")
            key = input("Enter the encryption key: ")
            encrypted_text = vigenere_encrypt(plaintext, key)
            print("Encrypted text:", encrypted_text)

        elif choice == "2":
            ciphertext = input("Enter the ciphertext to decrypt: ")
            key = input("Enter the decryption key: ")
            decrypted_text = vigenere_decrypt(ciphertext, key)
            print("Decrypted text:", decrypted_text)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

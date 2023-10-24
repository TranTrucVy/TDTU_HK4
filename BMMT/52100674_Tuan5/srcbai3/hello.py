from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file(key, iv, input_file, output_file):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    with open(input_file, 'rb') as file:
        plaintext = file.read()
        ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    with open(output_file, 'wb') as file:
        file.write(ciphertext)

def decrypt_file(key, iv, input_file, output_file):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    with open(input_file, 'rb') as file:
        ciphertext = file.read()
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    with open(output_file, 'wb') as file:
        file.write(plaintext)
        
def main():
    print("1. Ma hoa")
    print("2. Giai ma")
    choice = input("Nhap option: ")

    key = input("Nhap key 8 kitu: ").encode('utf-8')
    iv = input("Nhap IV 8 kitu: ").encode('utf-8')
    input_file = input("Nhap ten tep dau vao: ")
    output_file = input("Nhap ten tep dau ra: ")

    if choice == '1':
        encrypt_file(key, iv, input_file, output_file)
        print("File ma hoa thanh cong!")

        # Đọc nội dung tệp gốc và tệp sau khi mã hóa
        with open(input_file, 'rb') as file:
            original_content = file.read()
        with open(output_file, 'rb') as file:
            encrypted_content = file.read()

        # In nội dung của tệp gốc
        print("Noi dung trong file goc:")
        print(original_content)

        # In nội dung của tệp sau khi mã hóa
        print("Noi dung trong file ma hoa:")
        print(encrypted_content)
    elif choice == '2':
        decrypt_file(key, iv, input_file, output_file)
        print("File giai ma thanh cong!")

        # Đọc nội dung tệp gốc và tệp sau khi giải mã
        with open(input_file, 'rb') as file:
            original_content = file.read()
        with open(output_file, 'rb') as file:
            decrypted_content = file.read()

        # In nội dung của tệp gốc
        print("Noi dung trong file goc:")
        print(original_content)

        # In nội dung của tệp sau khi giải mã
        print("Noi dung trong file giai ma:")
        print(decrypted_content)
    else:
        print("Khong hop le chon lai")

# def main():
#     print("1. Ma hoa")
#     print("2. Giai ma")
#     choice = input("Nhap option: ")

#     key = input("Nhap key 8 kitu: ").encode('utf-8')
#     iv = input("Nhap IV 8 kitu: ").encode('utf-8')
#     input_file = input("Nhap ten tep dau vao: ")
#     output_file = input("Nhap ten tep dau ra: ")

#     if choice == '1':
#         encrypt_file(key, iv, input_file, output_file)
#         print("File ma hoa thanh cong")
#     elif choice == '2':
#         decrypt_file(key, iv, input_file, output_file)
#         print("File giai ma thanh cong!")
#     else:
#         print("Khong hop le chon lai")

if __name__ == "__main__":
    main()

import rsa

PUBLIC_KEY_FILE = '52100674_2/public_keys.pem'
PRIVATE_KEY_FILE = '52100674_2/private_keys.pem'

def generate_keys():
    (public_key, private_key) = rsa.newkeys(2048)
    with open(PUBLIC_KEY_FILE, 'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))
    with open(PRIVATE_KEY_FILE, 'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))

def load_keys():
    with open(PUBLIC_KEY_FILE, 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    with open(PRIVATE_KEY_FILE, 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key, public_key

def encrypt(message, key):
    message_bytes = message.encode('utf-8')
    return rsa.encrypt(message_bytes, key)

def decrypt(ciphertext, key):
    try:
        message_bytes = rsa.decrypt(ciphertext, key)
        message = message_bytes.decode('utf-8')
        return message
    except rsa.DecryptionError:
        return "Decryption error: Incorrect key"

def sign(message, key):
    message_bytes = message.encode('utf-8')
    signature = rsa.sign(message_bytes, key, 'SHA-256')
    return signature

def verify(message, signature, key):
    message_bytes = message.encode('utf-8')
    try:
        rsa.verify(message_bytes, signature, key)
        return True
    except rsa.VerificationError:
        return False

generate_keys()
private_key, public_key = load_keys()

message = input('Enter message: ')
ciphertext = encrypt(message, public_key)
signature = sign(message, private_key)
plaintext = decrypt(ciphertext, private_key)

print(f'Ciphertext:\n{ciphertext}')
print(f'Signature:\n{signature}')

if plaintext:
    print(f'Plaintext:\n{plaintext}')
else:
    print('Decryption error.')

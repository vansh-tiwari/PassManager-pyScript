from cryptography.fernet import Fernet

def write_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named 'key.key'
    return open('key.key', 'rb').read()

# generate and write a new key
write_key()
# load the previously generated key
key = load_key()
# some message
msg = 'abhishek12'.encode()
# initialize the Fernet class
f = Fernet(key)
# encrypt the msg
encrypted = f.encrypt(msg)
print(encrypted)
# decrypt the encrypted msg
decrypted = f.decrypt(encrypted)
print(decrypted)
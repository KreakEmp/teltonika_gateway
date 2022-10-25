from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

def encrypt_with_public_key(message, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_msg = encryptor.encrypt(message)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg

pubkey = """-----BEGIN RSA PUBLIC KEY-----
        MEgCQQCcADcRmHrTtDWsknzx5D64iNdwYscWi0+fI8nh9cO26HtRSeXBnSJuMlJK
        is7qn+lznsbi3DRwYOdM4w/7Z8bhAgMBAAE=
        -----END RSA PUBLIC KEY-----"""
# x509pem = open('public.pem', 'r').read() # load the key alternatively from the file system

key = RSA.import_key(pubkey)      # add the key import with import_key() or importKey()
byte_message = b'Surajit'

encoded_encrypted_msg = encrypt_with_public_key(byte_message, key)
print(encoded_encrypted_msg.decode('utf-8'))
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP, AES
from base64 import b64encode, b64decode


def encrypt(key, plaintext):
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext.encode('utf-8'))
    return {
      'ciphertext': b64encode(ciphertext).decode('utf-8'),
      'tag': b64encode(tag).decode('utf-8'),
      'session_key': b64encode(enc_session_key).decode('utf-8'),
      'nonce': b64encode(cipher_aes.nonce).decode('utf-8')
      }

def decrypt(key, cipher_msg):
    cipher_rsa = PKCS1_OAEP.new(key)
    session_key = cipher_rsa.decrypt(
            b64decode(cipher_msg['session_key'].encode('utf-8')))
    cipher_aes = AES.new(
            session_key,
            AES.MODE_EAX,
            b64decode(cipher_msg['nonce'].encode('utf-8')))
    return cipher_aes.decrypt_and_verify(
            b64decode(cipher_msg['ciphertext'].encode('utf-8')),
            b64decode(cipher_msg['tag'].encode('utf-8'))).decode('utf-8')

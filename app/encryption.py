# app/encryption.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
from app.models import Ciphertext

def encrypt_data(message: str, attributes: list, master_key: bytes) -> Ciphertext:
    """
    Encrypts the message using AES CBC mode and attaches hidden attributes.
    """
    cipher = AES.new(master_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return Ciphertext(iv=iv, ciphertext=ct, attributes=attributes)

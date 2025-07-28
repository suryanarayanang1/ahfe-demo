# app/keygen.py

from Crypto.Random import get_random_bytes
from base64 import b64encode

def generate_master_key():
    key = get_random_bytes(16)  # AES 128-bit
    return b64encode(key).decode('utf-8')  # Send as string for storage or sharing

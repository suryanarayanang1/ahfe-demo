# app/evaluator.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from app.utils import overlap_distance

def decrypt_data(ciphertext_obj, eval_attributes, threshold, master_key):
    """
    Decrypt message only if the evaluator's attributes meet or exceed the similarity threshold.
    """
    similarity = overlap_distance(ciphertext_obj.attributes, eval_attributes)
    
    if similarity >= threshold:
        iv = b64decode(ciphertext_obj.iv)
        ct = b64decode(ciphertext_obj.ciphertext)
        cipher = AES.new(master_key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode()
    else:
        return "ACCESS DENIED"

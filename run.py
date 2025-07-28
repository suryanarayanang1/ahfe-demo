'''
# run.py generating master key

from app.utils import overlap_distance
from app.keygen import generate_master_key

print("🔐 Master Key:", generate_master_key())

a = [1, 2, 3, 4]
b = [1, 0, 3, 4]

print("✅ Overlap Distance:", overlap_distance(a, b))


# run.py encryption

from base64 import b64decode
from app.encryption import encrypt_data
from app.models import Ciphertext
from app.keygen import generate_master_key

# Step 1: Generate key
key_str = generate_master_key()
print(f"\n🔐 Master Key (base64): {key_str}")
master_key = b64decode(key_str)

# Step 2: Define message and attributes
message = "Patient has high blood pressure"
attributes = [2, 4, 6, 8]

# Step 3: Encrypt
ciphertext = encrypt_data(message, attributes, master_key)

# Step 4: Show result
print("\n🧾 Encrypted Output:")
print(f"IV: {ciphertext.iv}")
print(f"Ciphertext: {ciphertext.ciphertext}")
print(f"Hidden Attributes: {ciphertext.attributes}")


#encrypt decrypt
from app.keygen import generate_master_key
from app.encryption import encrypt_data
from app.evaluator import decrypt_data
from base64 import b64decode

# Generate and decode master key
master_key_str = generate_master_key()
master_key = b64decode(master_key_str)

# Encrypt a message
ciphertext = encrypt_data("Patient has high fever", [1, 2, 3, 4], master_key)

# Evaluator 1 (Matching)
evaluator1_attrs = [1, 2, 0, 4]
threshold = 3
print("🧠 Evaluator Attempt (Matching Attributes):")
result = decrypt_data(ciphertext, evaluator1_attrs, threshold, master_key)
print("Result:", result)

# Evaluator 2 (Non-Matching)
evaluator2_attrs = [0, 0, 0, 0]
print("\n🚫 Evaluator Attempt (Non-Matching):")
result2 = decrypt_data(ciphertext, evaluator2_attrs, threshold, master_key)
print("Result:", result2)

'''
#store key in storage.py

from app.keygen import generate_master_key
from app.encryption import encrypt_data
from app.evaluator import decrypt_data
from app.storage import init_db, insert_data, get_all_data
from base64 import b64decode
from app.models import Ciphertext

# 🔧 Init database
init_db()

# 🔐 Generate master key
master_key_str = generate_master_key()
master_key = b64decode(master_key_str)

# 🧾 Encrypt a sample message
message = "Patient has irregular heart rate"
attributes = [2, 5, 1, 4]
ciphertext = encrypt_data(message, attributes, master_key)

# 💾 Store it
insert_data(ciphertext.iv, ciphertext.ciphertext, ciphertext.attributes)
print("✅ Data encrypted and stored in SQLite.")

# 📥 Retrieve and decrypt all records
print("\n🔓 Decryption Results:")
rows = get_all_data()
threshold = 3
eval_attrs = [2, 0, 1, 4]  # You can change this

for row in rows:
    _, iv, ct, attr_str = row
    attrs = list(map(int, attr_str.split(",")))
    cipher_obj = Ciphertext(iv=iv, ciphertext=ct, attributes=attrs)
    result = decrypt_data(cipher_obj, eval_attrs, threshold, master_key)
    print("→", result)

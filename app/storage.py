# app/storage.py

import sqlite3
import os

DB_PATH = "database/ahfe.db"

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encrypted_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            iv TEXT NOT NULL,
            ciphertext TEXT NOT NULL,
            attributes TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def insert_data(iv, ciphertext, attributes):
    attr_str = ",".join(map(str, attributes))
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO encrypted_data (iv, ciphertext, attributes) VALUES (?, ?, ?)",
        (iv, ciphertext, attr_str)
    )
    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, iv, ciphertext, attributes FROM encrypted_data")
    rows = cursor.fetchall()
    conn.close()
    return rows

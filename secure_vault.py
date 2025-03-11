import sqlite3
import bcrypt
import os
import base64
import getpass
import pyperclip
from cryptography.fernet import Fernet

# Database & Key Setup
db_file = "vault.db"
key_file = "key.key"

# Generate and load encryption key
def generate_key():
    key = Fernet.generate_key()
    with open(key_file, "wb") as keyfile:
        keyfile.write(key)

def load_key():
    return open(key_file, "rb").read()

if not os.path.exists(key_file):
    generate_key()
encryption_key = load_key()
cipher = Fernet(encryption_key)

# Database Initialization
def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS vault (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        service TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()
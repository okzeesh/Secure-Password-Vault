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
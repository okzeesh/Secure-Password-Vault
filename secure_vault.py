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

# Master Password Setup
def setup_master_password():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS master (password TEXT)")
    cursor.execute("SELECT password FROM master")
    result = cursor.fetchone()
    if result is None:
        master_password = getpass.getpass("Set a Master Password: ")
        hashed = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO master (password) VALUES (?)", (hashed,))
        conn.commit()
    conn.close()

# Verify Master Password
def verify_master_password():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM master")
    hashed_password = cursor.fetchone()[0]  # Fetch hashed password

    conn.close()

    while True:
        master_password = getpass.getpass("Enter Master Password: ")
        if bcrypt.checkpw(master_password.encode(), hashed_password):
            print("Access Granted!\n")
            break
        else:
            print("Incorrect Password. Try Again.")


# Add New Credential
def add_credential():
    service = input("Service Name: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    encrypted_password = cipher.encrypt(password.encode()).decode()
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vault (service, username, password) VALUES (?, ?, ?)", (service, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Credential Stored Successfully!\n")

# Retrieve Stored Credentials
def view_credentials():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id, service, username, password FROM vault")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("No credentials stored yet.\n")
        return
    
    print("Stored Credentials:")
    for row in rows:
        decrypted_password = cipher.decrypt(row[3].encode()).decode()
        print(f"[{row[0]}] {row[1]} - {row[2]} - {decrypted_password}")
    print()
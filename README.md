# Secure Password Vault

## Overview

The **Secure Password Vault** is a simple yet effective password manager built using Python. It securely stores and retrieves passwords using **AES encryption (Fernet)** and a **SQLite database**. Users can manage their credentials with a master password for authentication.

## Features

- 🔐 **AES Encryption (Fernet)** – Encrypts stored passwords for security.
- 🔑 **Master Password Authentication** – Uses **bcrypt hashing** to protect access.
- 🗄️ **SQLite Database Storage** – Stores credentials securely.
- 📋 **Clipboard Integration** – Copies passwords to clipboard for easy use.
- 🖥️ **Simple CLI Interface** – User-friendly command-line interactions.

## Installation

To use the Secure Password Vault, you need to install the required dependencies:

```bash
pip install cryptography bcrypt pyperclip
```

## Usage

Run the script using Python:

```bash
python secure_vault.py
```

### First-Time Setup

1. The script will prompt you to **set a master password**.
2. This password is **hashed** and stored securely in the database.

### Available Actions

- **Add Credentials** – Store a new username & password securely.
- **View Credentials** – Retrieve and view stored passwords.
- **Copy Password** – Copy a password to clipboard securely.
- **Exit** – Safely close the vault.

## Security Measures

- **Master password is hashed using bcrypt** for security.
- **Passwords are encrypted using Fernet (AES encryption).**
- **Sensitive information is never stored in plain text.**

## Troubleshooting

- If you see an `AttributeError: 'bytes' object has no attribute 'encode'`, ensure `bcrypt.checkpw()` receives a **bytes** object.
- If the encryption key (`key.key`) is lost, stored passwords **cannot** be decrypted.

## License

This project is open-source and free to use. Modify and enhance as needed! 🚀

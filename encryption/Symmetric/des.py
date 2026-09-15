import base64
import os

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


BLOCK_SIZE = 8
KEY_SIZE = 8


def generate_key():
    return os.urandom(KEY_SIZE)


def encrypt(plaintext, key):
    if len(key) != KEY_SIZE:
        raise ValueError(
            "DES key must be exactly 8 bytes."
        )

    iv = os.urandom(BLOCK_SIZE)

    cipher = DES.new(
        key,
        DES.MODE_CBC,
        iv
    )

    padded_data = pad(
        plaintext.encode("utf-8"),
        BLOCK_SIZE
    )

    ciphertext = cipher.encrypt(padded_data)

    return base64.b64encode(
        iv + ciphertext
    ).decode("utf-8")


def decrypt(ciphertext, key):
    if len(key) != KEY_SIZE:
        raise ValueError(
            "DES key must be exactly 8 bytes."
        )

    data = base64.b64decode(ciphertext)

    iv = data[:BLOCK_SIZE]
    encrypted_data = data[BLOCK_SIZE:]

    cipher = DES.new(
        key,
        DES.MODE_CBC,
        iv
    )

    padded_plaintext = cipher.decrypt(
        encrypted_data
    )

    plaintext = unpad(
        padded_plaintext,
        BLOCK_SIZE
    )

    return plaintext.decode("utf-8")
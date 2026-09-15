import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


KEY_SIZE = 32
NONCE_SIZE = 12


def generate_key():
    return AESGCM.generate_key(bit_length=256)


def encrypt(plaintext, key):
    if len(key) not in (16, 24, 32):
        raise ValueError(
            "AES key must be 16, 24, or 32 bytes."
        )

    nonce = os.urandom(NONCE_SIZE)

    aes = AESGCM(key)

    ciphertext = aes.encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None
    )

    return base64.b64encode(
        nonce + ciphertext
    ).decode("utf-8")


def decrypt(ciphertext, key):
    if len(key) not in (16, 24, 32):
        raise ValueError(
            "AES key must be 16, 24, or 32 bytes."
        )

    data = base64.b64decode(ciphertext)

    nonce = data[:NONCE_SIZE]
    encrypted_data = data[NONCE_SIZE:]

    aes = AESGCM(key)

    plaintext = aes.decrypt(
        nonce,
        encrypted_data,
        None
    )

    return plaintext.decode("utf-8")
import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
    load_pem_private_key,
    load_pem_public_key
)


def generate_keys(key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        Encoding.PEM,
        PrivateFormat.PKCS8,
        NoEncryption()
    )

    public_pem = public_key.public_bytes(
        Encoding.PEM,
        PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem


def encrypt(plaintext, public_key_pem):
    public_key = load_pem_public_key(public_key_pem)

    ciphertext = public_key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(ciphertext).decode("utf-8")


def decrypt(ciphertext, private_key_pem):
    private_key = load_pem_private_key(
        private_key_pem,
        password=None
    )

    ciphertext_bytes = base64.b64decode(ciphertext)

    plaintext = private_key.decrypt(
        ciphertext_bytes,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext.decode("utf-8")
import hashlib
import secrets
import base64

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


# =========================================================
# PBKDF2
# =========================================================

def hash_password_pbkdf2(password, iterations=600_000):
    """
    Hash a password using PBKDF2-HMAC-SHA256.
    """

    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations
    )

    salt_b64 = base64.b64encode(salt).decode("utf-8")
    hash_b64 = base64.b64encode(password_hash).decode("utf-8")

    return f"pbkdf2_sha256${iterations}${salt_b64}${hash_b64}"


def verify_password_pbkdf2(password, stored_hash):
    """
    Verify a password against a PBKDF2 hash.
    """

    try:
        algorithm, iterations, salt_b64, hash_b64 = stored_hash.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations)

        salt = base64.b64decode(salt_b64)
        expected_hash = base64.b64decode(hash_b64)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations
        )

        return secrets.compare_digest(
            password_hash,
            expected_hash
        )

    except (ValueError, TypeError):
        return False


# =========================================================
# scrypt
# =========================================================

def hash_password_scrypt(
    password,
    n=16384,
    r=8,
    p=1
):
    """
    Hash a password using scrypt.
    """

    salt = secrets.token_bytes(16)

    password_hash = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=n,
        r=r,
        p=p,
        dklen=32
    )

    salt_b64 = base64.b64encode(salt).decode("utf-8")
    hash_b64 = base64.b64encode(password_hash).decode("utf-8")

    return (
        f"scrypt${n}${r}${p}"
        f"${salt_b64}${hash_b64}"
    )


def verify_password_scrypt(password, stored_hash):
    """
    Verify a password against a scrypt hash.
    """

    try:
        (
            algorithm,
            n,
            r,
            p,
            salt_b64,
            hash_b64
        ) = stored_hash.split("$")

        if algorithm != "scrypt":
            return False

        n = int(n)
        r = int(r)
        p = int(p)

        salt = base64.b64decode(salt_b64)
        expected_hash = base64.b64decode(hash_b64)

        password_hash = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=n,
            r=r,
            p=p,
            dklen=32
        )

        return secrets.compare_digest(
            password_hash,
            expected_hash
        )

    except (ValueError, TypeError):
        return False


# =========================================================
# Argon2
# =========================================================

password_hasher = PasswordHasher()


def hash_password_argon2(password):
    """
    Hash a password using Argon2id.
    """

    return password_hasher.hash(password)


def verify_password_argon2(password, stored_hash):
    """
    Verify a password against an Argon2 hash.
    """

    try:
        return password_hasher.verify(
            stored_hash,
            password
        )

    except VerifyMismatchError:
        return False

    except Exception:
        return False
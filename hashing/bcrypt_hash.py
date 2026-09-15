import bcrypt


def hash_password(password):
    """
    Hash a password using bcrypt.

    Args:
        password (str): Plaintext password.

    Returns:
        str: Bcrypt password hash.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode("utf-8")


def verify_password(password, hashed_password):
    """
    Verify a password against a bcrypt hash.

    Args:
        password (str): Plaintext password.
        hashed_password (str): Bcrypt hash.

    Returns:
        bool: True if password matches, otherwise False.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if not isinstance(hashed_password, str):
        raise TypeError("Hashed password must be a string.")

    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )
    except (ValueError, TypeError):
        return False
import secrets
import string


ALPHABET = string.ascii_uppercase


def generate_key(length):
    if length < 1:
        raise ValueError("Length must be at least 1.")

    return "".join(
        secrets.choice(ALPHABET)
        for _ in range(length)
    )


def encrypt(text, key):
    key = key.upper()

    letters = [
        char for char in text
        if char.isalpha()
    ]

    if len(key) != len(letters):
        raise ValueError(
            "Key length must match the number of letters in the text."
        )

    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord("A")

            if char.isupper():
                result += chr(
                    (ord(char) - ord("A") + shift) % 26
                    + ord("A")
                )
            else:
                result += chr(
                    (ord(char) - ord("a") + shift) % 26
                    + ord("a")
                )

            key_index += 1

        else:
            result += char

    return result


def decrypt(text, key):
    key = key.upper()

    letters = [
        char for char in text
        if char.isalpha()
    ]

    if len(key) != len(letters):
        raise ValueError(
            "Key length must match the number of letters in the text."
        )

    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord("A")

            if char.isupper():
                result += chr(
                    (ord(char) - ord("A") - shift) % 26
                    + ord("A")
                )
            else:
                result += chr(
                    (ord(char) - ord("a") - shift) % 26
                    + ord("a")
                )

            key_index += 1

        else:
            result += char

    return result
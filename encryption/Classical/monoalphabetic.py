import string
import random


ALPHABET = string.ascii_uppercase


def generate_key():
    key = list(ALPHABET)
    random.shuffle(key)
    return "".join(key)


def validate_key(key):
    key = key.upper()

    if len(key) != 26:
        raise ValueError("Key must contain exactly 26 letters.")

    if not key.isalpha():
        raise ValueError("Key must contain letters only.")

    if len(set(key)) != 26:
        raise ValueError("Key must contain 26 unique letters.")

    return key


def encrypt(text, key):
    key = validate_key(key)

    result = ""

    for char in text:
        if char.isupper():
            result += key[ord(char) - ord("A")]

        elif char.islower():
            result += key[ord(char) - ord("a")].lower()

        else:
            result += char

    return result


def decrypt(text, key):
    key = validate_key(key)

    result = ""

    for char in text:
        if char.isupper():
            result += ALPHABET[key.index(char)]

        elif char.islower():
            result += ALPHABET[key.index(char.upper())].lower()

        else:
            result += char

    return result
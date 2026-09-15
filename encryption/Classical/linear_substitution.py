import string


ALPHABET = string.ascii_uppercase


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
            index = ord(char) - ord("A")
            result += key[index]

        elif char.islower():
            index = ord(char) - ord("a")
            result += key[index].lower()

        else:
            result += char

    return result


def decrypt(text, key):
    key = validate_key(key)

    result = ""

    for char in text:
        if char.isupper():
            index = key.index(char)
            result += ALPHABET[index]

        elif char.islower():
            index = key.index(char.upper())
            result += ALPHABET[index].lower()

        else:
            result += char

    return result
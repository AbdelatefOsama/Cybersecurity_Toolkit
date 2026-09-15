def validate_key(key):
    key = key.upper()

    if not key.isalpha():
        raise ValueError("Key must contain letters only.")

    if not key:
        raise ValueError("Key cannot be empty.")

    return key


def encrypt(text, key):
    key = validate_key(key)

    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("A")

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
    key = validate_key(key)

    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("A")

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
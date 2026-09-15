def validate_key(key):
    key = key.upper()

    if not key.isalpha():
        raise ValueError("Key must contain letters only.")

    if not key:
        raise ValueError("Key cannot be empty.")

    return key


def encrypt(text, key):
    key = validate_key(key)

    plaintext_letters = [
        char for char in text.upper()
        if char.isalpha()
    ]

    keystream = key + "".join(plaintext_letters)

    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(
                keystream[key_index]
            ) - ord("A")

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

    ciphertext_letters = [
        char for char in text.upper()
        if char.isalpha()
    ]

    result = ""
    keystream = list(key)

    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(
                keystream[key_index]
            ) - ord("A")

            decrypted = chr(
                (ord(char.upper()) - ord("A") - shift) % 26
                + ord("A")
            )

            if char.isupper():
                result += decrypted
            else:
                result += decrypted.lower()

            keystream.append(decrypted)
            key_index += 1

        else:
            result += char

    return result
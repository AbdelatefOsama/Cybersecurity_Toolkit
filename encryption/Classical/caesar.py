def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr(
                (ord(char) - ord("A") + shift) % 26
                + ord("A")
            )
        elif char.islower():
            result += chr(
                (ord(char) - ord("a") + shift) % 26
                + ord("a")
            )
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
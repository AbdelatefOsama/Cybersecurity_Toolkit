def rot13(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr(
                (ord(char) - ord("A") + 13) % 26
                + ord("A")
            )
        elif char.islower():
            result += chr(
                (ord(char) - ord("a") + 13) % 26
                + ord("a")
            )
        else:
            result += char

    return result
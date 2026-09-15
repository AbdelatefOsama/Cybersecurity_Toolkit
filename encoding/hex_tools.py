def encode(text):
    """
    Encode text into hexadecimal representation.
    """
    return text.encode("utf-8").hex()


def decode(encoded_text):
    """
    Decode hexadecimal text back to UTF-8.
    """
    try:
        return bytes.fromhex(encoded_text).decode("utf-8")
    except Exception as error:
        raise ValueError(f"Invalid hexadecimal input: {error}")


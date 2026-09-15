import base64


def encode(text):
    """
    Encode text using Base32.
    """
    return base64.b32encode(text.encode("utf-8")).decode("utf-8")


def decode(encoded_text):
    """
    Decode Base32 text.
    """
    try:
        return base64.b32decode(encoded_text, casefold=True).decode("utf-8")
    except Exception as error:
        raise ValueError(f"Invalid Base32 input: {error}")

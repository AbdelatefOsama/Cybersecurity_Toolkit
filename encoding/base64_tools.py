import base64


def encode(text):
    """
    Encode text using Base64.
    """
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def decode(encoded_text):
    """
    Decode Base64 text.
    """
    try:
        return base64.b64decode(encoded_text, validate=True).decode("utf-8")
    except Exception as error:
        raise ValueError(f"Invalid Base64 input: {error}")

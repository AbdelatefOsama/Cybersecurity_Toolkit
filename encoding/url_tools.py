from urllib.parse import quote, unquote


def encode(text):
    """
    URL percent-encode text.
    """
    return quote(text, safe="")


def decode(encoded_text):
    """
    Decode URL percent-encoded text.
    """
    return unquote(encoded_text)

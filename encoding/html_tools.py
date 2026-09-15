import html


def encode(text):
    """
    HTML-encode special characters.
    """
    return html.escape(text, quote=True)


def decode(encoded_text):
    """
    Decode HTML entities back to normal text.
    """
    return html.unescape(encoded_text)


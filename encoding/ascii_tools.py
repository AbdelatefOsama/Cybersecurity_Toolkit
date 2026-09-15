def encode(text):
    """
    Convert text to ASCII decimal values.
    """
    try:
        return " ".join(str(ord(char)) for char in text)
    except Exception as error:
        raise ValueError(f"ASCII encoding failed: {error}")


def decode(encoded_text):
    """
    Convert ASCII decimal values back to text.
    """
    try:
        values = encoded_text.split()

        for value in values:
            number = int(value)

            if number < 0 or number > 127:
                raise ValueError(
                    f"Invalid ASCII value: {number}. "
                    "ASCII values must be between 0 and 127."
                )

        return "".join(chr(int(value)) for value in values)

    except ValueError as error:
        raise ValueError(f"Invalid ASCII input: {error}")

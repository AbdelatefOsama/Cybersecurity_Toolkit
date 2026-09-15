def encode(text):
    """
    Convert text to binary representation.
    """
    return " ".join(
        format(byte, "08b")
        for byte in text.encode("utf-8")
    )


def decode(encoded_text):
    """
    Convert binary representation back to UTF-8 text.
    """
    try:
        binary_values = encoded_text.split()

        result = bytearray()

        for binary in binary_values:
            if len(binary) != 8 or any(bit not in "01" for bit in binary):
                raise ValueError(
                    f"Invalid binary byte: {binary}"
                )

            result.append(int(binary, 2))

        return bytes(result).decode("utf-8")

    except UnicodeDecodeError:
        raise ValueError(
            "Binary data does not represent valid UTF-8 text."
        )

    except ValueError as error:
        raise ValueError(
            f"Invalid binary input: {error}"
        )


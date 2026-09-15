def validate_key(key):
    if not key:
        raise ValueError("Key cannot be empty.")

    if not key.isalpha():
        raise ValueError("Key must contain letters only.")

    return key.upper()


def encrypt(text, key):
    key = validate_key(key)

    columns = len(key)

    clean_text = "".join(
        char for char in text
        if not char.isspace()
    )

    rows = [
        clean_text[i:i + columns]
        for i in range(0, len(clean_text), columns)
    ]

    while len(rows[-1]) < columns:
        rows[-1] += "X"

    order = sorted(
        range(columns),
        key=lambda i: (key[i], i)
    )

    result = ""

    for column in order:
        for row in rows:
            result += row[column]

    return result


def decrypt(text, key):
    key = validate_key(key)

    columns = len(key)

    if len(text) % columns != 0:
        raise ValueError(
            "Ciphertext length must be divisible by key length."
        )

    rows_count = len(text) // columns

    order = sorted(
        range(columns),
        key=lambda i: (key[i], i)
    )

    grid = [
        [""] * columns
        for _ in range(rows_count)
    ]

    index = 0

    for column in order:
        for row in range(rows_count):
            grid[row][column] = text[index]
            index += 1

    return "".join(
        "".join(row)
        for row in grid
    ).rstrip("X")
def create_matrix(key):
    key = key.upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    combined = ""

    for char in key + alphabet:
        if char.isalpha() and char not in combined:
            combined += char

    return [
        combined[0:5],
        combined[5:10],
        combined[10:15],
        combined[15:20],
        combined[20:25]
    ]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

    raise ValueError(f"Character not found: {char}")


def prepare_text(text):
    text = text.upper().replace("J", "I")

    text = "".join(
        char for char in text
        if char.isalpha()
    )

    prepared = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            prepared.append(first + "X")
            i += 1

        else:
            second = text[i + 1]

            if first == second:
                prepared.append(first + "X")
                i += 1
            else:
                prepared.append(first + second)
                i += 2

    return prepared


def encrypt(text, key):
    matrix = create_matrix(key)
    pairs = prepare_text(text)

    result = ""

    for first, second in pairs:
        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]

        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


def decrypt(text, key):
    matrix = create_matrix(key)

    text = text.upper().replace("J", "I")
    text = "".join(
        char for char in text
        if char.isalpha()
    )

    if len(text) % 2 != 0:
        raise ValueError(
            "Ciphertext length must be even."
        )

    result = ""

    for i in range(0, len(text), 2):
        first = text[i]
        second = text[i + 1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]

        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]

        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


def display_matrix(key):
    matrix = create_matrix(key)

    for row in matrix:
        print(" ".join(row))
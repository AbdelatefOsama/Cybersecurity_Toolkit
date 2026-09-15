import hashlib

from hashing.standard import SUPPORTED_ALGORITHMS


def calculate_file_hash(file_path, algorithm, chunk_size=8192):
    """
    Calculate the hash of a file using the selected algorithm.
    """

    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_function = SUPPORTED_ALGORITHMS[algorithm]
    hash_object = hash_function()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(chunk_size)

                if not chunk:
                    break

                hash_object.update(chunk)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")

    return hash_object.hexdigest()
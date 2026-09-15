import time
import hashlib
import itertools
import string


SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "sha3_224": hashlib.sha3_224,
    "sha3_256": hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_512": hashlib.sha3_512,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s,
}


CHARACTER_SETS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "letters": string.ascii_letters,
    "digits": string.digits,
    "lowercase_digits": string.ascii_lowercase + string.digits,
    "letters_digits": string.ascii_letters + string.digits,
}


def brute_force_attack(
    target_hash,
    algorithm,
    max_length,
    charset
):
    """
    Perform a brute-force attack against a target hash.

    Intended for educational use and authorized labs.

    Returns:
        {
            "found": bool,
            "password": str or None,
            "attempts": int,
            "time": float
        }
    """

    algorithm = algorithm.lower()
    target_hash = target_hash.strip().lower()

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(
            f"Unsupported algorithm: {algorithm}"
        )

    if charset not in CHARACTER_SETS:
        raise ValueError(
            f"Unsupported character set: {charset}"
        )

    if max_length < 1:
        raise ValueError(
            "Maximum length must be at least 1."
        )

    hash_function = SUPPORTED_ALGORITHMS[algorithm]
    characters = CHARACTER_SETS[charset]

    attempts = 0
    start_time = time.perf_counter()

    for length in range(1, max_length + 1):

        for combination in itertools.product(
            characters,
            repeat=length
        ):
            password = "".join(combination)

            attempts += 1

            calculated_hash = hash_function(
                password.encode("utf-8")
            ).hexdigest()

            if calculated_hash.lower() == target_hash:
                elapsed_time = time.perf_counter() - start_time

                return {
                    "found": True,
                    "password": password,
                    "attempts": attempts,
                    "time": elapsed_time
                }

    elapsed_time = time.perf_counter() - start_time

    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time": elapsed_time
    }


def get_character_sets():
    """
    Return available character sets.
    """

    return list(CHARACTER_SETS.keys())
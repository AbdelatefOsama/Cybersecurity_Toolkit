import time
import hashlib


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


def dictionary_attack(target_hash, wordlist_path, algorithm):
    """
    Perform a dictionary attack against a target hash.

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
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_function = SUPPORTED_ALGORITHMS[algorithm]

    attempts = 0
    start_time = time.perf_counter()

    try:
        with open(
            wordlist_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as wordlist:

            for line in wordlist:
                password = line.rstrip("\r\n")

                if not password:
                    continue

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

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Wordlist not found: {wordlist_path}"
        )

    except PermissionError:
        raise PermissionError(
            f"Permission denied: {wordlist_path}"
        )

    elapsed_time = time.perf_counter() - start_time

    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time": elapsed_time
    }
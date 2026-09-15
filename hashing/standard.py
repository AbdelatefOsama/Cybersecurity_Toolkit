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


def calculate_hash(text, algorithm):
    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_function = SUPPORTED_ALGORITHMS[algorithm]

    return hash_function(text.encode("utf-8")).hexdigest()


def get_supported_algorithms():
    return list(SUPPORTED_ALGORITHMS.keys())


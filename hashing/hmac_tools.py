import hashlib
import hmac


SUPPORTED_HMAC_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def calculate_hmac(message, secret_key, algorithm):
    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_HMAC_ALGORITHMS:
        raise ValueError(f"Unsupported HMAC algorithm: {algorithm}")

    key = secret_key.encode("utf-8")
    message = message.encode("utf-8")

    return hmac.new(
        key,
        message,
        SUPPORTED_HMAC_ALGORITHMS[algorithm]
    ).hexdigest()


def get_supported_hmac_algorithms():
    return list(SUPPORTED_HMAC_ALGORITHMS.keys())


import re


HASH_PATTERNS = {
    32: ["MD5", "NTLM"],
    40: ["SHA-1"],
    56: ["SHA-224"],
    64: ["SHA-256", "SHA3-256"],
    96: ["SHA-384", "SHA3-384"],
    128: ["SHA-512", "SHA3-512"],
}


def identify_hash(hash_value):
    """
    Identify possible hash types based on length and hexadecimal format.
    Returns a list of possible hash types.
    """

    hash_value = hash_value.strip()

    # Empty input
    if not hash_value:
        return []

    # Hashes in this module are expected to be hexadecimal
    if not re.fullmatch(r"[0-9a-fA-F]+", hash_value):
        return []

    length = len(hash_value)

    return HASH_PATTERNS.get(length, [])


def get_hash_length(hash_value):
    """
    Return the length of the hash.
    """

    return len(hash_value.strip())
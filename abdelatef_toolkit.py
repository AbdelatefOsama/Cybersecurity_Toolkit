# =========================================================
# HASHING
# =========================================================

from hashing.file_hash import calculate_file_hash
from hashing.compare_hashes import compare_hashes
from hashing.identifier import identify_hash

from hashing.standard import (
    calculate_hash,
    get_supported_algorithms
)

from hashing.hmac_tools import (
    calculate_hmac,
    get_supported_hmac_algorithms
)

from hashing.password_hashing import (
    hash_password_pbkdf2,
    verify_password_pbkdf2,
    hash_password_scrypt,
    verify_password_scrypt,
    hash_password_argon2,
    verify_password_argon2
)

# bcrypt
from hashing.bcrypt_hash import (
    hash_password as hash_password_bcrypt,
    verify_password as verify_password_bcrypt
)


# =========================================================
# HASH CRACKING
# =========================================================

from cracking.dictionary import dictionary_attack

from cracking.brute_force import (
    brute_force_attack,
    get_character_sets
)


# =========================================================
# CLASSICAL ENCRYPTION
# =========================================================

from encryption.Classical.caesar import (
    caesar_encrypt,
    caesar_decrypt
)

from encryption.Classical.rot13 import rot13

from encryption.Classical.linear_substitution import (
    encrypt as linear_encrypt,
    decrypt as linear_decrypt
)

from encryption.Classical.monoalphabetic import (
    encrypt as mono_encrypt,
    decrypt as mono_decrypt,
    generate_key as generate_mono_key
)

from encryption.Classical.playfair import (
    encrypt as playfair_encrypt,
    decrypt as playfair_decrypt,
    display_matrix
)

from encryption.Classical.vigenere import (
    encrypt as vigenere_encrypt,
    decrypt as vigenere_decrypt
)

from encryption.Classical.autokey import (
    encrypt as autokey_encrypt,
    decrypt as autokey_decrypt
)

from encryption.Classical.one_time_pad import (
    encrypt as otp_encrypt,
    decrypt as otp_decrypt,
    generate_key as generate_otp_key
)

from encryption.Classical.transposition import (
    encrypt as transposition_encrypt,
    decrypt as transposition_decrypt
)


# =========================================================
# SYMMETRIC ENCRYPTION
# =========================================================

from encryption.Symmetric.des import (
    encrypt as des_encrypt,
    decrypt as des_decrypt,
    generate_key as generate_des_key
)

from encryption.Symmetric.aes import (
    encrypt as aes_encrypt,
    decrypt as aes_decrypt,
    generate_key as generate_aes_key
)


# =========================================================
# ASYMMETRIC ENCRYPTION
# =========================================================

from encryption.Asymmetric.rsa import (
    generate_keys as rsa_generate_keys,
    encrypt as rsa_encrypt,
    decrypt as rsa_decrypt
)


# =========================================================
# ENCODING / DECODING
# =========================================================

from encoding.base64_tools import (
    encode as base64_encode,
    decode as base64_decode
)

from encoding.base32_tools import (
    encode as base32_encode,
    decode as base32_decode
)

from encoding.hex_tools import (
    encode as hex_encode,
    decode as hex_decode
)

from encoding.url_tools import (
    encode as url_encode,
    decode as url_decode
)

from encoding.ascii_tools import (
    encode as ascii_encode,
    decode as ascii_decode
)

from encoding.binary_tools import (
    encode as binary_encode,
    decode as binary_decode
)

from encoding.html_tools import (
    encode as html_encode,
    decode as html_decode
)


# =========================================================
# PASSWORD GENERATOR
# =========================================================

from Password_generator import password_generator


# =========================================================
# STANDARD LIBRARY
# =========================================================

import base64


# =========================================================
# MAIN MENU
# =========================================================

def show_main_menu():

    print("""
╔══════════════════════════════════════════╗
║        AbdelatefOsama TOOLKIT            ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Encryption / Decryption             ║
║  [2] Encoding / Decoding                 ║
║  [3] Hashing                             ║
║  [4] Hash Cracking                       ║
║  [5] Password Generator                  ║
║  [6] File Integrity                      ║
║  [7] About                               ║
║  [0] Exit                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# ENCRYPTION MAIN MENU
# =========================================================

def show_encryption_menu():

    print("""
╔══════════════════════════════════════════╗
║          ENCRYPTION / DECRYPTION         ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Classical Cryptography              ║
║  [2] Symmetric Cryptography              ║
║  [3] Asymmetric Cryptography             ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# CLASSICAL MENU
# =========================================================

def show_classical_menu():

    print("""
╔══════════════════════════════════════════╗
║         CLASSICAL CRYPTOGRAPHY           ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Caesar                              ║
║  [2] ROT13                               ║
║  [3] Linear Substitution                 ║
║  [4] Monoalphabetic                      ║
║  [5] Playfair                            ║
║  [6] Vigenère                            ║
║  [7] AutoKey                             ║
║  [8] One-Time Pad                        ║
║  [9] Transposition                       ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# SYMMETRIC MENU
# =========================================================

def show_symmetric_menu():

    print("""
╔══════════════════════════════════════════╗
║          SYMMETRIC CRYPTOGRAPHY          ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] DES                                 ║
║  [2] AES                                 ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# ASYMMETRIC MENU
# =========================================================

def show_asymmetric_menu():

    print("""
╔══════════════════════════════════════════╗
║         ASYMMETRIC CRYPTOGRAPHY          ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] RSA                                 ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# OPERATION MENU
# =========================================================

def show_operation_menu():

    print("""
╔══════════════════════════════════════════╗
║              OPERATION                   ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Encrypt                             ║
║  [2] Decrypt                             ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# ENCODING MENU
# =========================================================

def show_encoding_menu():

    print("""
╔══════════════════════════════════════════╗
║           ENCODING / DECODING            ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Base64                              ║
║  [2] Base32                              ║
║  [3] Hex                                 ║
║  [4] URL                                 ║
║  [5] ASCII                               ║
║  [6] Binary                              ║
║  [7] HTML                                ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# ENCODING OPERATION MENU
# =========================================================

def show_encoding_operation_menu():

    print("""
╔══════════════════════════════════════════╗
║          ENCODING OPERATION              ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Encode                              ║
║  [2] Decode                              ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# GENERIC ENCODING MENU
# =========================================================

def encoding_operation_menu(
    encode_function,
    decode_function,
    encoding_name
):

    show_encoding_operation_menu()

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    try:

        if choice == "1":

            text = input(
                "\nEnter text: "
            )

            result = encode_function(text)

            print("\n" + "=" * 60)
            print(f"[+] {encoding_name} Encoding Successful")
            print("=" * 60)
            print("\nEncoded:")
            print(result)
            print("=" * 60)

        else:

            encoded_text = input(
                f"\nEnter {encoding_name} encoded data: "
            )

            result = decode_function(encoded_text)

            print("\n" + "=" * 60)
            print(f"[+] {encoding_name} Decoding Successful")
            print("=" * 60)
            print("\nDecoded:")
            print(result)
            print("=" * 60)

    except Exception as error:

        print(
            f"\n[-] {encoding_name} operation failed: {error}"
        )


# =========================================================
# ENCODING / DECODING MENU
# =========================================================

def encoding_menu():

    while True:

        show_encoding_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            encoding_operation_menu(
                base64_encode,
                base64_decode,
                "Base64"
            )

        elif choice == "2":

            encoding_operation_menu(
                base32_encode,
                base32_decode,
                "Base32"
            )

        elif choice == "3":

            encoding_operation_menu(
                hex_encode,
                hex_decode,
                "Hex"
            )

        elif choice == "4":

            encoding_operation_menu(
                url_encode,
                url_decode,
                "URL"
            )

        elif choice == "5":

            encoding_operation_menu(
                ascii_encode,
                ascii_decode,
                "ASCII"
            )

        elif choice == "6":

            encoding_operation_menu(
                binary_encode,
                binary_decode,
                "Binary"
            )

        elif choice == "7":

            encoding_operation_menu(
                html_encode,
                html_decode,
                "HTML"
            )

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# PASSWORD GENERATOR MENU
# =========================================================

def password_generator_menu():

    print("\n" + "=" * 60)
    print("PASSWORD GENERATOR")
    print("=" * 60)

    try:

        length = int(
            input("\nEnter password length: ").strip()
        )

        if length < 4:

            print(
                "[-] Password length must be at least 4."
            )

            return

        print("\nCharacter Types")
        print("-" * 30)

        uppercase = (
            input(
                "Include uppercase letters? (y/n): "
            ).strip().lower() == "y"
        )

        lowercase = (
            input(
                "Include lowercase letters? (y/n): "
            ).strip().lower() == "y"
        )

        digits = (
            input(
                "Include digits? (y/n): "
            ).strip().lower() == "y"
        )

        special = (
            input(
                "Include special characters? (y/n): "
            ).strip().lower() == "y"
        )

        if not any([
            uppercase,
            lowercase,
            digits,
            special
        ]):

            print(
                "\n[-] You must select at least "
                "one character type."
            )

            return

        count = int(
            input(
                "\nHow many passwords to generate? "
            ).strip()
        )

        if count < 1:

            print(
                "[-] Number of passwords must be at least 1."
            )

            return

        print("\n" + "=" * 60)
        print("[+] Generated Passwords")
        print("=" * 60)

        for index in range(1, count + 1):

            password = password_generator.generate_password(
                length=length,
                use_uppercase=uppercase,
                use_lowercase=lowercase,
                use_digits=digits,
                use_special=special
            )

            print(
                f"{index:02d}. {password}"
            )

        print("=" * 60)

        print(
            "\n[!] Passwords are generated using "
            "a cryptographically secure random source."
        )

    except ValueError as error:

        print(
            f"\n[-] Invalid input: {error}"
        )

    except Exception as error:

        print(
            f"\n[-] Password generation failed: {error}"
        )


# =========================================================
# CAESAR
# =========================================================

def caesar_menu():

    show_operation_menu()

    choice = input("Choose operation: ").strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    try:

        text = input("\nEnter text: ")

        shift = int(
            input("Enter shift value: ").strip()
        )

        if choice == "1":

            result = caesar_encrypt(text, shift)

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = caesar_decrypt(text, shift)

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError:

        print("[-] Shift must be a number.")


# =========================================================
# ROT13
# =========================================================

def rot13_menu():

    text = input("\nEnter text: ")

    result = rot13(text)

    print("\n[+] Result:")
    print(result)


# =========================================================
# LINEAR SUBSTITUTION
# =========================================================

def linear_substitution_menu():

    show_operation_menu()

    choice = input("Choose operation: ").strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    print("\nExample key:")
    print("QWERTYUIOPASDFGHJKLZXCVBNM")

    key = input("\nEnter 26-letter key: ")

    text = input("Enter text: ")

    try:

        if choice == "1":

            result = linear_encrypt(text, key)

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = linear_decrypt(text, key)

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# MONOALPHABETIC
# =========================================================

def monoalphabetic_menu():

    print("""
[1] Generate Random Key
[2] Enter Key Manually
[0] Back
""")

    key_choice = input(
        "Choose key option: "
    ).strip()

    if key_choice == "0":
        return

    if key_choice == "1":

        key = generate_mono_key()

        print("\n[+] Generated Key:")
        print(key)

    elif key_choice == "2":

        key = input(
            "\nEnter 26-letter key: "
        )

    else:

        print("[-] Invalid option.")
        return

    show_operation_menu()

    operation = input(
        "Choose operation: "
    ).strip()

    if operation == "0":
        return

    if operation not in ("1", "2"):
        print("[-] Invalid option.")
        return

    text = input("\nEnter text: ")

    try:

        if operation == "1":

            result = mono_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = mono_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# PLAYFAIR
# =========================================================

def playfair_menu():

    show_operation_menu()

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    key = input(
        "\nEnter Playfair key: "
    )

    try:

        print("\n[+] Playfair Matrix:\n")

        display_matrix(key)

        text = input("\nEnter text: ")

        if choice == "1":

            result = playfair_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = playfair_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# VIGENERE
# =========================================================

def vigenere_menu():

    show_operation_menu()

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    key = input(
        "\nEnter Vigenère key: "
    )

    text = input(
        "Enter text: "
    )

    try:

        if choice == "1":

            result = vigenere_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = vigenere_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# AUTOKEY
# =========================================================

def autokey_menu():

    show_operation_menu()

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    key = input(
        "\nEnter initial key: "
    )

    text = input(
        "Enter text: "
    )

    try:

        if choice == "1":

            result = autokey_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = autokey_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# ONE-TIME PAD
# =========================================================

def otp_menu():

    print("""
[1] Generate Random Key
[2] Enter Existing Key
[0] Back
""")

    choice = input(
        "Choose key option: "
    ).strip()

    if choice == "0":
        return

    text = input(
        "\nEnter text: "
    )

    if choice == "1":

        letters_count = sum(
            1 for char in text
            if char.isalpha()
        )

        if letters_count == 0:

            print(
                "[-] Text must contain letters."
            )

            return

        key = generate_otp_key(
            letters_count
        )

        print("\n[+] Generated OTP Key:")
        print(key)

    elif choice == "2":

        key = input(
            "\nEnter OTP key: "
        )

    else:

        print("[-] Invalid option.")
        return

    show_operation_menu()

    operation = input(
        "Choose operation: "
    ).strip()

    if operation == "0":
        return

    if operation not in ("1", "2"):
        print("[-] Invalid option.")
        return

    try:

        if operation == "1":

            result = otp_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = otp_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# TRANSPOSITION
# =========================================================

def transposition_menu():

    show_operation_menu()

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):
        print("[-] Invalid option.")
        return

    key = input(
        "\nEnter transposition key: "
    )

    text = input(
        "Enter text: "
    )

    try:

        if choice == "1":

            result = transposition_encrypt(
                text,
                key
            )

            print("\n[+] Encrypted Text:")
            print(result)

        else:

            result = transposition_decrypt(
                text,
                key
            )

            print("\n[+] Decrypted Text:")
            print(result)

    except ValueError as error:

        print(f"[-] {error}")


# =========================================================
# CLASSICAL CRYPTOGRAPHY MENU
# =========================================================

def classical_encryption_menu():

    while True:

        show_classical_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            caesar_menu()

        elif choice == "2":

            rot13_menu()

        elif choice == "3":

            linear_substitution_menu()

        elif choice == "4":

            monoalphabetic_menu()

        elif choice == "5":

            playfair_menu()

        elif choice == "6":

            vigenere_menu()

        elif choice == "7":

            autokey_menu()

        elif choice == "8":

            otp_menu()

        elif choice == "9":

            transposition_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# DES
# =========================================================

def des_menu():

    print("""
[1] Encrypt
[2] Decrypt
[0] Back
""")

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice == "1":

        plaintext = input(
            "\nEnter plaintext: "
        )

        key = generate_des_key()

        try:

            ciphertext = des_encrypt(
                plaintext,
                key
            )

            key_b64 = base64.b64encode(
                key
            ).decode("utf-8")

            print("\n" + "=" * 60)
            print("[+] DES Encryption Successful")
            print("=" * 60)
            print(f"Key       : {key_b64}")
            print(f"Ciphertext: {ciphertext}")
            print("=" * 60)

            print(
                "\n[!] Save the key. "
                "You need it for decryption."
            )

        except Exception as error:

            print(
                f"[-] Encryption failed: {error}"
            )

    elif choice == "2":

        ciphertext = input(
            "\nEnter ciphertext: "
        )

        key_b64 = input(
            "Enter Base64 DES key: "
        ).strip()

        try:

            key = base64.b64decode(
                key_b64
            )

            plaintext = des_decrypt(
                ciphertext,
                key
            )

            print("\n[+] Decrypted Text:")
            print(plaintext)

        except Exception as error:

            print(
                f"[-] Decryption failed: {error}"
            )

    else:

        print("[-] Invalid option.")


# =========================================================
# AES
# =========================================================

def aes_menu():

    print("""
[1] Encrypt
[2] Decrypt
[0] Back
""")

    choice = input(
        "Choose operation: "
    ).strip()

    if choice == "0":
        return

    if choice == "1":

        plaintext = input(
            "\nEnter plaintext: "
        )

        key = generate_aes_key()

        try:

            ciphertext = aes_encrypt(
                plaintext,
                key
            )

            key_b64 = base64.b64encode(
                key
            ).decode("utf-8")

            print("\n" + "=" * 60)
            print("[+] AES-256 Encryption Successful")
            print("=" * 60)
            print(f"Key       : {key_b64}")
            print(f"Ciphertext: {ciphertext}")
            print("=" * 60)

            print(
                "\n[!] Save the key. "
                "You need it for decryption."
            )

        except Exception as error:

            print(
                f"[-] Encryption failed: {error}"
            )

    elif choice == "2":

        ciphertext = input(
            "\nEnter ciphertext: "
        )

        key_b64 = input(
            "Enter Base64 AES key: "
        ).strip()

        try:

            key = base64.b64decode(
                key_b64
            )

            plaintext = aes_decrypt(
                ciphertext,
                key
            )

            print("\n[+] Decrypted Text:")
            print(plaintext)

        except Exception as error:

            print(
                f"[-] Decryption failed: {error}"
            )

    else:

        print("[-] Invalid option.")


# =========================================================
# SYMMETRIC CRYPTOGRAPHY MENU
# =========================================================

def symmetric_encryption_menu():

    while True:

        show_symmetric_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            des_menu()

        elif choice == "2":

            aes_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# RSA
# =========================================================

def rsa_menu():

    print("""
╔══════════════════════════════════════════╗
║                  RSA                     ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Generate Keys + Encrypt             ║
║  [2] Generate Keys + Decrypt              ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")

    choice = input(
        "Choose an option: "
    ).strip()

    if choice == "0":
        return

    if choice not in ("1", "2"):

        print("[-] Invalid option.")
        return

    try:

        private_key, public_key = rsa_generate_keys(
            key_size=2048
        )

        print(
            "\n[+] RSA 2048-bit key pair generated."
        )

        if choice == "1":

            plaintext = input(
                "\nEnter plaintext: "
            )

            ciphertext = rsa_encrypt(
                plaintext,
                public_key
            )

            print("\n" + "=" * 60)
            print("[+] RSA Encryption Successful")
            print("=" * 60)

            print("\nPublic Key:")
            print(public_key.decode("utf-8"))

            print("\nPrivate Key:")
            print(private_key.decode("utf-8"))

            print("\nCiphertext:")
            print(ciphertext)

            print("=" * 60)

            print(
                "\n[!] Save the private key securely."
            )

        else:

            ciphertext = input(
                "\nEnter Base64 RSA ciphertext: "
            )

            plaintext = rsa_decrypt(
                ciphertext,
                private_key
            )

            print("\n" + "=" * 60)
            print("[+] RSA Decryption Successful")
            print("=" * 60)

            print("\nDecrypted Text:")
            print(plaintext)

            print("=" * 60)

            print(
                "\n[!] A new key pair was generated "
                "for this operation."
            )

    except Exception as error:

        print(
            f"\n[-] RSA operation failed: {error}"
        )


# =========================================================
# ASYMMETRIC CRYPTOGRAPHY MENU
# =========================================================

def asymmetric_encryption_menu():

    while True:

        show_asymmetric_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            rsa_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# ENCRYPTION MENU
# =========================================================

def encryption_menu():

    while True:

        show_encryption_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            classical_encryption_menu()

        elif choice == "2":

            symmetric_encryption_menu()

        elif choice == "3":

            asymmetric_encryption_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# HASHING MENU
# =========================================================

def show_hash_menu():

    print("""
╔══════════════════════════════════════════╗
║                  HASHING                 ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Standard Hash                       ║
║  [2] HMAC                                ║
║  [3] Password Hashing                    ║
║  [4] File Hash                           ║
║  [5] Compare Hashes                      ║
║  [6] Hash Identifier                     ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# PASSWORD HASHING MENU
# =========================================================

def show_password_hashing_menu():

    print("""
╔══════════════════════════════════════════╗
║             PASSWORD HASHING             ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] PBKDF2                              ║
║  [2] scrypt                              ║
║  [3] Argon2                              ║
║  [4] bcrypt                              ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# HASH CRACKING MENU
# =========================================================

def show_hash_cracking_menu():

    print("""
╔══════════════════════════════════════════╗
║              HASH CRACKING               ║
╠══════════════════════════════════════════╣
║                                          ║
║  [1] Dictionary Attack                   ║
║  [2] Brute Force                         ║
║  [0] Back                                ║
║                                          ║
╚══════════════════════════════════════════╝
""")


# =========================================================
# STANDARD HASH
# =========================================================

def standard_hash_menu():

    algorithms = get_supported_algorithms()

    print("\nAvailable Algorithms:\n")

    for index, algorithm in enumerate(
        algorithms,
        start=1
    ):

        print(
            f"[{index}] {algorithm}"
        )

    print("[0] Back")

    choice = input(
        "\nChoose algorithm: "
    ).strip()

    if choice == "0":
        return

    try:

        choice = int(choice)

        if choice < 1 or choice > len(algorithms):

            print("[-] Invalid choice.")
            return

        algorithm = algorithms[
            choice - 1
        ]

        text = input(
            "\nEnter text to hash: "
        )

        result = calculate_hash(
            text,
            algorithm
        )

        print("\n" + "=" * 60)
        print(f"Algorithm : {algorithm}")
        print(f"Input     : {text}")
        print(f"Hash      : {result}")
        print("=" * 60)

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )


# =========================================================
# HMAC
# =========================================================

def hmac_menu():

    algorithms = get_supported_hmac_algorithms()

    print("\nAvailable HMAC Algorithms:\n")

    for index, algorithm in enumerate(
        algorithms,
        start=1
    ):

        print(
            f"[{index}] HMAC-{algorithm.upper()}"
        )

    print("[0] Back")

    choice = input(
        "\nChoose algorithm: "
    ).strip()

    if choice == "0":
        return

    try:

        choice = int(choice)

        if choice < 1 or choice > len(algorithms):

            print("[-] Invalid choice.")
            return

        algorithm = algorithms[
            choice - 1
        ]

        message = input(
            "\nEnter message: "
        )

        secret_key = input(
            "Enter secret key: "
        )

        result = calculate_hmac(
            message,
            secret_key,
            algorithm
        )

        print("\n" + "=" * 60)
        print(
            f"Algorithm : HMAC-{algorithm.upper()}"
        )
        print(f"Message   : {message}")
        print(f"HMAC      : {result}")
        print("=" * 60)

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )


# =========================================================
# FILE HASH
# =========================================================

def file_hash_menu():

    algorithms = get_supported_algorithms()

    print("\nAvailable File Hash Algorithms:\n")

    for index, algorithm in enumerate(
        algorithms,
        start=1
    ):

        print(
            f"[{index}] {algorithm}"
        )

    print("[0] Back")

    choice = input(
        "\nChoose algorithm: "
    ).strip()

    if choice == "0":
        return

    try:

        choice = int(choice)

        if choice < 1 or choice > len(algorithms):

            print("[-] Invalid choice.")
            return

        algorithm = algorithms[
            choice - 1
        ]

        file_path = input(
            "\nEnter file path: "
        ).strip().strip('"')

        if not file_path:

            print(
                "[-] File path cannot be empty."
            )

            return

        result = calculate_file_hash(
            file_path,
            algorithm
        )

        print("\n" + "=" * 70)
        print(f"Algorithm : {algorithm}")
        print(f"File      : {file_path}")
        print(f"Hash      : {result}")
        print("=" * 70)

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )

    except FileNotFoundError as error:

        print(f"[-] {error}")

    except PermissionError as error:

        print(f"[-] {error}")


# =========================================================
# COMPARE HASHES
# =========================================================

def compare_hashes_menu():

    print("\n" + "=" * 60)
    print("HASH COMPARISON")
    print("=" * 60)

    hash1 = input(
        "\nEnter first hash: "
    ).strip()

    hash2 = input(
        "Enter second hash: "
    ).strip()

    if not hash1 or not hash2:

        print(
            "\n[-] Hash values cannot be empty."
        )

        return

    if compare_hashes(
        hash1,
        hash2
    ):

        print("\n[+] Hashes match.")
        print("[+] The values are identical.")

    else:

        print("\n[-] Hashes do not match.")
        print("[-] The values are different.")

    print("=" * 60)


# =========================================================
# HASH IDENTIFIER
# =========================================================

def hash_identifier_menu():

    print("\n" + "=" * 60)
    print("HASH IDENTIFIER")
    print("=" * 60)

    hash_value = input(
        "\nEnter hash: "
    ).strip()

    if not hash_value:

        print("\n[-] Hash cannot be empty.")
        return

    possible_types = identify_hash(
        hash_value
    )

    print("\n" + "=" * 60)

    if possible_types:

        print("Possible Hash Types:\n")

        for hash_type in possible_types:

            print(
                f"[+] {hash_type}"
            )

        print(
            "\n[!] Identification is heuristic, "
            "not guaranteed."
        )

    else:

        print(
            "[-] Unable to identify the hash."
        )

        print(
            "[-] Unsupported format or hash length."
        )

    print("=" * 60)


# =========================================================
# PASSWORD VERIFICATION
# =========================================================

def password_verification_menu(
    hash_function,
    verify_function,
    algorithm_name
):

    print("\n" + "=" * 60)
    print(
        f"{algorithm_name} PASSWORD HASHING"
    )
    print("=" * 60)

    password = input(
        "\nEnter password: "
    )

    if not password:

        print(
            "[-] Password cannot be empty."
        )

        return

    try:

        hashed_password = hash_function(
            password
        )

        print("\nGenerated Password Hash:")
        print(hashed_password)

        print("\n" + "-" * 60)

        verify_password = input(
            "Enter password to verify: "
        )

        if verify_function(
            verify_password,
            hashed_password
        ):

            print(
                "\n[+] Password verification successful."
            )

            print(
                "[+] Password matches the stored hash."
            )

        else:

            print(
                "\n[-] Password verification failed."
            )

            print(
                "[-] Password does not match the stored hash."
            )

    except Exception as error:

        print(
            f"\n[-] Password hashing/verification failed: {error}"
        )

    print("=" * 60)


# =========================================================
# PASSWORD HASHING MENU
# =========================================================

def password_hashing_menu():

    while True:

        show_password_hashing_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            password_verification_menu(
                hash_password_pbkdf2,
                verify_password_pbkdf2,
                "PBKDF2"
            )

        elif choice == "2":

            password_verification_menu(
                hash_password_scrypt,
                verify_password_scrypt,
                "scrypt"
            )

        elif choice == "3":

            password_verification_menu(
                hash_password_argon2,
                verify_password_argon2,
                "Argon2"
            )

        elif choice == "4":

            password_verification_menu(
                hash_password_bcrypt,
                verify_password_bcrypt,
                "bcrypt"
            )

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# DICTIONARY ATTACK
# =========================================================

def dictionary_attack_menu():

    print("\n" + "=" * 60)
    print("DICTIONARY ATTACK")
    print("=" * 60)

    algorithms = get_supported_algorithms()

    print("\nAvailable Algorithms:\n")

    for index, algorithm in enumerate(
        algorithms,
        start=1
    ):

        print(
            f"[{index}] {algorithm}"
        )

    print("[0] Back")

    choice = input(
        "\nChoose algorithm: "
    ).strip()

    if choice == "0":
        return

    try:

        choice = int(choice)

        if choice < 1 or choice > len(algorithms):

            print("[-] Invalid choice.")
            return

        algorithm = algorithms[
            choice - 1
        ]

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )

        return

    target_hash = input(
        "\nEnter target hash: "
    ).strip()

    if not target_hash:

        print(
            "[-] Hash cannot be empty."
        )

        return

    wordlist_path = input(
        "Enter wordlist path: "
    ).strip().strip('"')

    if not wordlist_path:

        print(
            "[-] Wordlist path cannot be empty."
        )

        return

    print("\n" + "-" * 60)
    print(
        "[*] Starting Dictionary Attack..."
    )
    print(
        f"[*] Algorithm : {algorithm}"
    )
    print(
        f"[*] Wordlist  : {wordlist_path}"
    )
    print("-" * 60)

    try:

        result = dictionary_attack(
            target_hash,
            wordlist_path,
            algorithm
        )

        print("\n" + "=" * 60)

        if result["found"]:

            print("[+] PASSWORD FOUND!")

            print(
                f"[+] Password : "
                f"{result['password']}"
            )

        else:

            print(
                "[-] Password not found."
            )

        print(
            f"[*] Attempts  : "
            f"{result['attempts']}"
        )

        print(
            f"[*] Time      : "
            f"{result['time']:.4f} seconds"
        )

        print("=" * 60)

    except FileNotFoundError as error:

        print(f"\n[-] {error}")

    except PermissionError as error:

        print(f"\n[-] {error}")

    except ValueError as error:

        print(f"\n[-] {error}")


# =========================================================
# BRUTE FORCE
# =========================================================

def brute_force_menu():

    print("\n" + "=" * 60)
    print("BRUTE FORCE ATTACK")
    print("=" * 60)

    algorithms = get_supported_algorithms()

    print("\nAvailable Algorithms:\n")

    for index, algorithm in enumerate(
        algorithms,
        start=1
    ):

        print(
            f"[{index}] {algorithm}"
        )

    print("[0] Back")

    choice = input(
        "\nChoose algorithm: "
    ).strip()

    if choice == "0":
        return

    try:

        choice = int(choice)

        if choice < 1 or choice > len(algorithms):

            print("[-] Invalid choice.")
            return

        algorithm = algorithms[
            choice - 1
        ]

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )

        return

    target_hash = input(
        "\nEnter target hash: "
    ).strip()

    if not target_hash:

        print(
            "[-] Hash cannot be empty."
        )

        return

    character_sets = get_character_sets()

    print("\nAvailable Character Sets:\n")

    for index, character_set in enumerate(
        character_sets,
        start=1
    ):

        print(
            f"[{index}] {character_set}"
        )

    print("[0] Back")

    charset_choice = input(
        "\nChoose character set: "
    ).strip()

    if charset_choice == "0":
        return

    try:

        charset_choice = int(
            charset_choice
        )

        if (
            charset_choice < 1
            or charset_choice > len(character_sets)
        ):

            print("[-] Invalid choice.")
            return

        charset = character_sets[
            charset_choice - 1
        ]

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )

        return

    max_length_input = input(
        "\nEnter maximum password length: "
    ).strip()

    try:

        max_length = int(
            max_length_input
        )

        if max_length < 1:

            print(
                "[-] Length must be at least 1."
            )

            return

    except ValueError:

        print(
            "[-] Please enter a valid number."
        )

        return

    print("\n" + "-" * 60)
    print(
        "[*] Starting Brute Force Attack..."
    )
    print(
        f"[*] Algorithm    : {algorithm}"
    )
    print(
        f"[*] Character Set: {charset}"
    )
    print(
        f"[*] Max Length   : {max_length}"
    )
    print("-" * 60)

    try:

        result = brute_force_attack(
            target_hash,
            algorithm,
            max_length,
            charset
        )

        print("\n" + "=" * 60)

        if result["found"]:

            print("[+] PASSWORD FOUND!")

            print(
                f"[+] Password : "
                f"{result['password']}"
            )

        else:

            print(
                "[-] Password not found."
            )

        print(
            f"[*] Attempts  : "
            f"{result['attempts']}"
        )

        print(
            f"[*] Time      : "
            f"{result['time']:.4f} seconds"
        )

        print("=" * 60)

    except ValueError as error:

        print(f"\n[-] {error}")


# =========================================================
# HASH CRACKING MENU
# =========================================================

def hash_cracking_menu():

    while True:

        show_hash_cracking_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            dictionary_attack_menu()

        elif choice == "2":

            brute_force_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# HASHING MENU
# =========================================================

def hashing_menu():

    while True:

        show_hash_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            standard_hash_menu()

        elif choice == "2":

            hmac_menu()

        elif choice == "3":

            password_hashing_menu()

        elif choice == "4":

            file_hash_menu()

        elif choice == "5":

            compare_hashes_menu()

        elif choice == "6":

            hash_identifier_menu()

        elif choice == "0":

            break

        else:

            print("[-] Invalid option.")


# =========================================================
# ABOUT
# =========================================================

def about_menu():

    print("\n" + "=" * 60)
    print("CYBER SECURITY TOOLKIT")
    print("=" * 60)

    print(
        "[+] Educational Cybersecurity Utility"
    )

    print("[+] Version: 1.0")

    print("\n[+] Encryption / Decryption")

    print("    Classical Cryptography:")
    print("      - Caesar")
    print("      - ROT13")
    print("      - Linear Substitution")
    print("      - Monoalphabetic")
    print("      - Playfair")
    print("      - Vigenère")
    print("      - AutoKey")
    print("      - One-Time Pad")
    print("      - Transposition")

    print("\n    Symmetric Cryptography:")
    print("      - DES")
    print("      - AES")

    print("\n    Asymmetric Cryptography:")
    print("      - RSA")

    print("\n[+] Encoding / Decoding")
    print("      - Base64")
    print("      - Base32")
    print("      - Hex")
    print("      - URL")
    print("      - ASCII")
    print("      - Binary")
    print("      - HTML")

    print("\n[+] Hashing")
    print("    - Standard Hashing")
    print("    - HMAC")
    print("    - Password Hashing")
    print("      * PBKDF2")
    print("      * scrypt")
    print("      * Argon2")
    print("      * bcrypt")
    print("    - File Hashing")
    print("    - Hash Comparison")
    print("    - Hash Identifier")

    print("\n[+] Hash Cracking")
    print("    - Dictionary Attack")
    print("    - Brute Force")

    print("\n[+] Password Security")
    print("    - Cryptographically Secure Password Generator")

    print("\n[+] File Integrity")
    print("    - Currently under development")

    print("\n[!] Educational use only.")

    print("=" * 60)


# =========================================================
# MAIN
# =========================================================

def main():

    while True:

        show_main_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        # -------------------------------------------------
        # Encryption
        # -------------------------------------------------

        if choice == "1":

            encryption_menu()

        # -------------------------------------------------
        # Encoding
        # -------------------------------------------------

        elif choice == "2":

            encoding_menu()

        # -------------------------------------------------
        # Hashing
        # -------------------------------------------------

        elif choice == "3":

            hashing_menu()

        # -------------------------------------------------
        # Hash Cracking
        # -------------------------------------------------

        elif choice == "4":

            hash_cracking_menu()

        # -------------------------------------------------
        # Password Generator
        # -------------------------------------------------

        elif choice == "5":

            password_generator_menu()

        # -------------------------------------------------
        # File Integrity
        # -------------------------------------------------

        elif choice == "6":

            print("\n" + "=" * 60)
            print("FILE INTEGRITY")
            print("=" * 60)

            print(
                "[!] File Integrity module is "
                "currently under development."
            )

            print("=" * 60)

        # -------------------------------------------------
        # About
        # -------------------------------------------------

        elif choice == "7":

            about_menu()

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        elif choice == "0":

            print("\n[+] Goodbye!")

            break

        # -------------------------------------------------
        # Invalid
        # -------------------------------------------------

        else:

            print("\n[-] Invalid option.")


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
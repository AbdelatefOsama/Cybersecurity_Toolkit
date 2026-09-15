import secrets
import string


def generate_password(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True
):
    """
    Generate a cryptographically secure random password.
    """

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_digits:
        character_sets.append(string.digits)

    if use_special:
        character_sets.append("!@#$%^&*()-_=+[]{};:,.<>?")

    if not character_sets:
        raise ValueError("At least one character set must be selected.")

    if length < len(character_sets):
        raise ValueError(
            f"Password length must be at least {len(character_sets)} "
            "to include all selected character types."
        )

    # Guarantee at least one character from each selected category
    password = [
        secrets.choice(character_set)
        for character_set in character_sets
    ]

    # Combine all selected character sets
    all_characters = "".join(character_sets)

    # Fill the remaining characters
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
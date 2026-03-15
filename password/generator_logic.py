import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """
    Generates a random password based on user constraints.
    """
    if length < 4:
        return "Error: Length too short (min 4)"

    # Define character sets
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not char_pool:
        return "Error: Select at least one character type"

    # Ensure at least one character from each selected category is included
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))

    # Fill the rest of the password length with random choices from the pool
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))

    # Shuffle the list to prevent predictable patterns (e.g., always starting with uppercase)
    random.shuffle(password)

    # Convert list back to string
    return "".join(password)

def check_strength(password):
    """
    Simple logic to rate password strength.
    """
    score = 0
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 1

    if score <= 2: return "Weak"
    if score <= 4: return "Medium"
    return "Strong"
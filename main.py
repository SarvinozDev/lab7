import random
import string

def create_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def check_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()-_=+" for c in password)

    if len(password) < 6:
        return "Zaif"
    elif len(password) >= 8 and has_lower and has_upper and has_digit and has_symbol:
        return "Kuchli"
    else:
        return "O‘rtacha"

# --- Asosiy qism ---
print("=== Kuchli parol generatori ===")
for i in range(5):
    pwd = create_password(12)
    strength = check_strength(pwd)
    print(f"{i+1}. {pwd}  -->  {strength}")

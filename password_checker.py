import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*()_+{}[\]:;<>,.?/~\\-]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    # Strength result
    if score == 5:
        strength = "Strong 🔐"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback


# Main program
password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for f in feedback:
        print("-", f)
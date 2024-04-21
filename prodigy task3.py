import re

def assess_password_strength(password):
    length = len(password)
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    numbers = any(c.isdigit() for c in password)
    special_characters = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))

    score = 0
    feedback = []

    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if numbers:
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_characters:
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    print("Password strength:", strength)
    if feedback:
        print("Feedback:")
        for message in feedback:
            print("-", message)

if __name__ == "__main__":
    main()

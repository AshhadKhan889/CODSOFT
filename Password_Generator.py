import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    upper_case_criteria = any(char.isupper() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    
    strength_score = sum([length_criteria, digit_criteria, upper_case_criteria, special_char_criteria])

    if strength_score == 4:
        return "Very Strong"
    elif strength_score >= 3:
        return "Strong"
    elif strength_score >= 2:
        return "Moderate"
    elif strength_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

password_length = int(input("Enter the length of the password you want to generate: "))

generated_password = generate_password(password_length)
strength = check_password_strength(generated_password)

print("Password that is generated is:", generated_password)
print("Password strength is:", strength)


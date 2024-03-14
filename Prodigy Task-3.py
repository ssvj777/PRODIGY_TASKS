import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/',
           '|', '~', '>', '*', '(', ')', '<']

def check_password_strength(password):
    complexity_meter = 0
    contains_digits = any(char in DIGITS for char in password)
    contains_lowercase = any(char in LOCASE_CHARACTERS for char in password)
    contains_uppercase = any(char in UPCASE_CHARACTERS for char in password)
    contains_symbols = any(char in SYMBOLS for char in password)

    if contains_digits:
        complexity_meter += 1
    if contains_lowercase:
        complexity_meter += 1
    if contains_uppercase:
        complexity_meter += 1
    if contains_symbols:
        complexity_meter += 1
    if len(password) > 7:
        complexity_meter += 1

    return complexity_meter

def main():
    print("-------------------------------------")
    print("Password Complexity Checker")
    print("-------------------------------------")

    password = input("Enter your Password: ")

    complexity_meter = check_password_strength(password)
    if complexity_meter == 5:
        strength = "Strong"
    elif complexity_meter >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("Password Complexity Meter:", complexity_meter, "/ 5")
    print("Password Strength:", strength)

    if complexity_meter == 5:
        print("Your Password is Extremely Strong")
    else:
        generate_password = input("Do you want to generate a Strong Password? (y/n): ")
        if generate_password.lower() == "y":
            print("Strong Password:", generate_strong_password())

def generate_strong_password():
    MAX_LEN = 12  
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    password = ''.join(random.choices(COMBINED_LIST, k=MAX_LEN))
    return password

if __name__ == "__main__":
    main()
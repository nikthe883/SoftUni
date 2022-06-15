password = input()


def long_check(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def letter_and_digit_check(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_at_least_two_digits(password):
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


validated = [long_check(password),
             letter_and_digit_check(password),
             have_at_least_two_digits(password)]
if all(validated):
    print("Password is valid")

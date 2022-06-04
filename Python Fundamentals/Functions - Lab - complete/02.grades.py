user_input = float(input())


def grade(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.5 <= grade <= 4.45:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    else:
        return "Excellent"

print(grade(user_input))

user_operator = input()
first_number = input()
second_number = input()

def calculator(a,b,operator):
    if operator == "multiply":
        operator = "*"
    elif operator == "divide":
        operator = "//"
    elif operator == "add":
        operator = "+"
    else:
        operator = "-"

    return eval(f"{a}{operator}{b}")

print(calculator(first_number, second_number, user_operator))


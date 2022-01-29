# inputs

number1 = int(input())
number2 = int(input())
operator = input()


if operator == "/" and number2 == 0 or operator == "%" and number2 == 0:
    print(f"Cannot divide {number1} by zero")
    exit()  # to exit the code cuz error division by 0 or put the bottom code in else statement

calculator = eval(f"{number1}{operator}{number2}")

even = False
if calculator % 2 == 0:
    even = True

if operator == "+" or operator == "-" or operator == "*":
    if even:
        print(f"{number1} {operator} {number2} = {calculator} - even")
    elif not even:
        print(f"{number1} {operator} {number2} = {calculator} - odd")
elif operator == "/":
    print(f"{number1} {operator} {number2} = {calculator:.2f}")
else:
    print(f"{number1} {operator} {number2} = {calculator}")

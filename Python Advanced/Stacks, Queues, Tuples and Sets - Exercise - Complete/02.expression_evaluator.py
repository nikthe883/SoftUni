from functools import reduce

user_input = input().split()

numbers = []

for i in user_input:
    if i.lstrip("-").isnumeric():
        numbers.append(int(i))
    else:
        if i == "*":
            numbers = [reduce(lambda x, y: x * y, numbers)]
        elif i == "/":
            numbers = [reduce(lambda x, y: x // y, numbers)]
        elif i == "+":
            numbers = [reduce(lambda x, y: x + y, numbers)]
        elif i == "-":
            numbers = [reduce(lambda x, y: x - y, numbers)]

print(numbers[0])

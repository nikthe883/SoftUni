expression = input()
stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        index = stack.pop()
        print(expression[index:i + 1])
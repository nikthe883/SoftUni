user_input = list(input())

stack = []

for i in range(len(user_input)):
    stack.append(user_input.pop())

print("".join(stack))


n = input().split()
stack = []

for i in range(len(n)):
    stack.append(n.pop())
print(" ".join(stack))

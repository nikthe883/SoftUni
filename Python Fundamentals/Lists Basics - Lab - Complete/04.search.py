n = int(input())
word = input()

user_inputs = []
for _ in range(n):
    user_input = input()
    user_inputs.append(user_input)

print(user_inputs)
for i in range(len(user_inputs) - 1, -1, -1):
    el = user_inputs[i]
    if word not in el:
        user_inputs.remove(el)
print(user_inputs)

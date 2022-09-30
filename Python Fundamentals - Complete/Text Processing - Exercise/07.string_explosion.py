user_input = input()

strength = 0
new_text = ""

for i in range(len(user_input)):
    if strength > 0 and user_input[i] != ">":
        strength -= 1
    elif user_input[i] == ">":
        strength += int(user_input[i + 1])
        new_text += user_input[i]
    else:
        new_text += user_input[i]

print(new_text)

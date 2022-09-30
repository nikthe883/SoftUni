user_input = input().split(", ")

command = input()

while command != "End":
    command = command.split(" - ")

    if command[0] == "Add":
        if command[1] not in user_input:

            user_input.append(command[1])

    if command[0] == "Remove":
        if command[1] in user_input:
            user_input.remove(command[1])
    if command[0] == "Bonus phone":
        old, new = command[1].split(":")
        if old in user_input:
            index_old = user_input.index(old)
            user_input.insert(index_old + 1, new)
    if command[0] == "Last":
        if command[1] in user_input:
            last_phone_index = user_input.index(command[1])
            last = user_input.pop(last_phone_index)
            user_input.append(last)
    command = input()

print(", ".join(user_input))
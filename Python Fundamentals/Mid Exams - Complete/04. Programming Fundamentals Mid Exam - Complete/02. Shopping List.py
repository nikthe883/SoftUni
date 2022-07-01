shopping_list = input().split("!")
commands = input()

while commands != "Go Shopping!":
    commands = commands.split(" ")

    if commands[0] == "Urgent":
        if commands[1] not in shopping_list:

            shopping_list.insert(0, commands[1])

    elif commands[0] == "Unnecessary":
        if commands[1] in shopping_list:
            shopping_list.remove(commands[1])

    elif commands[0] == "Correct":

        if commands[1] in shopping_list:
            get_item = shopping_list.index(commands[1])
            shopping_list[get_item] = commands[2]

    elif commands[0] == "Rearrange":
        if commands[1] in shopping_list:
            get_item = shopping_list.index(commands[1])
            removed_item = shopping_list.pop(get_item)
            shopping_list.append(removed_item)

    commands = input()

print(", ".join(shopping_list))

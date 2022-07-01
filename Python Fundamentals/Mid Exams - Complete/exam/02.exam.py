user_input = [int(x) for x in input().split(" ")]

command = input()

while command != "Finish":
    command = command.split(" ")

    if command[0] == "Add":
        user_input.append(int(command[1]))

    if command[0] == "Remove":
        if int(command[1]) in user_input:
            user_input.remove(int(command[1]))

    if command[0] == "Replace":
        if int(command[1]) in user_input:
            to_be_replace = user_input.index(int(command[1]))
            user_input[to_be_replace] = int(command[2])

    if command[0] == "Collapse":

        user_input = [x for x in user_input if x > int(command[1]) -1]



    command = input()

print(" ".join(str(x) for x in user_input))
user_input = [int(x) for x in input().split(" ")]
command = input().split(" ")

while command[0] != "end":

    if command[0] == "swap":
        user_input[int(command[1])], user_input[int(command[2])] = user_input[int(command[2])], user_input[int(command[1])]

    elif command[0] == "multiply":
        user_input[int(command[1])] = user_input[int(command[1])] * user_input[int(command[2])]

    elif command[0] == "decrease":
        user_input = [int(x) - 1 for x in user_input]

    command = input().split(" ")

print(", ".join(str(x) for x in user_input))

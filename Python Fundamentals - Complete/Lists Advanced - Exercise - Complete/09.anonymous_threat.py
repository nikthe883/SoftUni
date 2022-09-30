user_input = input().split(" ")

command = input().split(" ")

while command[0] != "3:1":

    task = command[0]
    start = int(command[1])
    end = int(command[2])
    if start < 0:
        start = 0

    if task == 'merge':

        if len(user_input) < end:
            user_input[start:] = ["".join(user_input[start:])]
        else:

            user_input[start:end+1] = ["".join(user_input[start: end+1])]

    if task == "divide":
        if 0 < end < 100:
            divider = len(user_input[start]) // end

            my_list = []
            for i in range(0, end):
                if i != (end - 1):
                    my_list.append(user_input[start][i * divider:(i + 1) * divider:])
                else:
                    my_list.append(user_input[start][i * divider:])
            user_input[start:start + 1] = my_list

    command = input().split(" ")

print(" ".join(user_input))

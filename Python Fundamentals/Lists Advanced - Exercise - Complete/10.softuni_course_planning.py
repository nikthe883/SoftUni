schedule = input().split(", ")
user_input = input().split(":")

while user_input[0] != "course start":

    command = user_input[0]
    if command == "Add":
        if user_input[1] not in schedule:
            schedule.append(user_input[1])
    elif command == "Insert":
        if user_input[1] not in schedule:
            schedule.insert(int(user_input[2]), user_input[1])
    elif command == "Remove":
        if user_input[1] in schedule:
            schedule.remove(user_input[1])
    elif command == "Swap":
        if user_input[1] in schedule and user_input[2] in schedule:
            swap1, swap2 = schedule.index(user_input[1]), schedule.index(user_input[2])

            schedule[swap1], schedule[swap2] = schedule[swap2], schedule[swap1]
            get_index = schedule.index(user_input[2])
            if f"{user_input[2]}-Exercise" in schedule:
                get_index_again = schedule.index(f"{user_input[2]}-Exercise")
                replace_string = schedule.pop(get_index_again)
                schedule.insert(get_index + 1, replace_string)

            get_index = schedule.index(user_input[1])


    elif command == "Exercise":
        if user_input[1] in schedule and f"{user_input[1]}-Exercise" not in schedule:

            take_index = schedule.index(user_input[1])
            schedule.insert(take_index + 1, f"{user_input[1]}-Exercise")

        elif user_input[1] not in schedule:
            schedule.append(user_input[1])
            schedule.append(f"{user_input[1]}-Exercise")

    user_input = input().split(":")

for i in range(1, len(schedule) + 1):
    print(f"{i}.{schedule[i - 1]}")

my_dict = {}
user_input = input()

while user_input != "Lumpawaroo":
    if "|" in user_input:
        user_input = user_input.split(" | ")
        is_present = False

        for value in my_dict.values():
            if user_input[1] in value:
                is_present = True
                break
        if not is_present:
            if user_input[0] not in my_dict:
                my_dict[user_input[0]] = [user_input[1]]
            else:
                my_dict[user_input[0]].append(user_input[1])

        elif user_input[1] not in user_input[0] and user_input[1] in my_dict.values():
            for key, value in my_dict.items():
                if user_input[1] in value and key != user_input[1]:
                    value.remove(user_input[0])

    elif "->" in user_input:
        user_input = user_input.split(" -> ")

        for key, value in my_dict.items():
            if user_input[0] in value:
                my_dict[key].remove(user_input[0])
                break
        if user_input[1] not in my_dict:
            my_dict[user_input[1]] = [user_input[0]]
        else:
            my_dict[user_input[1]].append(user_input[0])
        print(f"{user_input[0]} joins the {user_input[1]} side!")

    user_input = input()

for key, value in my_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}", end="\n! ")
        print("\n! ".join(value))
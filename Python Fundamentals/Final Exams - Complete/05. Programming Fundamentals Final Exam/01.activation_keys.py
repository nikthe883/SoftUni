activation_key = input()
user_input = input().split(">>>")

while user_input[0] != "Generate":

    if user_input[0] == "Contains":
        if user_input[1] in activation_key:
            print(f"{activation_key} contains {user_input[1]}")
        else:
            print("Substring not found!")

    elif user_input[0] == "Flip":
        my_list = [x for x in activation_key]

        if user_input[1] == "Upper":
            for i in range(int(user_input[2]), int(user_input[3])):
                my_list[i] = my_list[i].upper()

        elif user_input[1] == "Lower":
            for i in range(int(user_input[2]), int(user_input[3])):
                my_list[i] = my_list[i].lower()

        activation_key = "".join(my_list)
        print(activation_key)

    elif user_input[0] == "Slice":
        my_list = [x for x in activation_key]

        del my_list[int(user_input[1]): int(user_input[2])]
        activation_key = "".join(my_list)
        print(activation_key)

    user_input = input().split(">>>")

print(f"Your activation key is: {activation_key}")

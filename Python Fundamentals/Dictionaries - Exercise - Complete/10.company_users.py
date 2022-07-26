user_input = input().split(" -> ")

my_dict = {}

while user_input[0] != "End":
    if user_input[0] not in my_dict:
        my_dict[user_input[0]] = [user_input[1]]
    else:
        if user_input[1] not in my_dict[user_input[0]]:
            my_dict[user_input[0]].append(user_input[1])

    user_input = input().split(" -> ")


for k, v in my_dict.items():
    print(f"{k}")
    for item in v:
         print(f"-- {item}")



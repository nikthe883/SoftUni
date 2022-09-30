user_input = input().split("-")

my_dict = {}

while user_input[0].isdigit() != True:

    if user_input[0] not in my_dict:
        my_dict[user_input[0]] = 0
    my_dict[user_input[0]] = user_input[1]

    user_input = input().split("-")


for i in range(int(user_input[0])):
    search = input()
    if search in my_dict:
        print(f"{search} -> {my_dict[search]}")
    else:
        print(f"Contact {search} does not exist.")

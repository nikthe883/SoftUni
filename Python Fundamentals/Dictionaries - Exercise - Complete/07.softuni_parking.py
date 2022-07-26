num = int(input())
my_dict = {}
for i in range(num):
    user_input = input().split()
    if user_input[0] == "register":
        if user_input[1] not in my_dict:
            my_dict[user_input[1]] = user_input[2]
            print(f"{user_input[1]} registered {user_input[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[user_input[1]]}")
    elif user_input[0] == "unregister":
        if user_input[1] in my_dict:
            print(f"{user_input[1]} unregistered successfully")
            my_dict.pop(user_input[1], None)
        else:
            print(f"ERROR: user {user_input[1]} not found")

for k, v in my_dict.items():
    print(f"{k} => {v}")

my_dict = {}

user_input = input().split(" : ")

while user_input[0] != "end":
    if user_input[0] not in my_dict:
        my_dict[user_input[0]] = [user_input[1]]
    else:
        my_dict[user_input[0]].append(user_input[1])
    user_input = input().split(" : ")

for k, v in my_dict.items():
    print(f"{k}: {len(v)}")
    for item in v:
        print(f"-- {item}")

my_dict = {}
user_input = input().split(" ")

while user_input[0] != "buy":
    if user_input[0] not in my_dict:
        my_dict[user_input[0]] = [float(user_input[1]), int(user_input[2])]
    else:
        my_dict[user_input[0]][0] = float(user_input[1])
        my_dict[user_input[0]][1] += int(user_input[2])

    user_input = input().split(" ")

for k, v in my_dict.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")

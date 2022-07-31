n = int(input())

my_dict = {}

for _ in range(n):
    user_input = input().split("|")
    if user_input[0] not in my_dict:
        my_dict[user_input[0]] = {"composer" : user_input[1], "key" : user_input[2]}

command = input().split("|")

while command[0] != "Stop":
    if command[0] == "Add":
        if command[1] not in my_dict:
            my_dict[command[1]] = {"composer": command[2], "key": command[3]}
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")
    elif command[0] == "Remove":
        if command[1] in my_dict:
            del my_dict[command[1]]
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        if command[1] in my_dict:
            my_dict[command[1]]["key"] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    command = input().split("|")

for k in my_dict:

    print(f"{k} -> Composer: {my_dict[k]['composer']}, Key: {my_dict[k]['key']}")

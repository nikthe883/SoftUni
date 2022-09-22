commands = input().split(" ")
heroes = {}

while commands[0] != "End":
    if commands[0] == "Enroll":
        if commands[1] not in heroes:
            heroes[commands[1]] = []
        else:
            print(f"{commands[1]} is already enrolled.")
    elif commands[0] == "Learn":
        if commands[1] in heroes:
            if commands[2] not in heroes[commands[1]]:
                heroes[commands[1]].append(commands[2])
            else:
                print(f"{commands[1]} has already learnt {commands[2]}.")
        else:
            print(f"{commands[1]} doesn't exist.")
    elif commands[0] == "Unlearn":
        if commands[1] in heroes:
            if commands[2] in heroes[commands[1]]:
                heroes[commands[1]].remove(commands[2])
            else:
                print(f"{commands[1]} doesn't know {commands[2]}.")
        else:
            print(f"{commands[1]} doesn't exist.")

    commands = input().split(" ")

print("Heroes:")
for k in heroes:
    print(f"== {k}: {', '.join(heroes[k])}")

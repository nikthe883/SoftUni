command = input().split("||")

cities = {}

while command[0] != "Sail":
    if command[0] not in cities:
        cities[command[0]] = {"population": int(command[1]),
                              "gold": int(command[2])}
    else:
        cities[command[0]]["population"] += int(command[1])
        cities[command[0]]["gold"] += int(command[2])

    command = input().split("||")

action = input().split("=>")

while action[0] != "End":
    if action[0] == "Plunder":
        cities[action[1]]["population"] -= int(action[2])
        cities[action[1]]["gold"] -= int(action[3])
        print(f"{action[1]} plundered! {action[3]} gold stolen, {action[2]} citizens killed.")
        if int(cities[action[1]]["population"]) <= 0  or int(cities[action[1]]["gold"]) <= 0:
            del cities[action[1]]
            print(f"{action[1]} has been wiped off the map!")
    elif action[0] == "Prosper":
        if int(action[2]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[action[1]]["gold"] += int(action[2])
            print(f"{action[2]} gold added to the city treasury. {action[1]} now has {cities[action[1]]['gold']} gold.")

    action = input().split("=>")


if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for k in cities:
        print(f"{k} -> Population: {cities[k]['population']} citizens, Gold: {cities[k]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

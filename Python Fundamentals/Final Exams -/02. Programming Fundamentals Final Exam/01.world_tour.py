travel = input()

commands = input().split(":")

while commands[0] != "Travel":

    if commands[0] == "Add Stop":
        if 0 <= int(commands[1]) <= len(travel) - 1:
            travel = travel[:int(commands[1])] + commands[2] + travel[int(commands[1]):]
        print(travel)

    elif commands[0] == "Remove Stop":
        if 0 <= int(commands[1]) <= len(travel) - 1 and 0 <= int(commands[2]) <= len(travel) - 1:

            travel_list = [x for x in travel]
            del travel_list[int(commands[1]):int(commands[2]) + 1]

            travel = "".join(travel_list)
        print(travel)

    elif commands[0] == "Switch":
        if commands[1] in travel:

            travel = travel.replace(commands[1], commands[2])
        print(travel)

    commands = input().split(":")
print(f"Ready for world tour! Planned stops: {travel}")

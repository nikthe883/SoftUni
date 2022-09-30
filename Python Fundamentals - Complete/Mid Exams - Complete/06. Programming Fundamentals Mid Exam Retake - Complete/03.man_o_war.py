pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]

max_health_cap = int(input())
war_ship_alive = True
pirate_ship_alive = True

command = input()

while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        if 0 <= int(command[1]) < len(war_ship):
            war_ship[int(command[1])] -= int(command[2])
            if war_ship[int(command[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                war_ship_alive = False
                break
    elif command[0] == "Defend":
        if int(command[1]) >= 0 and int(command[2]) < len(pirate_ship):

            for i in range(int(command[1]), int(command[2]) + 1):
                pirate_ship[i] -= int(command[3])

                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    pirate_ship_alive = False

                    break
    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_ship):
            pirate_ship[int(command[1])] += int(command[2])
            if pirate_ship[int(command[1])] > max_health_cap:
                pirate_ship[int(command[1])] = max_health_cap

    elif command[0] == "Status":
        sections_to_repair = 0
        for i in pirate_ship:
            if i < max_health_cap * 0.2:
                sections_to_repair += 1
        print(f"{sections_to_repair} sections need repair.")

    command = input()

if war_ship_alive and pirate_ship_alive:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(war_ship)}")


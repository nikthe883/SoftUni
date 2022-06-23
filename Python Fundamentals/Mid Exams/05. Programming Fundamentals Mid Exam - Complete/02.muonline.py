health = 100
bitcoins = 0
room_counter = 0
rooms = input().split("|")

for i in rooms:

    room_counter += 1
    action, attack = i.split(" ")
    if action == "potion":
        curr_health = health
        health += int(attack)
        if health > 100:
            health = 100

            print(f"You healed for {health - curr_health} hp.")
        else:
            print(f"You healed for {attack} hp.")

        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += int(attack)
        print(f"You found {attack} bitcoins.")

    else:
        health -= int(attack)
        if health <= 0:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {room_counter}")
            break
        else:
            print(f"You slayed {action}.")

if health > 0:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")

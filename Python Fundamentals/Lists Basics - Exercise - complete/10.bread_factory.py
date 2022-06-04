working_day_events = input().split("|")

ENERGY = 100
COINS = 100


for events in working_day_events:
    args = events.split("-")
    event = args[0]
    number = int(args[1])

    if event == "rest":

        if ENERGY + number > 100:
            number = 100 - ENERGY
            ENERGY = 100
        else:
            ENERGY += number

        print(f"You gained {number} energy.\n"
              f"Current energy: {ENERGY}.")

    elif event == "order":
        if ENERGY >= 30:
            ENERGY -= 30
            COINS += number
            print(f"You earned {number} coins.")
        else:

            print("You had to rest!")
            ENERGY += 50

    else:
        COINS -= number
        if COINS >= 0:
            print(f"You bought {event}.")

        else:
            print(f"Closed! Cannot afford {event}.")

            break

if COINS >= 0:
    print(f"Day completed!\n"
          f"Coins: {COINS}\n"
          f"Energy: {ENERGY}")

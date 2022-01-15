
# inputs

fruit = input()
day = input()
quantity = float(input())

# variables
week = {"banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
        }

week_end = {"banana": 2.70,
            "apple": 1.25,
            "orange": 0.90,
            "grapefruit": 1.60,
            "kiwi": 3,
            "pineapple": 5.60,
            "grapes": 4.20
            }

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
week_end_days = ["Saturday", "Sunday"]

found = False

# decisions

if day in week_days:
    for key, value in week.items():
        if key == fruit:
            price = value * quantity
            print(f"{price:.2f}")
            found = True


elif day in week_end_days:
    for key, value in week_end.items():
        if key == fruit:
            price = value * quantity
            print(f"{price:.2f}")
            found = True

if not found:
    print('error')


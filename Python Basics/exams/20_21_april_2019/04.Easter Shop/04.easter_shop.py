
number_eggs = int(input())

action = input()

eggs_sold = 0

while action != "Close":
    eggs = int(input())

    if action == "Buy":
        if eggs > number_eggs:
            print(f"Not enough eggs in store!\n"
                  f"You can buy only {number_eggs}.")
            break
        number_eggs -= eggs
        eggs_sold += eggs

    elif action == "Fill":
        number_eggs += eggs

    action = input()


if action == "Close":
    print(f"Store is closed!\n"
          f"{eggs_sold} eggs sold.")

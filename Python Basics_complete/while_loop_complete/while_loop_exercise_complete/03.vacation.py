
money_for_holiday = float(input())
money_available = float(input())

day_counter = 0
strike_days = 0


while (money_available < money_for_holiday):

    action = input()
    day_counter += 1
    if action == "save":
        money = float(input())

        money_available += money
        strike_days = 0
    else:
        money = float(input())
        strike_days += 1
        money_available -= money
        if money_available < 0:
            money_available = 0
        if strike_days == 5:
            break


if strike_days >= 5:
    print(f"You can't save the money.\n"
          f"{day_counter}")
else:
    print(f'You saved the money for {day_counter} days.')



from math import ceil

number_guests = int(input())
budget = int(input())

price_bread = 4
price_egg = 0.45

breads_needed = ceil(number_guests / 3)
eggs_needed = number_guests * 2

total_price = breads_needed * price_bread +\
                eggs_needed * price_egg

if budget >= total_price:
    left = budget - total_price
    print(f"Lyubo bought {breads_needed} Easter bread and {eggs_needed} eggs.\n"
          f"He has {left:.2f} lv. left.")
else:
    need = total_price - budget
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {need:.2f} lv. more.")

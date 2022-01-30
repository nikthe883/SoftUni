from math import ceil

number_people = int(input())
entry_price = float(input())
price_deck_chair = float(input())
price_umbrella = float(input())

total_entry_price = number_people * entry_price
total_deck_chair_price = ceil(number_people * 0.75) * price_deck_chair
total_umbrella_price = ceil(number_people / 2) * price_umbrella

total_price = total_umbrella_price + total_deck_chair_price +\
                total_entry_price

print(f"{total_price:.2f} lv.")

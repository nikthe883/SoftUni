
days_for_stay = int(input())
type_of_room = input()
assessment = input()

price_for_room = 0

if type_of_room == "room for one person":
    price_for_room = 18
elif type_of_room == "apartment":
    price_for_room = 25
elif type_of_room == "president apartment":
    price_for_room = 35

price_per_stay = days_for_stay * price_for_room  # you need the how many nights he slept in the hotel so - price_per_stay = (days_for_stay - 1) * price_for_room

if type_of_room == "apartment":
    if days_for_stay < 10:
        price_per_stay = price_per_stay * 0.70
    elif 10 <= days_for_stay <= 15:
        price_per_stay = price_per_stay * 0.65
    elif days_for_stay > 15:
        price_per_stay = price_per_stay * 0.50
if type_of_room == "president apartment":
    if days_for_stay < 10:
        price_per_stay = price_per_stay * 0.90
    elif 10 <= days_for_stay <= 15:
        price_per_stay = price_per_stay * 0.85
    elif days_for_stay > 15:
        price_per_stay = price_per_stay * 0.20  # at the moment you are reducing the price with 80 percent : price_per_stay = price_per_stay * 0.80

if assessment == "positive":
    # some mistakes in the cals. We need to add 25 percent on top: price_per_stay = price_per_stay * 1.25
    # you have added 0.25 to the whole price
    price_per_stay = price_per_stay + 0.25 / 100
elif assessment == "negative":
    price_per_stay = price_per_stay * 0.10 # again reducing bu 90 percent you need to reduce by 10 : price_per_stay = price_per_stay * 0.90
print(f"{price_per_stay:.2f}")
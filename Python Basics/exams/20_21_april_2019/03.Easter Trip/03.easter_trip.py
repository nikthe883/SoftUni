destination = input()
date = input()
number_stays = int(input())

price = 0

if destination == "France":
    if date == "21-23":
        price += number_stays * 30
    elif date == "24-27":
        price += number_stays * 35
    elif date == "28-31":
        price += number_stays * 40
elif destination == "Italy":
    if date == "21-23":
        price += number_stays * 28
    elif date == "24-27":
        price += number_stays * 32
    elif date == "28-31":
        price += number_stays * 39
else:
    if date == "21-23":
        price += number_stays * 32
    elif date == "24-27":
        price += number_stays * 37
    elif date == "28-31":
        price += number_stays * 43

print(f'Easter trip to {destination} : {price:.2f} leva.')

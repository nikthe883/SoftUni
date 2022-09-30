
budget = float(input())
gender = input()
age = int(input())
sport = input()

my_dict = {"Gym": [42,35],
            "Boxing": [41, 37],
            "Yoga": [45, 42],
            "Zumba": [34, 31],
            "Dances": [51, 53],
            "Pilates": [39, 37],
           }

price = 0


if gender == "m":
    price = my_dict[sport][0]
elif gender == "f":
    price = my_dict[sport][1]

if age <= 19:
    price *= 0.80

if budget > price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    money = price - budget
    print(f"You don't have enough money! You need ${money:.2f} more.")

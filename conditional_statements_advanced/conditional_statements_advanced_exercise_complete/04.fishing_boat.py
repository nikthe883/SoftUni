

# fast solution

# inputs

fishing_budget = int(input())
season = input()
number_fishers = int(input())

# vars


seasons = {"Spring" : 3000, "Summer" : 4200, "Autumn" : 4200 ,"Winter" : 2600}
price = 0


for k,v in seasons.items():
    if k == season:
        price = v

if number_fishers <= 6:
    price = price - price * 0.1
elif 6 < number_fishers <= 11:
    price =  price - price * 0.15
else:
    price = price - price * 0.25

evan = False
if number_fishers % 2 == 0:
    evan = True

if season != "Autumn" and evan:
    price = price - price * 0.05
else:
    price = price

if price <= fishing_budget:
    money = fishing_budget - price
    print(f"Yes! You have {money:.2f} leva left.")
else:
    money = price - fishing_budget
    print(f"Not enough money! You need {money:.2f} leva.")

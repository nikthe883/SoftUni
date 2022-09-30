budget = float(input())
fuel = float(input())
week_day = input()

price = fuel * 2.10 + 100

if week_day == "Saturday":
    price *= 0.90
elif week_day == "Sunday":
    price *= 0.80

left = abs(budget - price)

if price < budget:
    print(f"Safari time! Money left: {left:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {left:.2f} lv.")

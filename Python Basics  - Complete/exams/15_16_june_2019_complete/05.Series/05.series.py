
budget = float(input())
number_series = int(input())

for i in range(number_series):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        budget -= series_price * 0.50
    elif series_name == "Lucifer":
        budget -= series_price * 0.60
    elif series_name == "Protector":
        budget -= series_price * 0.70
    elif series_name == "TotalDrama":
        budget -= series_price * 0.80
    elif series_name == "Area":
        budget -= series_price * 0.90
    else:
        budget -= series_price


if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")

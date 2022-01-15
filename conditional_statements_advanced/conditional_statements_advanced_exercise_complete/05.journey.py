# inputs

budget = float(input())
season = input()

# variables
destination = ""
holiday_type = ""
price = 0

# decisions

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday_type = "Camp"
        price = budget * 0.3
    else:
        holiday_type = "Hotel"
        price = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday_type = "Camp"
        price = budget * 0.4
    else:
        holiday_type = "Hotel"
        price = budget * 0.8
else:
    destination = "Europe"
    holiday_type = "Hotel"
    price = budget * 0.9

# output

print(f"Somewhere in {destination}\n"
      f"{holiday_type} - {price:.02f}")

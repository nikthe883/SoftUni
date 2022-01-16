
budget = float(input())
season = input()

price = 0
car_class = ""
car_type = ""

if season == "Winter":
    car_type = "Jeep"
elif season == "Summer":
    car_type = "Cabrio"

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        price = budget * 0.35
    else:
        price = budget * 0.65

elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90

else:
    car_class = "Compact class"


    if season == "Summer":
        price = budget * 0.45
    else:
        price = budget * 0.80



print(f"{car_class}\n"
      f"{car_type} - {price:.2f}")

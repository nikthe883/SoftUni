
budget = float(input())
season = input()

place_to_stay = ""
location = ""
price = ""



if budget <= 1000:
    place_to_stay = "Camp"
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.45
    else:
        location = "Alaska"
        price = budget * 0.65
elif budget > 3000:
    place_to_stay = "Hotel"
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.90
    else:
        location = "Alaska"
        price = budget * 0.90
else:
    place_to_stay = "Hut"
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.60
    else:
        location = "Alaska"
        price = budget * 0.80

print(f"{location} - {place_to_stay} - {price:.2f}")

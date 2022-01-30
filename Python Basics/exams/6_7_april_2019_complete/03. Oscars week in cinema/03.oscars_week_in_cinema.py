
movie_name = input()
hall_type = input()
tickets = int(input())

price = 0

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        price = tickets * 7.50
    elif hall_type == "luxury":
        price = tickets * 10.50
    else:
        price = tickets * 13.50

elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        price = tickets * 7.35
    elif hall_type == "luxury":
        price = tickets * 9.45
    else:
        price = tickets * 12.75

elif movie_name == "Green Book":
    if hall_type == "normal":
        price = tickets * 8.15
    elif hall_type == "luxury":
        price = tickets * 10.25
    else:
        price = tickets * 13.25

else:
    if hall_type == "normal":
        price = tickets * 8.75
    elif hall_type == "luxury":
        price = tickets * 11.55
    else:
        price = tickets * 13.95

print(f"{movie_name} -> {price:.2f} lv.")

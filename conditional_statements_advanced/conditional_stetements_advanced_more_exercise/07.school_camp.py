
season = input()
group_type = input()
number_students = int(input())
number_stays = int(input())


sport = ""
price = 0

if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price = number_stays * number_students * 9.60
    elif season == "Spring":
        price = number_stays * number_students * 7.20
    else:
        price = number_stays * number_students * 15
else:
    if season == "Winter":
        price = number_stays * number_students * 10
    elif season == "Spring":
        price = number_stays * number_students * 9.50
    else:
        price = number_stays * number_students * 20

if number_students >= 50:
    price -= price * 0.50
elif 20 <= number_students < 50:
    price -= price * 0.15
elif 10 <= number_students < 20:
    price -= price * 0.05



boys = {"Judo": "Winter", "Tennis": "Spring", "Football": "Summer"}
girls = {"Gymnastics": "Winter", "Athletics": "Spring", "Volleyball": "Summer"}
mixed = {"Ski": "Winter", "Cycling" : "Spring", "Swimming": "Summer"}

sport = ""

if group_type == "boys":
    for k,v in boys.items():
        if v == season:
            sport = k
elif group_type == "girls":
    for k, v in girls.items():
        if v == season:
            sport = k
else:
    for k,v in mixed.items():
        if v == season:
            sport = k



print(f"{sport} {price:.2f} lv.")




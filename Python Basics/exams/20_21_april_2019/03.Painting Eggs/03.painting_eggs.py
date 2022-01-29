egg_size = input()
egg_color = input()
egg_number = int(input())

money = 0

if egg_size == "Large":
    if egg_color == "Red":
        money = egg_number * 16
    elif egg_color == "Green":
        money = egg_number * 12
    elif egg_color == "Yellow":
        money = egg_number * 9

elif egg_size == "Medium":
    if egg_color == "Red":
        money = egg_number * 13
    elif egg_color == "Green":
        money = egg_number * 9
    elif egg_color == "Yellow":
        money = egg_number * 7

else:
    if egg_color == "Red":
        money = egg_number * 9
    elif egg_color == "Green":
        money = egg_number * 8
    elif egg_color == "Yellow":
        money = egg_number * 5

money *= 0.65

print(f"{money:.2f} leva.")

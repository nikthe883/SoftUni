scent = input()
set_size = input()
count_of_sets = int(input())

price = 0

if set_size == "small":
    if scent == "Watermelon":
        price = 56
    elif scent == "Mango":
        price = 36.66
    elif scent == "Pineapple":
        price = 42.10
    elif scent == "Raspberry":
        price = 20
    price *= 2

elif set_size == "big":
    if scent == "Watermelon":
        price = 28.70
    elif scent == "Mango":
        price = 19.60
    elif scent == "Pineapple":
        price = 24.80
    elif scent == "Raspberry":
        price = 15.20
    price *= 5

price = price * count_of_sets

if 400 <= price <= 1000:
    price *= 0.85
if price > 1000:
    price *= 0.50

print(f"{price:.2f} lv.")

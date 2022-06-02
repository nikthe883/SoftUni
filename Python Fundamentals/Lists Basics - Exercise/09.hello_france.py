items = input().split("|")
budget = float(input())

CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES = 20.50
TICKET_PRICE = 150
MARKUP = 0.4
profit = 0
bought_items = []

for i in items:
    arg = i.split("->")
    item_type = arg[0]
    price = float(arg[1])

    if item_type == "Clothes" and price > CLOTHES_MAX_PRICE:
        continue
    if item_type == "Shoes" and price > SHOES_MAX_PRICE:
        continue
    if item_type == "Accessories" and price > ACCESSORIES:
        continue

    if budget < price:
        continue
    budget -= price
    profit += price * MARKUP
    price = price + (price * MARKUP)

    bought_items.append(price)

bought_items_string = " ".join([f"{x:.2f}" for x in bought_items])
print(bought_items_string)

print(f"Profit: {profit:.2f}")
if budget + sum(bought_items) >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")

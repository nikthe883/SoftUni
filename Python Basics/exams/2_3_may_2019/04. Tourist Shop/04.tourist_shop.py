
budget = float(input())

product_name = input()
money_spend = 0
count = 0

while product_name != "Stop":
    product_price = float(input())
    count += 1
    if count % 3 == 0:
        product_price *= 0.5
    money_spend += product_price

    if money_spend > budget:
        print(f"You don't have enough money!\n"
              f"You need {money_spend - budget:.2f} leva!")
        break
    product_name = input()

if product_name == "Stop":
    print(f"You bought {count} products for {money_spend:.2f} leva.")

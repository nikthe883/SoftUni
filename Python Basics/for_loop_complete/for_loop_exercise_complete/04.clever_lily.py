
lily_age = int(input())
machine_cost = float(input())
price_per_toy = int(input())

toys = 0
money = 0
#brother_tax = 0

for i in range(1, lily_age + 1):

    if i % 2 == 0:
        money += (10 * (i / 2)) - 1
    #    brother_tax += 1
    else:
        toys += 1

money_toys = toys * price_per_toy
money = money_toys + money
#money = money - brother_tax

if money >= machine_cost:
    money_left = money - machine_cost
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = machine_cost - money
    print(f"No! {money_needed:.2f}")

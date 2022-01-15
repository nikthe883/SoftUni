excursion = float(input())
puzzle = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())



rent = 0.1
discount = 0.25
prices = []
toys = []


for i in 2.6,3,4.1,8.2,2:
    prices.append(i)


for i in puzzle,talking_dolls,teddy_bears,minions,trucks:
    toys.append(i)


money_before_tax = sum([prices[i] * toys[i] for i in range(len(prices))])


if sum(toys) >= 50:
    money_before_tax -= money_before_tax * discount


money_after_tax = money_before_tax - (money_before_tax * rent)


if money_after_tax >= excursion:
    print(f"Yes! {money_after_tax - excursion:.2f} lv left.")
else:
    print(f"Not enough money! {excursion - money_after_tax:.2f} lv needed.")
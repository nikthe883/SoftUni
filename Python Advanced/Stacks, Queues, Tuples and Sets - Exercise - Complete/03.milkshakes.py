from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))
milkshake = 0

while milkshake < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk_cup = cups_of_milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk_cup)
        continue

    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshake += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk_cup)

if milkshake == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')

if cups_of_milk:
    print(f'Milk: {", ".join([str(x) for x in cups_of_milk])}')
else:
    print(f'Milk: empty')
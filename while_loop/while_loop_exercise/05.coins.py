
# stolen from the net

from math import floor
coins = 0

change = float(input())

change = floor(change * 100)

while change > 0:

    if change >= 200:

        change -= 200

        coins += 1

    elif 200 > change >= 100:

        change -= 100

        coins += 1

    elif 100 > change >= 50:

        change -= 50

        coins += 1

    elif 50 > change >= 20:

        change -= 20

        coins += 1

    elif 20 > change >= 10:

        change -= 10

        coins += 1

    elif 10 > change >= 5:

        change -= 5

        coins += 1

    elif 5 > change >= 2:

        change -= 2

        coins += 1

    elif 2 > change >= 1:

        change -= 1

        coins += 1

print(coins)


from math import ceil, floor
tennis_racket_price = float(input())
number_tennis_rackets = int(input())
number_sneakers = int(input())

price_sneakers = tennis_racket_price / 6

total_price = tennis_racket_price * number_tennis_rackets + \
                price_sneakers * number_sneakers
total_price *= 1.20

djokovic_price = total_price / 8
sponsor_price = total_price * 7/8
print(f"Price to be paid by Djokovic {floor(djokovic_price)}\n"
        f"Price to be paid by sponsors {ceil(sponsor_price)}"
)

budget = float(input())
stays = int(input())
price_per_stay = float(input())
percent_other_expenses = int(input())

if stays > 7:
    price_per_stay *= 0.95

total_price = stays * price_per_stay
total_price += budget * percent_other_expenses / 100

if budget >= total_price:
    left = budget - total_price
    print(f'Ivanovi will be left with {left:.2f} leva after vacation.')
else:
    more = total_price - budget
    print(f"{more:.2f} leva needed.")

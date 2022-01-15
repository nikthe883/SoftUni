
# imports

from math import floor, ceil

# inputs

number_magnolias = int(input())
number_hyacinths = int(input())
number_roses = int(input())
number_cactus = int(input())
gift_price = float(input())

# variables

price_magnolias = 3.25
price_hyacinths = 4.00
price_roses = 3.50
price_cactus = 8.00
taxes_percentage = 0.05

# calculations

total_price_magnolias = number_magnolias * price_magnolias
total_price_hyacinths = number_hyacinths * price_hyacinths
total_price_roses = number_roses * price_roses
total_price_cactus = number_cactus * price_cactus

before_tax_total_income = total_price_cactus + total_price_roses + total_price_hyacinths + total_price_magnolias
after_tax_total_income = before_tax_total_income - (before_tax_total_income * taxes_percentage)

# decisions

if after_tax_total_income >= gift_price:

    money_left = floor(after_tax_total_income - gift_price)
    print(f"She is left with {money_left} leva.")

else:
    money_needed = ceil(gift_price - after_tax_total_income)
    print(f"She will have to borrow {money_needed} leva.")

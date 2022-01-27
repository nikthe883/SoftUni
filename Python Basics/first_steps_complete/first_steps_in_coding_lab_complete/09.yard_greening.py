
# inputs

square_meters = float(input())

# variables

greening_price_per_square_meter = 7.61
discount_percentage = 0.18

# calculations

price_without_discount = square_meters * greening_price_per_square_meter
price_with_discount = price_without_discount - (price_without_discount * discount_percentage)
discount = price_without_discount - price_with_discount

# output

print(f"The final price is: {price_with_discount} lv.\n"
        f"The discount is: {discount} lv.")


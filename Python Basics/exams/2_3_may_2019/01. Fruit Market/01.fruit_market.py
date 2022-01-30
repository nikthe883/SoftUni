
strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_price = strawberry_price * strawberry_kg +\
                raspberries_price * raspberries_kg +\
                oranges_price * oranges_kg +\
                bananas_price * bananas_kg

print(f"{total_price:.2f}")

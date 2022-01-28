
price_flour_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_number = int(input())
maia_number = int(input())

price_sugar_per_kg = price_flour_per_kg * 0.75
price_eggs_per_count = price_flour_per_kg * 1.10
price_maia_per_count = price_sugar_per_kg * 0.20

total_price_sugar = price_sugar_per_kg * sugar_kg
total_price_flour = price_flour_per_kg * flour_kg
total_price_maia = price_maia_per_count * maia_number
total_price_eggs = price_eggs_per_count * eggs_number

total_price = total_price_maia + total_price_eggs + \
                total_price_flour + total_price_sugar
print(f"{total_price:.2f}")

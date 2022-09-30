
# inputs

price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

# variables

bgn_to_eur = 1.94

# calculations

total_price_vegetables = price_kg_vegetables * total_kg_vegetables
total_price_fruits = price_kg_fruits * total_kg_fruits

total_price_bgn = total_price_fruits + total_price_vegetables
total_price_eur = total_price_bgn / bgn_to_eur

# output

print(f"{total_price_eur:.2f}")

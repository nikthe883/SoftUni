
# inputs


price_mackerel = float(input())  # скумрия
price_sprats = float(input())  # цаца
kg_bonito = float(input())  # паламуд
kg_horse_mackerel = float(input())  # сафрид
kg_mussels = int(input())  # миди

# variables

price_bonito_per_kg_percentage = 0.6
price_horse_mackerel_per_kg_percentage = 0.8
price_mussels_per_kg = 7.50

# calculations

price_bonito_per_kg = price_mackerel + price_mackerel * price_bonito_per_kg_percentage
price_horse_mackerel_per_kg = price_sprats + price_sprats * price_horse_mackerel_per_kg_percentage

total_price_bonito = price_bonito_per_kg * kg_bonito
total_price_horse_mackerel = price_horse_mackerel_per_kg * kg_horse_mackerel
total_price_mussels = price_mussels_per_kg * kg_mussels

total_price = total_price_bonito + total_price_mussels + total_price_horse_mackerel

# output

print(f"{total_price:.2f}")





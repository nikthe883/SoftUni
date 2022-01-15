
# imports

from math import ceil, floor

# inputs

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

# calculations

area_of_grapes_for_wine = x * 0.4
kg_grapes_for_wine = area_of_grapes_for_wine * y
wine_liters = kg_grapes_for_wine / 2.5


# decisions

if wine_liters < z:
    wine_liters_needed = z - wine_liters

    print(f"It will be a tough winter! More {floor(wine_liters_needed):.0f} liters wine needed.")

else:
    wine_for_workers = wine_liters - z
    wine_per_worker = wine_for_workers / workers

    print(f"Good harvest this year! Total wine: {floor(wine_liters):.0f} liters.\n"
          f"{ceil(wine_for_workers):.0f} liters left -> {wine_per_worker:.0f} liters per person.")

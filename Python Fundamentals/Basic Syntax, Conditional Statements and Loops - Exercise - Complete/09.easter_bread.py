budget = float(input())
price_flour = float(input())

eggs_pack_price = price_flour * 0.75
one_litter_milk_price = price_flour * 1.25

total_price_one_bread = price_flour + eggs_pack_price + one_litter_milk_price / 4

coloured_eggs_received = 0
count_breads = 0

while total_price_one_bread <= budget:
    budget -= total_price_one_bread
    coloured_eggs_received += 3
    count_breads += 1
    if count_breads % 3 == 0:
        coloured_eggs_received -= count_breads - 2

print(f"You made {count_breads} loaves of Easter bread! Now you have {coloured_eggs_received} eggs and {budget:.2f}BGN left.")

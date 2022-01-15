
# inputs

dog_food_packs = int(input())
cat_food_packs = int(input())

# variables

price_dog_food_pack = 2.5
price_cat_food_pack = 4

# calculations

total_price_cat_food = cat_food_packs * price_cat_food_pack
total_price_dog_food = dog_food_packs * price_dog_food_pack

total_price = total_price_dog_food + total_price_cat_food

# output

print(f'{total_price} lv.')
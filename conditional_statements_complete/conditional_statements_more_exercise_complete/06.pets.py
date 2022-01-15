
# imports

from math import floor, ceil

# inputs

number_days_out = int(input())
left_animal_food_kg = int(input())
daily_dog_food_consumption_kg = float(input())
daily_cat_food_consumption_kg = float(input())
daily_turtle_food_consumption_gr = float(input())


# calculations

food_for_dog_needed_kg = number_days_out * daily_dog_food_consumption_kg
food_for_cat_needed_kg = number_days_out * daily_cat_food_consumption_kg
food_for_turtle_needed_kg = number_days_out * daily_turtle_food_consumption_gr / 1000


total_food_needed = food_for_turtle_needed_kg + food_for_cat_needed_kg + food_for_dog_needed_kg

# decisions

if left_animal_food_kg >= total_food_needed:
    left_food_kg = floor(left_animal_food_kg - total_food_needed)
    print(f"{left_food_kg} kilos of food left.")

else:
    needed_food_kg = ceil(total_food_needed - left_animal_food_kg)
    print(f"{needed_food_kg} more kilos of food are needed.")



walking_time = int(input())
number_of_walks_per_day = int(input())
kcal_per_day = int(input())

kcal_burn_per_min = 5

total_walking_time = walking_time * number_of_walks_per_day
total_kcal_burned_for_the_day = total_walking_time * kcal_burn_per_min

if kcal_per_day /2 <= total_kcal_burned_for_the_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_kcal_burned_for_the_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_kcal_burned_for_the_day}.")

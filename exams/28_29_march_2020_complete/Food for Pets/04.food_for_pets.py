
days = int(input())
total_food = float(input())

dog_food = 0
cat_food = 0
biscuits = 0

for i in range(1,days+1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    if i % 3 == 0:
        biscuits += (dog_eaten_food + cat_eaten_food) * 0.10
    dog_food += dog_eaten_food
    cat_food += cat_eaten_food


total_food_eaten = dog_food + cat_food
percentage_dog_food = dog_food / total_food_eaten * 100
percentage_cat_food = cat_food / total_food_eaten * 100
total_food_eaten_percentage = total_food_eaten / total_food * 100

print(f"Total eaten biscuits: {biscuits:.0f}gr.\n"
      f"{total_food_eaten_percentage:.2f}% of the food has been eaten.\n"
      f"{percentage_dog_food:.2f}% eaten from the dog.\n"
      f"{percentage_cat_food:.2f}% eaten from the cat.")


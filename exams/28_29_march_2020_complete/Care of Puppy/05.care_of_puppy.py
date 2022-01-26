
puppy_food = int(input()) * 1000

dog_food_daily = input()
dog_food_eaten = 0


while dog_food_daily != "Adopted":

    dog_food_eaten += int(dog_food_daily)

    dog_food_daily = input()


if puppy_food >= dog_food_eaten:
    left = puppy_food - dog_food_eaten
    print(f"Food is enough! Leftovers: {left} grams.")
else:
    more = dog_food_eaten - puppy_food
    print(f"Food is not enough. You need {more} grams more.")

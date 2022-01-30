import sys
movies_number = int(input())

highest_rating = 0
lowest_rating = sys.maxsize
total_rating = 0
name_highest = ""
name_lowest = ""

for i in range(movies_number):
    name = input()
    rating = float(input())

    total_rating += rating

    if highest_rating < rating:
        highest_rating = rating
        name_highest = name

    if lowest_rating > rating:
        lowest_rating = rating
        name_lowest = name

average_rating = total_rating / movies_number

print(f"{name_highest} is with highest rating: {highest_rating:.1f}\n"
      f"{name_lowest} is with lowest rating: {lowest_rating:.1f}\n"
      f"Average rating: {average_rating:.1f}")

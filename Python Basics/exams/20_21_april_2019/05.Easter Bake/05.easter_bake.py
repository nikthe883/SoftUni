
from math import ceil
number_breads = int(input())

max_flour = 0
max_sugar = 0
total_sugar = 0
total_flour = 0

for i in range(number_breads):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if max_sugar < sugar:
        max_sugar = sugar
    if max_flour < flour:
        max_flour = flour

sugar_packs = ceil(total_sugar / 950)
flour_packs = ceil(total_flour / 750)

print(f"Sugar: {sugar_packs}\n"
      f"Flour: {flour_packs}\n"
      f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")


from math import floor

text = input()

max_points = 0
points = 0
word_string = ""

special_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

while text != "End of words":

    for value in text:
        points += ord(value)

    if text[0] in special_list:
        points *= len(text)
    else:
        points = floor(points / len(text))

    if max_points < points:
        max_points = points
        word_string = text

    points = 0
    text = input()

print(f"The most powerful word is {word_string} - {max_points}")

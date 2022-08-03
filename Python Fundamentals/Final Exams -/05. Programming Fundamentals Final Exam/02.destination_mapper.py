import re

pattern = r"=[A-Z][A-Za-z]{2,}=|\/[A-Z][A-Za-z]{2,}\/"

destinations = input()

matches = re.finditer(pattern, destinations)


total_destinations = []
travel_points = 0

for i in matches:
    word = ""
    for l in i.group():
        if l.isalpha():
            word += l
    total_destinations.append(word)
    travel_points += len(word)
    word = ""

print(f"Destinations: {', '.join(total_destinations)}")
print(f"Travel Points: {travel_points}")

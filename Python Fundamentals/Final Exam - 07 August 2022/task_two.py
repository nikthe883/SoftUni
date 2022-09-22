import re

n = int(input())

pattern = r"\|{1}([A-Z]{4,})\|{1}:{1}#{1}([A-Za-z]+\s[A-Za-z]+)#{1}"

for i in range(n):
    message = input()
    matches = re.match(pattern, message)
    if matches:
        print(f"{matches.group(1)}, The {matches.group(2)}")
        print(f">> Strength: {len(matches.group(1))}")
        print(f">> Armor: {len(matches.group(2))}")
    else:
        print("Access denied!")

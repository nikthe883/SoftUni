import re

pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"

dates = input()

matches = re.findall(pattern, dates)

for m in matches:
    print(f"Day: {m[0]}, Month: {m[2]}, Year: {m[3]}")

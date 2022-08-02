import re

pattern = r"\d+"

text = input()
match = []
while True:
    if text:
        matches = re.findall(pattern, text)
        match += matches
    else:
        break
    text = input()

print(" ".join(match))



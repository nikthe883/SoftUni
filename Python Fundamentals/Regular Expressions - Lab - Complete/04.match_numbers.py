import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
text = input()

matches = re.finditer(pattern, text)

for m in matches:
    print(m.group(), end=" ")

import re

text = input()
pattern = r"www.[A-Za-z0-9\]+.[a-z\-]+(\.[a-z]+)+"
while True:
    if text:
        matches = re.finditer(pattern, text)
        for i in matches:
            print(i.group())
    else:
        break
    text = input()

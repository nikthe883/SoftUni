banned = input().split(", ")
text = input()

for i in banned:
    while i in text:
        text = text.replace(i, "*" * len(i))
print(text)

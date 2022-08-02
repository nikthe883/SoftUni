import re

text = input()

cool_threshold = 1
emoji = []

pattern = r":{2}[A-Z][a-z]{2,}:{2}|\*{2}[A-Z][a-z]{2,}\*{2}|\d"

matches = re.findall(pattern, text)
for i in matches:
    if i.isdigit():
        cool_threshold *= int(i)
    else:
        emoji.append(i)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji)} emojis found in the text. The cool ones are:")

emoji_coolness = 0

for word in emoji:
    for i in word:
        if i.isalpha():
            emoji_coolness += ord(i)
        if emoji_coolness >= cool_threshold:
            print(word)
            break
    emoji_coolness = 0

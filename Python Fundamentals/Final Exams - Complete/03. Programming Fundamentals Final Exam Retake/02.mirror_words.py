import re

pattern = r"@{1}([A-Za-z]{3,})@{2}([A-Za-z]{3,})@{1}|#{1}([A-Za-z]{3,})#{2}([A-Za-z]{3,})#{1}"

text = input()

matches = re.findall(pattern, text)

my_dict = {}

for words in matches:
    for i in range(len(words)):
        if words[i] != "":
            if words[i][::-1] == words[i+1]:
                my_dict[words[i]] = words[i+1]
            break

some_string = ""
for k in my_dict:
    some_string += f"{k} <=> {my_dict[k]}, "

if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")

    if len(some_string) > 0:
        print("The mirror words are:")
        print(some_string[:-2])
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")

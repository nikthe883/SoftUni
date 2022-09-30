character = input().split(", ")
my_dict = {}

for i in character:
    my_dict[i] = ord(i)

print(my_dict)
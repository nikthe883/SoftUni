string_one = input().split(", ")
string_two = input().split(", ")

repeated_substrings = [x for x in string_one if any(x in b for b in string_two)]

print(repeated_substrings)


# inputs

number = int(input())

# variables

bonus = 0

# decision

if number <= 100:
    bonus = 5
elif 1000 >= number > 100:
    bonus = number * 0.2
else:
    bonus = number * 0.1

# checks if odd or even
if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

# output

print(bonus)
print(bonus + number)

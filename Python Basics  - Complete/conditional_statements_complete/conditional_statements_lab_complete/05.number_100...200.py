
# checks if user number < 100 , from 100 to 200 or > 200

# inputs

number = int(input())

# decision

if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
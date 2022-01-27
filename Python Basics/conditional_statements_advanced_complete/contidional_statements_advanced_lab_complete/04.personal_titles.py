
# inputs

age = float(input())
gender = input()

# decisions

if gender == 'm':
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

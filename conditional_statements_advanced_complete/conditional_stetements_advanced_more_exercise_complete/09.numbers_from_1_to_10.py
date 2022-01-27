
# variant 1

negative = False

while not negative:

    number = float(input())

    if number >= 0:
        print(f"Result: {number * 2:.2f}")
    else:
        print("Negative number!")
        negative = True

# variant 2

while True:
    number = float(input())

    if number >= 0:
        print(f"Result: {number * 2:.2f}")
    else:
        print("Negative number!")
        break


# variant 3

number = 0

while number >= 0:

    number = float(input())

    if number >= 0:
        number = number
        print(f"Result: {number * 2:.2f}")
    else:
        print("Negative number!")
        number = number



prev_number = -100_000_000

while True:
    number = input()

    if number == "Stop":
        print(prev_number)
        break

    elif int(number) > prev_number:
        prev_number = int(number)


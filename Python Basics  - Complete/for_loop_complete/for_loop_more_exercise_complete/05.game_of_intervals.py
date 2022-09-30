number_of_loops = int(input())

points = 0
nine = 0
nineteen = 0
twenty_nine = 0
thirty_nine = 0
fifty = 0
invalid_numbers = 0

for _ in range(number_of_loops):

    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.20
        nine += 1

    elif 10 <= number <= 19:
        points += number * 0.30
        nineteen += 1

    elif 20 <= number <= 29:
        points += number * 0.40
        twenty_nine += 1

    elif 30 <= number <= 39:
        points += 50
        thirty_nine += 1

    elif 40 <= number <= 50:
        points += 100
        fifty += 1

    else:
        invalid_numbers += 1
        points = points / 2

average_nine = nine / number_of_loops * 100
average_nineteen = nineteen / number_of_loops * 100
average_twenty_nine = twenty_nine / number_of_loops * 100
average_thirty_nine = thirty_nine / number_of_loops * 100
average_fifty = fifty / number_of_loops * 100
average_invalid_number = invalid_numbers / number_of_loops * 100

print(f"{points:.2f}\n"
      f"From 0 to 9: {average_nine:.2f}%\n"
      f"From 10 to 19: {average_nineteen:.2f}%\n"
      f"From 20 to 29: {average_twenty_nine:.2f}%\n"
      f"From 30 to 39: {average_thirty_nine:.2f}%\n"
      f"From 40 to 50: {average_fifty:.2f}%\n"
      f"Invalid numbers: {average_invalid_number:.2f}%")

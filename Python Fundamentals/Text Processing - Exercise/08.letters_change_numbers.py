user_input = input()
user_input = " ".join(user_input.split())
user_input = user_input.split(" ")
total = 0

for i in user_input:
    total_curr = 0
    number = ''
    for n in i:
        if n.isdigit():
            number += n
    number = int(number)
    for index, value in enumerate(i):
        if index == 0:
            letter_position = ord(value.lower()) - 96
            if value.islower():
                total_curr += number * letter_position
            else:
                total_curr += number / letter_position

        elif index == len(i) - 1:

            letter_position = ord(value.lower()) - 96
            if value.islower():
                total_curr += letter_position
            else:
                total_curr -= letter_position
    total += total_curr


print(f"{total:.2f}")


number_count = int(input())
loop = 0
numbers = 0

while loop < number_count:

    number = int(input())
    numbers += number
    loop += 1

average_value = numbers / number_count

print(f"{average_value:.2f}")

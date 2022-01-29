
one = int(input())
two = int(input())
five = int(input())
total = int(input())

for num1 in range(one + 1):
    for num2 in range(two + 1):
        for num3 in range(five + 1):
            if num1 * 1 + num2 * 2 + num3 * 5 == total:
                print(f"{num1} * 1 lv. + {num2} * 2 lv. + {num3} * 5 lv. = {total} lv.")



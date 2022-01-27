# there should be a better solution to this...

control = int(input())

numbers = ""

for num1 in range(1,10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num1 < num2 and num3 > num4 and num1 * num2 + num3 * num4 == control:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
                    numbers += f"{num1}{num2}{num3}{num4} "

print()



if len(numbers) < 19:
    print("No!")
else:
    print(f"Password: {numbers[15]}{numbers[16]}{numbers[17]}{numbers[18]}")

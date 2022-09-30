
max_num1 = int(input())
max_num2 = int(input())
max_num3 = int(input())

for num1 in range(1,max_num1 + 1):
    for num2 in range(1, max_num2 + 1):
        for num3 in range(1, max_num3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                    print(f"{num1} {num2} {num3}")

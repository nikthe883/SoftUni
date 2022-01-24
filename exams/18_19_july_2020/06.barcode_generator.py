
num1 = input()
num2 = input()


for n1 in range(int(num1[0]), int(num2[0]) + 1):
    for n2 in range(int(num1[1]), int(num2[1]) + 1):
        for n3 in range(int(num1[2]), int(num2[2]) + 1):
            for n4 in range(int(num1[3]), int(num2[3]) + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")



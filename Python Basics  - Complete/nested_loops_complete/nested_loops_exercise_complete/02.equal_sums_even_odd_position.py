
num1 = int(input())
num2 = int(input())

for i in range(num1, num2 +1):
    num_str = str(i)
    even = 0
    odd = 0

    for index, digit in enumerate(num_str):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)

    if even == odd:
        print(i, end=" ")
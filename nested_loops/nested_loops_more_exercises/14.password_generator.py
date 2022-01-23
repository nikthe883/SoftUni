
n = int(input())
l = int(input())

for num1 in range(1, n + 1):
    for num2 in range(1, n + 1):
        for let1 in range(97, l + 97):
            for let2 in range(97, l + 97):
                for num3 in range(1, n + 1):
                    if num3 > num1 and num3 > num2:
                        print(f"{num1}{num2}{chr(let1)}{chr(let2)}{num3}", end=" ")

#  So ASCII small letters start from 97
#  https://www.asciitable.com/

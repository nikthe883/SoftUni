
# GOOD DECISION

n = int(input())

for num1 in range(1,10):
    for num2 in range(1,10):
        for num3 in range(1,10):
            for num4 in range(1,10):
                if n % num1 == 0 and n % num2 == 0 and n % num3 == 0 and n % num4 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")

# mine alternative gibberish

n = int(input())
special = 0
number = ""
for i in range(1111, 10_000):
    str_i = str(i)
    for b in str_i:
        if b == "0":  # catching the 0 to avoid / 0
            pass
        else:
            if n % int(b) == 0:
                number += b   # appending the number to empty string if if meets req

    if str(i) == number:
        print(i, end=" ")  # printing the number if it is == to i

    number = ""  # refreshing the string




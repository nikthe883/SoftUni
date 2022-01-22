
# BETTER SOLUTION : https://github.com/hammer4/SoftUni/blob/master/Programming%20Basics%20with%20Python/05.%20Simple%20Loops/11.%20Odd%20Even%20Position.py

counts = int(input())

odd_sum = 0
odd_min = 10000
odd_max = -10000

even_sum = 0
even_min = 10000
even_max = -10000

odd_min_prev = 0
even_min_prev = 0

for i in range(1, counts + 1):
    num = float(input())

    if i % 2 == 0:
        even_sum += num
        even_min_prev = num

        if even_min > even_min_prev:
            even_min = num

        if num > even_max:
            even_max = num

    else:
        odd_sum += num
        odd_min_prev = num
        if odd_min > odd_min_prev:
            odd_min = num

        if num > odd_max:
            odd_max = num

if even_max == -10_000:
    even_max = "No"
else:
    even_max = f"{even_max:.2f}"

if even_min == 10_000:
    even_min = "No"
else:
    even_min = f"{even_min:.2f}"

if odd_max == -10_000:
    odd_max = "No"
else:
    odd_max = f"{odd_max:.2f}"

if odd_min == 10_000:
    odd_min = "No"
else:
    odd_min = f"{odd_min:.2f}"

print(f"OddSum={odd_sum:.2f},\n"
      f"OddMin={odd_min},\n"
      f"OddMax={odd_max},\n"
      f"EvenSum={even_sum:.2f},\n"
      f"EvenMin={even_min},\n"
      f"EvenMax={even_max}")

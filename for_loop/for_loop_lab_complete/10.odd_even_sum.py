
n = int(input())

odd = 0
even = 0

for i in range(n):
    num1 = int(input())
    if i % 2 == 0:
        even += num1
    else:
        odd += num1

if odd == even:
    print(f"Yes\n"
          f"Sum = {odd}")
else:
    diff = abs(odd - even)
    print(f"No\n"
          f"Diff = {diff}")


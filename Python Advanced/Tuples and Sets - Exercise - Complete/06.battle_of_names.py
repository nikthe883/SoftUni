n = int(input())

odd = set()
even = set()

for i in range(1, n + 1):
    values = [ord(x) for x in input()]
    total = sum(values) // i
    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)
if sum(even) > sum(odd):
    print(*even.symmetric_difference(odd),sep=", ")
else:
    print(*odd.difference(even), sep=", ")

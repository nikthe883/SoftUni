n, m = [int(x) for x in input().split()]

a = set()
b = set()

for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))

print(*a.intersection(b), sep="\n")


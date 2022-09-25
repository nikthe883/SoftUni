n = int(input())
unique = []
for _ in range(n):
    unique.append(input())

for i in set(unique):
    print(i)

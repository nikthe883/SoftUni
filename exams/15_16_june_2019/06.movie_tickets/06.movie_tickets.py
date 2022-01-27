
a1 = int(input())
a2 = int(input())
n = int(input())

m = round(n / 2)
for i in range(a1, a2):
    for b in range(1, n):
        for c in range(1, m):
            if i % 2 != 0 and (b + c + i) % 2 != 0:
                print(f"{chr(i)}-{b}{c}{i}")



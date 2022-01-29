n = int(input())

for i in range(n+1):
    stars = "*" * i
    spaces = " " * (n-i)
    print(f"{spaces}", end="")
    print(f"{stars}",end="")
    print(f" | ",end="")
    print(f"{stars}",end="")
    print(f"{spaces}")
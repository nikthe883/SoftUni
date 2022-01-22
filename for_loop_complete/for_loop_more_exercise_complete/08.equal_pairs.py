
n = int(input())
previous = int(input()) + int(input())
diff = 0

for i in range(n -1):
    curr = int(input()) + int(input())

    if abs(previous - curr) > diff:
        diff = abs(previous - curr)

    previous = curr

if diff == 0:
    print(f"Yes, value={previous}")
else:
    print(f"No, maxdiff={diff}")

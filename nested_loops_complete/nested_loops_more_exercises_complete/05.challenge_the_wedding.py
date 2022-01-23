men = int(input())
women = int(input())
max_tables = int(input())

counter = 0

for m in range(1, men + 1):
    for w in range(1, women + 1):
        counter += 1
        if counter > max_tables:
            break
        else:
            print(f"({m} <-> {w})", end=" ")

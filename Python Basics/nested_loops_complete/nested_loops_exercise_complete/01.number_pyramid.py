
to_number = int(input())
current = 1


for row in range(1,to_number + 1):
    for cow in range(1, row + 1):
        if current > to_number:
            break
        print(f"{current}", end=" ")
        current += 1
    if current > to_number:
        break
    print()

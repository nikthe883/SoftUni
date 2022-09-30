rows, columns = [int(x) for x in input().split()]
snake = input()
matrix = []

idx = 0
for row in range(rows):
    path = ""
    for column in range(columns):
        path += snake[idx % len(snake)]
        idx += 1

    if row % 2 == 0:
        matrix.append(path)
    else:
        matrix.append(path[::-1])

for i in matrix:
    print(*i, sep="")

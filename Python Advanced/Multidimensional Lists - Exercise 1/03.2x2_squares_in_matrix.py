rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
total = 0
for row in range(rows - 1):
    for column in range(cols - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            total += 1
print(total)


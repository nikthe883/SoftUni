rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

total = 0
for row in matrix:
    total += sum(row)
print(total)
print(matrix)

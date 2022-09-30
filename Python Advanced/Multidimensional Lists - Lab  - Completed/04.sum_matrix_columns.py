rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()]for x in range(rows)]

for i in range(cols):
    total_col_sum = 0
    for j in range(rows):
        total_col_sum += matrix[j][i]
    print(total_col_sum)

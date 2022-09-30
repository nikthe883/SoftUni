rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for x in range(rows)]

max_matrix = []
sum_max_matrix = 0

for row in range(rows - 2):
    for column in range(cols - 2):
        curr_matrix = [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2],
                       matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2],
                       matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]
                       ]
        curr_sum_matrix = sum(curr_matrix)
        if curr_sum_matrix > sum_max_matrix:
            max_matrix = curr_matrix
            sum_max_matrix = curr_sum_matrix

print(f"Sum = {sum_max_matrix}")
print(" ".join(str(x) for x in max_matrix[:3]))
print(" ".join(str(x) for x in max_matrix[3:6]))
print(" ".join(str(x) for x in max_matrix[6:]))


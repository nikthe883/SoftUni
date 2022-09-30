rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]

max_matrix = []
sum_max_matrix = 0

for row in range(rows - 1):
    for column in range(cols - 1):

        curr_matrix = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column], matrix[row + 1][column + 1]]
        curr_sum_matrix = sum(curr_matrix)
        if curr_sum_matrix > sum_max_matrix:
            max_matrix = curr_matrix
            sum_max_matrix = curr_sum_matrix

print(" ".join(str(x) for x in max_matrix[:2]))
print(" ".join(str(x) for x in max_matrix[2:]))
print(sum_max_matrix)

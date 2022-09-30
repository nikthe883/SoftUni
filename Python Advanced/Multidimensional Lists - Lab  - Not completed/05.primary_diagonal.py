rows = int(input())
matrix = [[int(x) for x in input().split()]for x in range(rows)]
total_sum = 0
for i in range(rows):
    for j in range(rows):
        if i == j:
            total_sum += matrix[j][i]

print(total_sum)

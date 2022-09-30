rows = int(input())

matrix = [[int(x) for x in input().split()] for i in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[rows - 1 - i][i] for i in range(rows - 1, -1, -1)]

print(abs(sum(primary) - sum(secondary)))

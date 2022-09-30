rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[rows - 1 - i][i] for i in range(rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")

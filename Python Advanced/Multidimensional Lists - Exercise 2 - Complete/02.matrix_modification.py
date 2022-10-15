n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

command = input().split()
while command[0] != "END":

    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if action == "Add":
        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input().split()

for line in matrix:
    print(*line, sep=" ")

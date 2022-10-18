matrix = []

for row in range(6):
    matrix.append(input().split())

first_pos = input().strip("(").strip(")").split(", ")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input().split(", ")

while command[0] != "Stop":
    rol, col = 0, 0
    if command[0] == "Create":
        row, col = int(first_pos[0]) + directions[command[1]][0], int(first_pos[1]) + directions[command[1]][1]
        if matrix[row][col] == ".":
            matrix[row][col] = command[2]

    elif command[0] == "Update":
        row, col = int(first_pos[0]) + directions[command[1]][0], int(first_pos[1]) + directions[command[1]][1]
        if matrix[row][col] != ".":
            matrix[row][col] = command[2]

    elif command[0] == "Delete":
        row, col = int(first_pos[0]) + directions[command[1]][0], int(first_pos[1]) + directions[command[1]][1]
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    elif command[0] == "Read":
        row, col = int(first_pos[0]) + directions[command[1]][0], int(first_pos[1]) + directions[command[1]][1]
        if matrix[row][col] != ".":
            print(matrix[row][col])
    first_pos = [row, col]
    command = input().split(", ")

for i in matrix:
    print(" ".join(i))


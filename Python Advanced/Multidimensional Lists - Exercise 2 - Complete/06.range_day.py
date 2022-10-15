n = 5

matrix = []
shooter = []
targets_shot_position = []
row, column = 0, 0
total_targets = 0
targets_shot = 0

for row in range(n):
    lst = input().split()
    if 'A' in lst:
        shooter = [row, lst.index('A')]
    matrix.append(lst)

for i in matrix:
    total_targets += i.count("x")

number = int(input())

for _ in range(number):
    commands = input().split()
    bullet = [shooter[0], shooter[1]]

    if commands[0] == "move":
        if commands[1] == "right":
            row, column = shooter[0], shooter[1] + int(commands[2])
        elif commands[1] == "left":
            row, column = shooter[0], shooter[1] - int(commands[2])
        elif commands[1] == "down":
            row, column = shooter[0] + int(commands[2]), shooter[1]
        elif commands[1] == "up":
            row, column = shooter[0] - int(commands[2]), shooter[1]

        if 0 <= row < 5 and 0 <= column < 5 and matrix[row][column] == ".":
            matrix[shooter[0]][shooter[1]] = "."
            shooter[0], shooter[1] = row, column
            matrix[row][column] = "A"

    elif commands[0] == "shoot":
        while True:
            if 0 > bullet[0] or bullet[0] >= n or 0 > bullet[1] or bullet[1] >= n:
                break
            if matrix[bullet[0]][bullet[1]] == "x":
                matrix[bullet[0]][bullet[1]] = "."
                targets_shot_position.append([bullet[0], bullet[1]])
                targets_shot += 1
                break
            if commands[1] == "right":
                bullet[1] += 1
            elif commands[1] == "left":
                bullet[1] -= 1
            elif commands[1] == "down":
                bullet[0] += 1
            elif commands[1] == "up":
                bullet[0] -= 1
    if targets_shot == total_targets:
        break
    # for i in matrix:
    #     print(i)
    # print()


if targets_shot != total_targets:
    print(f"Training not completed! {total_targets - targets_shot} targets left.")

else:
    print(f"Training completed! All {total_targets} targets hit.")
for i in targets_shot_position:
    print(i)

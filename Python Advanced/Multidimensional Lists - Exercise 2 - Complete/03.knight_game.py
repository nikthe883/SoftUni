
# not working dont want to make it work - working des - https://github.com/anachevv/SoftUni/blob/main/SoftUni-Project/SoftUni%20Advanced/Multidimensional%20Lists/Exercise%202/knight_game.py
n = int(input())

board = []

for _ in range(n):
    board.append([x for x in input()])

pos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

knights_removed = 0

while True:
    treats = {}
    for row in range(n - 1):
        for col in range(n - 1):
            if board[row][col] == "K":
                for position in pos:
                    if 0 <= row + position[0] <= len(board) - 1 and 0 <= col + position[1] <= len(board) - 1:
                        if board[row + position[0]][col + position[1]] == "K":
                            if (row, col) not in treats:
                                treats[row, col] = 0
                            else:
                                treats[row, col] += 1
    if not treats:
        break

    most_threatening = max(treats, key=treats.get)
    board[most_threatening[0]][most_threatening[1]] = "0"
    knights_removed += 1


print(knights_removed)

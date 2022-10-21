matrix = []

for i in range(8):
    matrix.append(input().split())

white = ()
black = ()
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
count = 8
for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white = (row, col)
            matrix[row][col] = letters[col] + str(count)
        if matrix[row][col] == 'b':
            black = (row, col)
            matrix[row][col] = letters[col] + str(count)
        if matrix[row][col] == "-":
            matrix[row][col] = letters[col] + str(count)
    count -= 1

white_alive = True
black_alive = True
while True:

    if white_alive:
        if (white[0] - 1, white[1] + 1) == black or (white[0] - 1, white[1] - 1) == black:
            white = black
            black_alive = False
            print(f"Game over! White win, capture on {matrix[white[0]][white[1]]}.")
            break
        else:
            white = white[0] - 1, white[1]
            # matrix[white[0]][white[1]] = matrix[white[0] - 1][white[1]]
            if white[0] == 0:
                print(f"Game over! White pawn is promoted to a queen at {matrix[white[0]][white[1]]}.")
                break

    if black_alive:
        if (black[0] + 1, black[1] + 1) == white or (black[0] + 1, black[1] - 1) == white:
            black = white
            white_alive = False
            print(f"Game over! Black win, capture on {matrix[black[0]][black[1]]}.")
            break
        else:
            black = black[0] + 1, black[1]
            # matrix[black[0]][black[1]] = matrix[black[0] + 1][black[1]]
            if black[0] == 7:
                print(f"Game over! Black pawn is promoted to a queen at {matrix[black[0]][black[1]]}.")
                break



n = int(input())

matrix = []
alice = []

for row in range(n):
    lst = input().split()
    if 'A' in lst:
        alice = [row, lst.index('A')]
    matrix.append(lst)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

tea = 0
matrix[alice[0]][alice[1]] = "*"
while True:
    command = input()

    row = alice[0] + directions[command][0]
    column = alice[1] + directions[command][1]

    if 0 > row or row >= n or 0 > column or column >= n:
        print("Alice didn't make it to the tea party.")
        break
    if matrix[row][column] == "R":
        matrix[row][column] = "*"
        print("Alice didn't make it to the tea party.")
        break

    else:
        alice = [row, column]
        if matrix[row][column] != "." and matrix[row][column] != "*":
            tea += int(matrix[row][column])
    matrix[row][column] = "*"

    if tea >= 10:
        print("She did it! She went to the party.")
        break


for i in matrix:
    print(*i, sep=" ", end="\n")

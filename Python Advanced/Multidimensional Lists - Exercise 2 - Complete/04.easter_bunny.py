size = int(input())
matrix = []
b = []
max_eggs = 0
best_dir = ""
best_p = []


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(size):
    lst = input().split()
    if 'B' in lst:
        b = [row, lst.index('B')]


    matrix.append(lst)


for dir, pos in directions.items():
    path = []
    eggs = 0
    row, column = [b[0] + pos[0], b[1] + pos[1]]

    while 0 <= row < size and 0 <= column < size:
        if matrix[row][column] == 'X':
            break
        eggs += int(matrix[row][column])
        path.append([row, column])

        row += pos[0]
        column += pos[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        best_dir = dir
        best_p = path

print(best_dir)
print(*best_p, sep='\n')
print(max_eggs)

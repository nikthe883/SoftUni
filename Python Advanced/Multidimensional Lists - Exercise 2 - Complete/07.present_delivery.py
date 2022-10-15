number_of_presents = int(input())
size = int(input())

neighborhood = []
santa = []

for row in range(size):
    lst = input().split()
    if 'S' in lst:
        santa = [row, lst.index('S')]
    neighborhood.append(lst)

neighborhood[santa[0]][santa[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
total_nice_kids = 0
for i in neighborhood:
    total_nice_kids += i.count("V")

nice_kids_visited = 0

while True:
    command = input()
    if command == "Christmas morning":
        break

    row = santa[0] + directions[command][0]
    column = santa[1] + directions[command][1]

    if neighborhood[row][column] == "V":
        number_of_presents -= 1
        nice_kids_visited += 1
        neighborhood[row][column] = "-"

    if neighborhood[row][column] == "X" and number_of_presents:
        neighborhood[row][column] = "-"

    if neighborhood[row][column] == "C" and number_of_presents:
        for pos1, pos2 in directions.values():

            if neighborhood[row + pos1][column + pos2] == "V" :
                neighborhood[row + pos1][column + pos2] = "-"
                number_of_presents -= 1
                nice_kids_visited += 1

            elif neighborhood[row + pos1][column + pos2] == "X":
                number_of_presents -= 1
                neighborhood[row + pos1][column + pos2] = "-"

    santa = row, column

    if not number_of_presents or nice_kids_visited == total_nice_kids:
        break

neighborhood[santa[0]][santa[1]] = "S"

if not number_of_presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

for i in neighborhood:
    print(" ".join([x for x in i]))

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")

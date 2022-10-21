rows, cols = [int(x) for x in input().split(", ")]

def check_collectables():
    values = False
    if collectable['C'] == 0 and collectable['D'] == 0 and collectable['G'] == 0:
        values = True
    return values

matrix = [input().split() for _ in range(rows)]
santa = []
collectable = {"C": 0, "D": 0, "G": 0}


for i in range(len(matrix)):
    for b in range(len(matrix[i])):
        if matrix[i][b] == "Y":
            santa += i, b
        if matrix[i][b] == "C":
            collectable[matrix[i][b]] += 1
        if matrix[i][b] == "D":
            collectable[matrix[i][b]] += 1
        if matrix[i][b] == "G":
            collectable[matrix[i][b]] += 1

collectable_gathered = {"C": 0, "D": 0, "G": 0}
run = True
commands = input().split("-")
values = False

while commands[0] != "End" and run:
    matrix[santa[0]][santa[1]] = "x"
    if commands[0] == "right":
        for _ in range(int(commands[1])):
            santa[1] += 1
            if santa[1] > cols-1:
                santa[1] = 0
            if matrix[santa[0]][santa[1]] in collectable.keys():
                collectable[matrix[santa[0]][santa[1]]] -= 1
                collectable_gathered[matrix[santa[0]][santa[1]]] += 1
                values = check_collectables()
                if values:
                    break

            matrix[santa[0]][santa[1]] = "x"

    if commands[0] == "left":
        for _ in range(int(commands[1])):
            santa[1] -= 1
            if santa[1] < 0:
                santa[1] = cols - 1
            if matrix[santa[0]][santa[1]] in collectable.keys():
                collectable[matrix[santa[0]][santa[1]]] -= 1
                collectable_gathered[matrix[santa[0]][santa[1]]] += 1
                values = check_collectables()
                if values:
                    break
            matrix[santa[0]][santa[1]] = "x"


    if commands[0] == "up":
        for _ in range(int(commands[1])):
            santa[0] -= 1
            if santa[0] < 0:
                santa[0] = rows - 1
            if matrix[santa[0]][santa[1]] in collectable.keys():
                collectable[matrix[santa[0]][santa[1]]] -= 1
                collectable_gathered[matrix[santa[0]][santa[1]]] += 1
                values = check_collectables()
                if values:
                    break
            matrix[santa[0]][santa[1]] = "x"

    if commands[0] == "down":
        for _ in range(int(commands[1])):
            santa[0] += 1
            if santa[0] > rows - 1:
                santa[0] = 0
            if matrix[santa[0]][santa[1]] in collectable.keys():
                collectable[matrix[santa[0]][santa[1]]] -= 1
                collectable_gathered[matrix[santa[0]][santa[1]]] += 1
                values = check_collectables()
                if values:
                    break
            matrix[santa[0]][santa[1]] = "x"

    if values:
        run = False
    else:
        commands = input().split("-")

if values:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {collectable_gathered['D']} Christmas decorations")
print(f"- {collectable_gathered['G']} Gifts")
print(f"- {collectable_gathered['C']} Cookies")

for i in range(rows):
    for b in range(cols):
        if i == santa[0] and b == santa[1]:
            matrix[i][b] = "Y"

for i in matrix:
    print(" ".join(i))



size = int(input())
racing_number = input()
matrix = []
kilometers = 0
car_pos = [0,0]

tunnel_pos = []

for i in range(size):
    matrix.append([x for x in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "T":
            tunnel_pos.append([row, col])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


command = input()
finished = False
while command != "End":

    kilometers += 10
    row, column = [directions[command][0] + car_pos[0], directions[command][1] + car_pos[1]]
    car_pos[0] = row
    car_pos[1] = column

    if matrix[car_pos[0]][car_pos[1]] == "T":
        if car_pos[0] == tunnel_pos[0][0] and car_pos[1] == tunnel_pos[0][1]:
            car_pos = tunnel_pos[1]


        elif car_pos[0] == tunnel_pos[1][0] and car_pos[1] == tunnel_pos[1][1]:
            car_pos = tunnel_pos[0]

        kilometers += 20
        matrix[tunnel_pos[1][0]][tunnel_pos[1][1]] = "."
        matrix[tunnel_pos[0][0]][tunnel_pos[0][1]] = "."

    if matrix[car_pos[0]][car_pos[1]] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        finished = True
        break

    command = input()
if not finished:
    print(f"Racing car {racing_number} DNF.")
matrix[car_pos[0]][car_pos[1]] = "C"
print(f"Distance covered {kilometers} km.")
for i in matrix:
    print("".join(i))

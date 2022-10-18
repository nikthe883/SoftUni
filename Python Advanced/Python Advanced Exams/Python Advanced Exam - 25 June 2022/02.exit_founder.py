order = input().split(", ")
first, second = "", ""

if order[0] == "Tom":
    first = "Tom"
    second = "Jerry"
else:
    first = "Jerry"
    second = "Tom"

matrix = []

for _ in range(6):
    matrix.append([x for x in input().split()])


first_pass = False
second_pass = False

while True:

    first_coordinates = tuple(int(x) for x in input() if x.isdigit())
    if not first_pass:

        if matrix[first_coordinates[0]][first_coordinates[1]] == "E":
            print(f"{first} found the Exit and wins the game!")
            break

        if matrix[first_coordinates[0]][first_coordinates[1]] == "T":
            print(f"{first} is out of the game! The winner is {second}.")
            break

        if matrix[first_coordinates[0]][first_coordinates[1]] == "W":
            print(f"{first} hits a wall and needs to rest.")
            first_pass = True
    else:
        first_pass = False

    second_coordinates = tuple(int(x) for x in input() if x.isdigit())
    if not second_pass:

        if matrix[second_coordinates[0]][second_coordinates[1]] == "T":
            print(f"{second} is out of the game! The winner is {first}.")
            break

        if matrix[second_coordinates[0]][second_coordinates[1]] == "E":
            print(f"{second} found the Exit and wins the game!")
            break

        if matrix[second_coordinates[0]][second_coordinates[1]] == "W":
            print(f"{second} hits a wall and needs to rest.")
            second_pass = True
    else:
        second_pass = False










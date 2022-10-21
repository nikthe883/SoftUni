matrix = []

for i in range(6):
    matrix.append([x for x in input().split()])


rover = ()

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "E":
            rover = row, col

deposits = {"W": "Water deposit" , "C": "Concrete deposit", "M": "Metal deposit"}
deposits_found = {"W": 0, "C": 0, "M": 0}

commands = input().split(", ")

for command in commands:

    if command == "left":
        rover = rover[0], rover[1] - 1
        if rover[1] < 0:
            rover = rover[0], len(matrix) - 1
        if matrix[rover[0]][rover[1]] in deposits:
            deposits_found[matrix[rover[0]][rover[1]]] += 1
            print(f"{deposits[matrix[rover[0]][rover[1]]]} found at {rover}")
        if matrix[rover[0]][rover[1]] == "R":
            print(f"Rover got broken at {rover}")
            break

    if command == "right":
        rover = rover[0], rover[1] + 1
        if rover[1] > len(matrix) - 1:
            rover = rover[0], 0
        if matrix[rover[0]][rover[1]] in deposits:
            deposits_found[matrix[rover[0]][rover[1]]] += 1
            print(f"{deposits[matrix[rover[0]][rover[1]]]} found at {rover}")
        if matrix[rover[0]][rover[1]] == "R":
            print(f"Rover got broken at {rover}")
            break

    if command == "up":
        rover = rover[0] - 1, rover[1]
        if rover[0] < 0:
            rover = len(matrix) - 1, rover[1]
        if matrix[rover[0]][rover[1]] in deposits:
            deposits_found[matrix[rover[0]][rover[1]]] += 1
            print(f"{deposits[matrix[rover[0]][rover[1]]]} found at {rover}")
        if matrix[rover[0]][rover[1]] == "R":
            print(f"Rover got broken at {rover}")
            break

    if command == "down":
        rover = rover[0] + 1, rover[1]
        if rover[0] > len(matrix) - 1:
            rover = 0, rover[1]
        if matrix[rover[0]][rover[1]] in deposits:
            deposits_found[matrix[rover[0]][rover[1]]] += 1
            print(f"{deposits[matrix[rover[0]][rover[1]]]} found at {rover}")
        if matrix[rover[0]][rover[1]] == "R":
            print(f"Rover got broken at {rover}")
            break



if deposits_found['W'] >= 1 and deposits_found['C'] >= 1 and deposits_found['M'] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

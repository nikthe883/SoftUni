rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input().split()

while command[0] != "END":
    # checks
    if "swap" not in command or len(command) != 5 or \
            int(command[1]) > rows and int(command[2]) > rows and int(command[3]) > cols and int(command[4]) > cols:

        print("Invalid input!")
    else:

        command_values = [int(x) for x in command[1:]]
        one, two, three, four = command_values
        matrix[one][two], matrix[three][four] = matrix[three][four], matrix[one][two]

        print('\n'.join(' '.join(map(str, i)) for i in matrix))

    command = input().split()

targets = [int(x) for x in input().split(" ")]

commands = input().split(" ")

while commands[0] != "End":

    indexes = int(commands[1])
    values = int(commands[2])

    if commands[0] == "Shoot":
        if 0 <= indexes < len(targets):
            get_target = targets[indexes]
            if get_target in targets:
                targets[indexes] -= values
                if targets[indexes] <= 0:
                    del targets[indexes]

    elif commands[0] == "Add":
        if 0 <= indexes < len(targets):
            targets.insert(indexes, values)

        else:
            print("Invalid placement!")

    elif commands[0] == "Strike":
        if 0 <= indexes < len(targets):
            if values <= indexes:

                indexes_to_delete_left = indexes - values
                indexes_to_delete_right = indexes + values

                del targets[indexes_to_delete_left:indexes_to_delete_right + 1]

            else:
                print("Strike missed!")

    commands = input().split(" ")

print("|".join(str(x) for x in targets))

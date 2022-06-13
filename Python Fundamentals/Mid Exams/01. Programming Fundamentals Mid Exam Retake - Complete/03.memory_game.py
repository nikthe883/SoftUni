elements = input().split(" ")
user_input = input()

number_of_moves = 0
while user_input != 'end':

    index1 = int(user_input.split(" ")[0])
    index2 = int(user_input.split(" ")[1])

    number_of_moves += 1

    if index1 == index2 or index1 < 0 or index2 > len(elements) or index2 >= len(elements) or index2 < 0:
        print("Invalid input! Adding additional elements to the board")
        new_value = "-" + str(number_of_moves) + "a"
        elements.insert(int(len(elements) / 2), new_value)
        elements.insert(int(len(elements) / 2), new_value)

    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[int(user_input[0])]}!")
        x = elements.pop(index1)
        elements.remove(x)


    elif index1 != index2:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

    user_input = input()

if len(elements) > 1:
    print("Sorry you lose :(\n"
          f"{' '.join(elements)}")

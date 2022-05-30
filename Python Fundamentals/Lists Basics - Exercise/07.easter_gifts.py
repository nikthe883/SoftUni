# list comprehension fo the input.
gifts = [x for x in input().split(" ")]

# inputs
command = input()

# making a copy of gifts
new_list = gifts
# while loop

while command != "No Money":
    # splitting the string.
    command_split = command.split(" ")
    # check
    if command_split[0] == "OutOfStock":
        # list comprehension : Put None if element is apple ( for example) else element is element in the list
        new_list = ["None" if el == command_split[1] else el for el in new_list]

    # again check
    elif command_split[0] == "Required":

        # check if the index will be out of range : if index is greater than 0 but smaller than length of the list do this.
        if 0 <= int(command_split[2]) < len(gifts):

            # Taking element at index whatever and changing it with the second part of the string
            new_list[int(command_split[2])] = command_split[1]

    # again check
    elif command_split[0] == "JustInCase":

        # getting the last element in the list and changing it accordingly.
        new_list[-1] = command_split[1]

    # again waiting for input
    command = input()

# printing basically I want to join every element in the list with white space if the element is not None
print(" ".join([x for x in new_list if x != "None"]))


inventory = input().split(", ")

command = input()

while command != "Craft!":

    command = command.split(" - ")

    if command[0] == "Collect":
        if command[1] not in inventory:
            inventory.append(command[1])
    elif command[0] == "Drop":
        if command[1] in inventory:
            inventory.remove(command[1])
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in inventory:
            index_old_item = inventory.index(old_item)
            inventory.insert(index_old_item + 1, new_item)
    elif command[0] == "Renew":
        if command[1] in inventory:
            index_item = inventory.index(command[1])
            item = inventory.pop(index_item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))

loots = input().split("|")

commands = input()

while commands != "Yohoho!":
    commands = commands.split(" ")
    if commands[0] == "Loot":
        for i in commands[1:]:
            if i not in loots:
                loots.insert(0, i)
    elif commands[0] == "Drop":
        if 0 <= int(commands[1]) < len(loots):
            item = loots.pop(int(commands[1]))
            loots.append(item)
    elif commands[0] == "Steal":

        if int(commands[1]) >= len(loots):
            print(", ".join(loots[-int(commands[1]):]))
            loots = []
        else:
            removed_items_index = [loots.index(x) for x in loots[-int(commands[1]):]]
            removed_items_index.reverse()
            removed_items = [loots.pop(x) for x in removed_items_index]
            removed_items.reverse()

            print(", ".join(removed_items))

    commands = input()

if len(loots) == 0:
    print("Failed treasure hunt.")
else:
    item_length = 0
    for i in loots:
        item_length += len(i)
    print(f"Average treasure gain: {(item_length / len(loots)):.2f} pirate credits.")

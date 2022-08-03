n = int(input())
plants = {}

for _ in range(n):
    update = input().split("<->")
    plants[update[0]] = {"rarity": update[1], "rating": []}


command = input().split(": ")

while command[0] != "Exhibition":
    if command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rating"].append(int(rating))
    elif command[0] == "Update":
        plant, rarity = command[1].split(" - ")
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rarity"] = rarity
    elif command[0] == "Reset":
        if command[1] not in plants:
            print("error")
        else:
            plants[command[1]]["rating"] = []

    command = input().split(": ")

print("Plants for the exhibition:")
for k in plants:

    if not plants[k]['rating']:
        total_rating = 0
    else:
        total_rating = sum(plants[k]['rating']) / len(plants[k]['rating'])
    print(f"- {k}; Rarity: {plants[k]['rarity']}; Rating: {total_rating:.2f}")
materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_obtained = False
user_input = input().lower().split()

while True:
    for index in range(0, len(user_input), 2):
        value = int(user_input[index])
        key = user_input[index + 1]

        if key in materials:
            materials[key] += value
        else:
            if not key in junk:
                junk[key] = 0
            junk[key] += value

        if materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            is_obtained = True
        elif materials["fragments"] >= 250:
            print("Valanyr obtained!")
            materials["fragments"] -= 250
            is_obtained = True
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            is_obtained = True

        if is_obtained:
            break
    if is_obtained:
        break

    command = input().lower().split()

for key, value in materials.items():
    print(f"{key}: {value}")

for useless_key, useless_value in junk.items():
    print(f"{useless_key}: {useless_value}")
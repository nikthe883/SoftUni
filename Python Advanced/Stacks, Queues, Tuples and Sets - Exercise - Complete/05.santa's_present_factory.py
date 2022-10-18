from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

presents = {"Bicycle": 0,
            "Doll": 0,
            "Teddy bear": 0,
            "Wooden train": 0}

while magic and materials:

    materials_last = materials.pop()
    magic_first = magic.popleft()

    if materials_last == 0 and magic_first == 0:
        continue
    if materials_last == 0:
        magic.appendleft(magic_first)
        continue
    if magic_first == 0:
        materials.append(materials_last)
        continue

    product = materials_last * magic_first

    if product < 0:
        the_sum = materials_last + magic_first
        materials.append(the_sum)
    elif product == 150:
        presents["Doll"] += 1
    elif product == 250:
        presents["Wooden train"] += 1
    elif product == 300:
        presents["Teddy bear"] += 1
    elif product == 400:
        presents["Bicycle"] += 1
    else:
        materials.append(materials_last + 15)

if presents["Doll"] >= 1 and presents["Wooden train"] >= 1 or presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

for k, v in presents.items():
    if v > 0:
        print(f"{k}: {v}")

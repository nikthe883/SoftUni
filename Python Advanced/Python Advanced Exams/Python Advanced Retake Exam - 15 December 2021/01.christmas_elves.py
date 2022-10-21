from collections import deque

elf_squad = deque(int(x) for x in input().split())
material_in_box = [int(x) for x in input().split()]

count = 1
gifts = 0
total_energy = 0
while elf_squad and material_in_box:


    energy = elf_squad.popleft()
    material = material_in_box.pop()

    if energy < 5:
        material_in_box.append(material)
        continue

    if energy >= material:
        if count % 3 == 0 and count % 5 == 0:
            material *= 2
            if energy >= material:
                energy -= material
                elf_squad.append(energy)
                total_energy += material
                continue
            else:
                energy *= 2
                elf_squad.append(energy)
                material //= 2
                material_in_box.append(material)

        if count % 3 == 0:
            material *= 2
            if energy >= material:
                energy -= material - 1
                elf_squad.append(energy)
                gifts += 2
                total_energy += material
            else:
                energy *= 2
                elf_squad.append(energy)
                material //= 2
                material_in_box.append(material)

        elif count % 5 == 0:
            if energy >= material:
                energy -= material
                elf_squad.append(energy)
                total_energy += material
            else:
                energy *= 2
                elf_squad.append(energy)
                material_in_box.append(material)

        else:
            energy -= material - 1
            elf_squad.append(energy)
            gifts += 1
            total_energy += material

    else:
        energy *= 2
        elf_squad.append(energy)
        material_in_box.append(material)
    count += 1

print(f"Toys: {gifts}")
print(f"Energy: {total_energy}")
if elf_squad:
    print(f"Elves left: {', '.join(str(x) for x in elf_squad)}")
if material_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in material_in_box)}")

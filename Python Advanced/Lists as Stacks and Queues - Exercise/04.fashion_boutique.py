clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
total_racks = 1
clothes_in_rack = 0

while clothes:
    new_cloth = clothes.pop()
    clothes_in_rack += new_cloth
    if clothes_in_rack == rack_capacity:
        if len(clothes) > 0:
            total_racks += 1
            clothes_in_rack = 0
    elif clothes_in_rack > rack_capacity:
        total_racks += 1
        clothes.append(new_cloth)
        clothes_in_rack = 0


print(total_racks)

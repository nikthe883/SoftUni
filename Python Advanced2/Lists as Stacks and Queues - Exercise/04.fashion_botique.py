
clothes = [int(x) for x in input().split()]

rack_cap = int(input())

number_of_racks = 1

curr_rack = rack_cap

while clothes:
    cloth = clothes.pop()
    
    if curr_rack >= cloth:
        curr_rack -= cloth
    else:
        number_of_racks += 1
        curr_rack = rack_cap
        curr_rack -= cloth

    

print(number_of_racks)       


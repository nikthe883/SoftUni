n = int(input())
car_plates = set([])

for i in range(n):
    action, number = input().split(", ")
    if action == "IN":
        car_plates.add(number)
    elif action == "OUT":
        car_plates.remove(number)

if car_plates:
    print(*car_plates, sep="\n")
else:
    print("Parking Lot is Empty")

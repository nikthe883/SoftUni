from collections import deque

pump_number = int(input())
pump_data = deque(input().split() for x in range(pump_number))


iterations = 0

for i in range(pump_number):

    iterations = i
    counter = 0
    liters = 0

    for x in pump_data:
        petrol, distance = x
        if liters + int(petrol) < int(distance):
            pump_data.append(pump_data.popleft())
            break
        else:
            liters += int(petrol) - int(distance)
            counter += 1

    if counter == pump_number:
        break

print(iterations)


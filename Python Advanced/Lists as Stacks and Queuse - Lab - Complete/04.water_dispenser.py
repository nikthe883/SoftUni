from collections import deque

queue = deque()

water_quantity = int(input())
command = input()

while command != "Start":
    queue.append(command)
    command = input()

if command == "Start":
    command_new = input()
    while command_new != "End":

        if "refill" in command_new:
            ref, liters = command_new.split()
            water_quantity += int(liters)
        else:
            if int(command_new) <= water_quantity:
                print(f"{queue.popleft()} got water")
                water_quantity -= int(command_new)
            else:
                print(f"{queue.popleft()} must wait")
        command_new = input()

print(f"{water_quantity} liters left")

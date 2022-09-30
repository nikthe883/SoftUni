from math import ceil


number_of_people = int(input())
elevator_capacity = int(input())

print(ceil(number_of_people / elevator_capacity))

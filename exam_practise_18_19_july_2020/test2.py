
# calc works spaces in room

# inputs

length_room = float(input()) # : w (дължина в метри)
width_room = float(input()) # h (широчина в метри).

# variables in meters

corridor = 1
work_place_width = 0.7
work_place_length = 1.20

# occupied workplaces by door and teacher desk

door = 1
teacher_desk = 2

# calculations

total_work_places_width = (width_room - corridor) // work_place_width
total_work_places_length = length_room // work_place_length
total_workplaces =(total_work_places_width * total_work_places_length) - (door + teacher_desk)

# output

print(total_workplaces)
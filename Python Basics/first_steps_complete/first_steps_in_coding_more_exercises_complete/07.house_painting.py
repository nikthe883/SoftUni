
# inputs

house_height = float(input())
house_length = float(input())
roof_height = float(input())

# variables

green_paint_cost_per_sqm = 3.4
red_paint_cost_per_sqm = 4.3

door_height = 2
door_width = 1.2
window_side_a = 1.5

# calculations

# house area


door_area = door_height * door_width
window_area = window_side_a * window_side_a
house_front_area = house_height * house_height - door_area
house_back_area = house_height * house_height
house_sides_area = (house_height * house_length - window_area) * 2
total_house_area = house_sides_area + house_front_area + house_back_area

# rood area

roof_sides_area = house_height * house_length * 2
roof_front_back_area = 2 * (house_height * roof_height / 2)
total_roof_area = roof_sides_area + roof_front_back_area

# paint needed

total_green_paint_needed = total_house_area / green_paint_cost_per_sqm
total_red_paint_needed = total_roof_area / red_paint_cost_per_sqm

# output

print(f"{total_green_paint_needed:.2f}\n"
      f"{total_red_paint_needed:.2f}")

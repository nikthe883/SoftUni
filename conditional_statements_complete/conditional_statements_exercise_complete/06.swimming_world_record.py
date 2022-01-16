# app
import math

world_record = float(input())
distance_to_swim = float(input())
time_per_meter = float(input())

water_resistance_meters = 15
water_resistance_seconds = 12.5

a = distance_to_swim * time_per_meter
b = math.floor(distance_to_swim / water_resistance_meters) * water_resistance_seconds
total_time = a + b


if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

elif total_time >= world_record:
    time_needed = total_time - world_record
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")




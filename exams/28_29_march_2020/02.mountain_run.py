
from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter_per_second = float(input())

total_seconds_drawback = floor((distance_in_meters / 50 )) * 30

georges_attempt = distance_in_meters * time_for_one_meter_per_second + total_seconds_drawback

if georges_attempt < record_in_seconds:
    print(f"Yes! The new record is {georges_attempt:.2f} seconds.")
else:
    left = georges_attempt - record_in_seconds
    print(f"No! He was {left:.2f} seconds slower.")

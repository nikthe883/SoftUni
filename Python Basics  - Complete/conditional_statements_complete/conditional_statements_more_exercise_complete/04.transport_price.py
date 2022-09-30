
# inputs

km_to_travel = int(input())
day_n_night = input()

# variables

taxi_initial_price = 0.7
taxi_day_cost_per_km = 0.79
taxi_night_cost_per_km = 0.90

bus_day_n_night_cost_per_km = 0.09
train_day_n_night_cost_per_km = 0.06

minimum_bus_travel_distance_km = 20
minimum_train_travel_distance_km = 100

cheapest_price = 0

# calculations

if km_to_travel < minimum_bus_travel_distance_km:
    if day_n_night == "day":
        cheapest_price = taxi_initial_price + taxi_day_cost_per_km * km_to_travel
    else:
        cheapest_price = taxi_initial_price + taxi_night_cost_per_km * km_to_travel

elif minimum_train_travel_distance_km > km_to_travel >= minimum_bus_travel_distance_km:
    cheapest_price = bus_day_n_night_cost_per_km * km_to_travel

elif km_to_travel >= minimum_train_travel_distance_km:
    cheapest_price = train_day_n_night_cost_per_km * km_to_travel

# output

print(f'{cheapest_price:.2f}')

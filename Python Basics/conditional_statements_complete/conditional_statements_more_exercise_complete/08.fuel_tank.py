
# inputs

fuel_type = input()
liters_of_fuel = int(input())

# variables

enough_fuel_l = 25

# desicions

if fuel_type == "Diesel":
    if liters_of_fuel >= enough_fuel_l:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")

elif fuel_type == "Gasoline":
    if liters_of_fuel >= enough_fuel_l:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")

elif fuel_type == "Gas":
    if liters_of_fuel >= enough_fuel_l:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")

else:
    print("Invalid fuel!")

n = int(input())

cars = {}

for _ in range(n):
    user_input = input().split("|")
    cars[user_input[0]] = {"mileage": int(user_input[1]), "fuel": int(user_input[2])}

commands = input().split(" : ")

while commands[0] != "Stop":
    if commands[0] == "Drive":
        if cars[commands[1]]['fuel'] < int(commands[3]):
            print("Not enough fuel to make that ride")
        else:
            cars[commands[1]]['mileage'] += int(commands[2])
            cars[commands[1]]['fuel'] -= int(commands[3])
            print(f"{commands[1]} driven for {commands[2]} kilometers. {commands[3]} liters of fuel consumed.")

        if cars[commands[1]]['mileage'] >= 100_000:
            print(f"Time to sell the {commands[1]}!")
            del cars[commands[1]]

    elif commands[0] == "Refuel":
        remaining_tank = 75 - cars[commands[1]]['fuel']
        cars[commands[1]]['fuel'] += int(commands[2])

        if cars[commands[1]]['fuel'] > 75:
            print(f"{commands[1]} refueled with {remaining_tank} liters")

            cars[commands[1]]['fuel'] = 75
        else:
            print(f"{commands[1]} refueled with {commands[2]} liters")


    elif commands[0] == "Revert":
        cars[commands[1]]['mileage'] -= int(commands[2])
        if cars[commands[1]]['mileage'] < 10_000:
            cars[commands[1]]['mileage'] = 10_000
        else:
            print(f"{commands[1]} mileage decreased by {commands[2]} kilometers")

    commands = input().split(" : ")

for k in cars:
    print(f"{k} -> Mileage: {cars[k]['mileage']} kms, Fuel in the tank: {cars[k]['fuel']} lt.")


number_joinery = int(input())
joinery_type = input()
delivery_type = input()

total_price = 0



if joinery_type == "90X130":
    total_price += 110 * number_joinery
    if 60 > number_joinery > 30:
        total_price *= 0.95
    elif number_joinery > 60:
        total_price *= 0.92

if joinery_type == "100X150":
    total_price += 140 * number_joinery
    if 80 > number_joinery > 40:
        total_price *= 0.94
    elif number_joinery > 80:
        total_price *= 0.90

if joinery_type == "130X180":
    total_price += 190 * number_joinery
    if 50 > number_joinery > 20:
        total_price *= 0.93
    elif number_joinery > 50:
        total_price *= 0.88

if joinery_type == "200X300":
    total_price += 250 * number_joinery
    if 50 > number_joinery > 25:
        total_price *= 0.91
    elif number_joinery > 50:
        total_price *= 0.86

if delivery_type == "With delivery":
    total_price += 60

if number_joinery > 99:
    total_price *= 0.96


if number_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")

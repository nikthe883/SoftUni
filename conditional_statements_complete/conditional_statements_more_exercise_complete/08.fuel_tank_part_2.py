
# inputs

fuel_type = input()
fuel_pumped_l = float(input())
club_card = input()


# prices

gasoline_price_per_l = 2.22
diesel_price_per_l = 2.33
gas_price_per_l = 0.93

# club card discount

discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08

club_card_price_gasoline_l = gasoline_price_per_l - discount_gasoline
club_card_price_diesel_l = diesel_price_per_l - discount_diesel
club_card_price_gas_l = gas_price_per_l - discount_gas

# higher volume discounts

from_20_to_25_l_discount_percentage = 0.08
above_25_discount_percentage = 0.1

total_fuel_price = 0

# decisions

if fuel_type == "Gasoline":
    total_fuel_price = gasoline_price_per_l * fuel_pumped_l
    if club_card == "Yes":
        total_fuel_price = club_card_price_gasoline_l * fuel_pumped_l
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)
    else:
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)

elif fuel_type == "Diesel":
    total_fuel_price = diesel_price_per_l * fuel_pumped_l
    if club_card == "Yes":
        total_fuel_price = club_card_price_diesel_l * fuel_pumped_l
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)
    else:
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)

elif fuel_type == "Gas":
    total_fuel_price = gas_price_per_l * fuel_pumped_l
    if club_card == "Yes":
        total_fuel_price = club_card_price_gas_l * fuel_pumped_l
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)
    else:
        if 20 <= fuel_pumped_l <= 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * from_20_to_25_l_discount_percentage)
        elif fuel_pumped_l > 25:
            total_fuel_price = total_fuel_price - (total_fuel_price * above_25_discount_percentage)


# output

print(f"{total_fuel_price:.2f} lv.")

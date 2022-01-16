
# too many vars
# inputs

chrysanthemums_input = int(input())
roses_input = int(input())
tulips_input = int(input())
season = input()
is_it_holiday = input()

# variables

# flower prices plus arranging
spring_summer_chrysanthemums_price = 2
fall_winter_chrysanthemums_price = 3.75

spring_summer_roses_price = 4.10
fall_winter_roses_price = 4.50

spring_summer_tulips_price = 2.50
fall_winter_tulips_price = 4.15

arranging_price = 2
# discounts in percentage

above_seven_tulips_spring = 0.05
above_ten_roses_winter = 0.10
above_twenty_flowers_all_seasons = 0.20

# discounts variables
number_tulips_for_discount = 7
number_roses_for_discount = 10
total_number_flowers_for_discount = 20

# if it is holiday
over_price = 0.15

# variable for the price with no arranging
total_price_no_arranging = 0

# total_number_of flowers
total_number_flowers = tulips_input + chrysanthemums_input + roses_input

# decisions

if season == "Spring":

    total_price_chrysanthemums = chrysanthemums_input * spring_summer_chrysanthemums_price
    total_price_roses = roses_input * spring_summer_roses_price
    total_price_tulips = tulips_input * spring_summer_tulips_price
    total_price_no_arranging = total_price_tulips + total_price_roses + total_price_chrysanthemums

    if is_it_holiday == "Y":
        total_price_no_arranging += over_price * total_price_no_arranging
        if tulips_input > number_tulips_for_discount:
            total_price_no_arranging -= above_seven_tulips_spring * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging
    else:
        if tulips_input > number_tulips_for_discount:
            total_price_no_arranging -= above_seven_tulips_spring * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging

elif season == "Summer":

    total_price_chrysanthemums = chrysanthemums_input * spring_summer_chrysanthemums_price
    total_price_roses = roses_input * spring_summer_roses_price
    total_price_tulips = tulips_input * spring_summer_tulips_price
    total_price_no_arranging = total_price_tulips + total_price_roses + total_price_chrysanthemums

    if is_it_holiday == "Y":
        total_price_no_arranging += over_price * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging
    else:
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging

elif season == "Autumn":

    total_price_chrysanthemums = chrysanthemums_input * fall_winter_chrysanthemums_price
    total_price_roses = roses_input * fall_winter_roses_price
    total_price_tulips = tulips_input * fall_winter_tulips_price
    total_price_no_arranging = total_price_tulips + total_price_roses + total_price_chrysanthemums

    if is_it_holiday == "Y":
        total_price_no_arranging += over_price * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging
    else:
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging

if season == "Winter":

    total_price_chrysanthemums = chrysanthemums_input * fall_winter_chrysanthemums_price
    total_price_roses = roses_input * fall_winter_roses_price
    total_price_tulips = tulips_input * fall_winter_tulips_price
    total_price_no_arranging = total_price_tulips + total_price_roses + total_price_chrysanthemums

    if is_it_holiday == "Y":
        total_price_no_arranging += over_price * total_price_no_arranging
        if roses_input >= number_roses_for_discount:
            total_price_no_arranging -= above_ten_roses_winter * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging
    else:
        if roses_input >= number_roses_for_discount:
            total_price_no_arranging -= above_ten_roses_winter * total_price_no_arranging
        if total_number_flowers > total_number_flowers_for_discount:
            total_price_no_arranging -= above_twenty_flowers_all_seasons * total_price_no_arranging



total_price = total_price_no_arranging + arranging_price

# output
print(f"{total_price:.02f}")



# inputs

flower = input()
flower_number = int(input())
budget = int(input())

# variables

single_rose_price = 5
single_dahlias_price = 3.80
single_tulip_price = 2.80
single_narcissus_price = 3
single_gladiolus_price = 2.50

total_price = 0

if flower == "Roses":
    if flower_number > 80:
        total_price = flower_number * single_rose_price - ((flower_number * single_rose_price) * 0.1)
    else:
        total_price = flower_number * single_rose_price

elif flower == "Dahlias":
    if flower_number > 90:
        total_price = flower_number * single_dahlias_price - ((flower_number * single_dahlias_price) * 0.15)
    else:
        total_price = flower_number * single_dahlias_price

elif flower == "Tulips":
    if flower_number > 80:
        total_price = flower_number * single_tulip_price - ((flower_number * single_tulip_price) * 0.15)
    else:
        total_price = flower_number * single_tulip_price

elif flower == "Narcissus":
    if flower_number < 120:
        total_price = flower_number * single_narcissus_price + ((flower_number * single_narcissus_price) * 0.15)
    else:
        total_price = flower_number * single_narcissus_price

elif flower == "Gladiolus":
    if flower_number < 80:
        total_price = flower_number * single_gladiolus_price + ((flower_number * single_gladiolus_price) * 0.20)
    else:
        total_price = flower_number * single_gladiolus_price


if total_price <= budget:
    left_money = budget - total_price
    print(f"Hey, you have a great garden with {flower_number} {flower} and {left_money:.2f} leva left.")
else:
    need_money = total_price - budget
    print(f"Not enough money, you need {need_money:.2f} leva more.")


# inputs

number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegetarian_menus = int(input())


# variables

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50
desert_percentage_price = 0.2

# calculations

total_price_menus = chicken_menu_price * number_chicken_menus + \
                fish_menu_price * number_fish_menus + \
                vegetarian_menu_price * number_vegetarian_menus

desert_price = total_price_menus * desert_percentage_price

total_price = total_price_menus + desert_price + delivery_price

# output

print(total_price)

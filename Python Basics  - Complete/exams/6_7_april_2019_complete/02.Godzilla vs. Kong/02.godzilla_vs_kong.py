
# inputs

film_budget = float(input())
number_statist = int(input())
statist_clothing_price = float(input())

# variables

film_decor_percentage_cost = 0.1
statist_clothing_price_percentage_discount = 0.1
total_price_statists_clothing = number_statist * statist_clothing_price
money_film_decor = film_budget * film_decor_percentage_cost


# Check for discount in clothing
if number_statist >= 150:
    total_price_statists_clothing = total_price_statists_clothing - (total_price_statists_clothing * statist_clothing_price_percentage_discount)


# declare var expences
expenses = total_price_statists_clothing + money_film_decor

# Film or not film
if expenses > film_budget:
    money = expenses - film_budget
    print(f"Not enough money!\n"
          f"Wingard needs {money:.2f} leva more.")
else:
    money = film_budget - expenses
    print(f"Action!\n"
          f"Wingard starts filming with {money:.2f} leva left.")


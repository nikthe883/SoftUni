
drink = input()
sugar = input()
number_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = number_drinks * 0.90 * 0.65
    elif sugar == "Normal":
        price = number_drinks * 1
    elif sugar == "Extra":
        price = number_drinks * 1.20

elif drink == "Cappuccino":
    if sugar == "Without":
        price = number_drinks * 1 * 0.65
    elif sugar == "Normal":
        price = number_drinks * 1.20
    elif sugar == "Extra":
        price = number_drinks * 1.60

else:
    if sugar == "Without":
        price = number_drinks * 0.50 * 0.65
    elif sugar == "Normal":
        price = number_drinks * 0.60
    elif sugar == "Extra":
        price = number_drinks * 0.70

if drink == "Espresso" and number_drinks >= 5:
    price *= 0.75

if price > 15:
    price *= 0.80

print(f"You bought {number_drinks} cups of {drink} for {price:.2f} lv.")

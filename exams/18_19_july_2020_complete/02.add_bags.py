
price_luggage_above_twenty = float(input())
kg_luggage = float(input())
days_till_travel = int(input())
luggage_number = int(input())


price_luggage = price_luggage_above_twenty

if kg_luggage < 10:
    price_luggage *= 0.20
elif 10 <= kg_luggage <= 20:
    price_luggage *= 0.50

if days_till_travel > 30:
    price_luggage *= 1.10

elif 7 <= days_till_travel <= 30:
    price_luggage *= 1.15
else:
    price_luggage *= 1.40

print(f"The total price of bags is: {price_luggage * luggage_number:.2f} lv.")

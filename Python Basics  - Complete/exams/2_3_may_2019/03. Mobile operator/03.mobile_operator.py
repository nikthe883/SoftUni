
contract_time = input()
contract_type = input()
mobile_net = input()
payments_months = int(input())

price = 0

if contract_time == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99
else:
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if mobile_net == "yes":
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

total_price = price * payments_months

if contract_time == "two":
    total_price *= 0.9625

print(f"{total_price:.2f} lv.")

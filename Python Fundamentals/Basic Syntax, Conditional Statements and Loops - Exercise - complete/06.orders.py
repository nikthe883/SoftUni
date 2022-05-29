
orders = int(input())
total = 0

for i in range(orders):
    price = float(input())
    days = int(input())
    count = int(input())
    if price < 0.01 or price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif count < 1 or count > 2000:
        continue
    total_price = price * days * count
    total += total_price
    print(f"The price for the coffee is: ${total_price:.2f}")

print(f"Total: ${total:.2f}")

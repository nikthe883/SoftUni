
orders = int(input())
total = 0

for i in range(orders):
    price = float(input())
    days = int(input())
    count =  int(input())
    total_price = price * days * count
    total += total_price
    print(f"The price for the coffee is: ${total_price:.2f}")

print(f"Total: ${total:.2f}")

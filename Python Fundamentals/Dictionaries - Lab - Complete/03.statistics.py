user_input = input().split(": ")

products = {}

while user_input[0] != "statistics":
    if user_input[0] not in products:
        products[user_input[0]] = 0
    products[user_input[0]] += int(user_input[1])
    user_input = input().split(": ")

print("Products in stock:")

for k, v in products.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

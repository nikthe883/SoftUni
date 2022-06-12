user_choice = input()
quantity = int(input())

AVAILABLE_PRODUCTS = {"coffee": 1.50,
                      "coke": 1.40,
                      "water": 1.00,
                      "snacks": 2.00}


def total_price(user_product, quantity):
    for product, price in AVAILABLE_PRODUCTS.items():
        if product == user_product:
            total_product_price = price * quantity
            print(f'{total_product_price:.2f}')


total_price(user_choice, quantity)

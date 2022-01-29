
number_clients = int(input())

total_price = 0
total_client_price = 0
number_products = 0

for i in range(number_clients):

    purchase = input()

    while purchase != "Finish":
        number_products += 1
        if purchase == "basket":
            total_client_price += 1.50
        elif purchase == "wreath":
            total_client_price += 3.80
        elif purchase == "chocolate bunny":
            total_client_price += 7
        purchase = input()

    if number_products % 2 == 0:
        total_client_price *= 0.80

    print(f"You purchased {number_products} items for {total_client_price:.2f} leva.")

    total_price += total_client_price
    total_client_price = 0
    number_products = 0

average = total_price / number_clients
print(f"Average bill per client is: {average:.2f} leva.")

expected_sales = int(input())
counter = 0
gathered_sum_cash = 0
gathered_sum_card = 0
sold_counter_cash = 0
sold_counter_card = 0
total_sum = 0

while total_sum < expected_sales:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        break

    item_price = int(command)
    counter += 1

    if counter % 2 == 0:
        if item_price < 10:
            print("Error in transaction!")
        else:
            gathered_sum_card += item_price
            sold_counter_card += 1
            print("Product sold!")
    else:
        if item_price > 100:
            print("Error in transaction!")
        else:
            gathered_sum_cash += item_price
            sold_counter_cash += 1
            print("Product sold!")

    total_sum = gathered_sum_cash + gathered_sum_card


if total_sum >= expected_sales:
    print(f'Average CS: {gathered_sum_cash / sold_counter_cash:.2f}')
    print(f'Average CC: {gathered_sum_card / sold_counter_card:.2f}')
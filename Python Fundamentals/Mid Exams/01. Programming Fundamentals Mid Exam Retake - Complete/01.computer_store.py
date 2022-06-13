user_input = input()

total_price_no_taxes = 0
total_price_with_taxes = 0
total_taxes = 0
discount = 0.1
taxes = 0.2

while True:
    if user_input == "special":
        total_price_with_taxes = total_price_with_taxes - total_price_with_taxes * discount
        break
    elif user_input == 'regular':
        break

    if float(user_input) < 0:
        print('Invalid price!')


    else:
        total_taxes += float(user_input) * taxes
        total_price_no_taxes += float(user_input)
        total_price_with_taxes += float(user_input) + float(user_input) * taxes
    user_input = input()

if total_price_with_taxes > 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_no_taxes:.2f}$\n"
          f"Taxes: {total_taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$")
else:
    print("Invalid order!")


total_amount = 0

run = True

while run:
    money = input()

    if money == "NoMoreMoney":
        print(f'Total: {total_amount:.2f}')
        run = False

    elif float(money) < 0:
        print("Invalid operation!")
        print(f'Total: {total_amount:.2f}')
        run = False

    else:
        total_amount += float(money)
        print(f'Increase: {float(money):.2f}')



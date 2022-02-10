from decimal import Decimal
shopping_money = Decimal(input())
purchases = 0

command = input()
while command != "mall.Enter":
    command = input()
command = input()


while command != "mall.Exit":
    for s in command:
        p = False
        if s.isupper():
            price = ord(s) * Decimal("0.5")
            if shopping_money < price:
                continue
            shopping_money -= price
            p = True

        elif s.islower():
            price = ord(s) * Decimal("0.3")
            if shopping_money < price:
                continue
            shopping_money -= price
            p = True

        elif s == "%":
            price = shopping_money / 2
            if shopping_money <= price:
                continue
            shopping_money -= price
            p = True


        elif s == "*":
            shopping_money += 10

        else:
            price = ord(s)
            if shopping_money < price:
                continue
            shopping_money -= price
            p = True

        if p:
            purchases += 1

    command = input()

if purchases > 0:
    print(f"{purchases} purchases. Money left: {shopping_money:.2f} lv.")
else:
    print(f"No purchases. Money left: {shopping_money:.2f} lv.")



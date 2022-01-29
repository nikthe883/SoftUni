
desired_money = float(input())

earned_money = 0

while earned_money < desired_money:

    drink_name = input()
    price = 0
    if drink_name == "Party!":
        print(f"We need {desired_money - earned_money:.2f} leva more.")
        break
    drink_number = int(input())
    price += len(drink_name) * drink_number
    if price % 2 != 0:
        price *= 0.75

    earned_money += price


if earned_money >= desired_money:
    print("Target acquired.")

print(f"Club income - {earned_money:.2f} leva.")

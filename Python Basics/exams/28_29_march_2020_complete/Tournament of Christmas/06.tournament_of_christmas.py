
n = int(input())
money = 0
wins = 0
loses = 0
win_days = 0
loose_days = 0

for i in range(n):
    money_for_day = 0
    wins = 0
    loses = 0
    sport = input()

    while sport != "Finish":

        result = input()
        if result == "win":
            money_for_day += 20
            wins += 1
        else:
            loses += 1

        sport = input()

    if wins > loses:
        win_days += 1
        money_for_day *= 1.10
    else:
        loose_days += 1

    money += money_for_day

if win_days > loose_days:
    money *= 1.20

if win_days > loose_days:
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")

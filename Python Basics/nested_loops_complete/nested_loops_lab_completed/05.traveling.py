


destination = input()

while destination != "End":
    budget = float(input())
    needed_money = 0
    while budget > needed_money:
        input_money = float(input())
        needed_money += input_money
    print(f'Going to {destination}!')
    destination = input()


player_name = input()

total_points = 301
field = input()
fail = 0
win = 0

while field != "Retire":

    points = int(input())
    if field == "Single":
        total_points -= points
        if total_points < 0:
            total_points += points
            fail += 1
        else:
            win += 1
    elif field == "Double":
        total_points -= points * 2
        if total_points < 0:
            total_points += points * 2
            fail += 1
        else:
            win += 1
    elif field == "Triple":
        total_points -= points * 3
        if total_points < 0:
            total_points += points * 3
            fail += 1
        else:
            win += 1
    if total_points == 0:
        print(f"{player_name} won the leg with {win} shots.")
        break

    field = input()

if field == "Retire":
    print(f"{player_name} retired after {fail} unsuccessful shots.")

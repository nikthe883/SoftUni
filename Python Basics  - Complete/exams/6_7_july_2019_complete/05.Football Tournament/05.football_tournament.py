football_team_name = input()
number_matches = int(input())

points = 0
w = 0
d = 0
l = 0

for i in range(number_matches):

    result = input()
    if result == "W":
        points += 3
        w += 1
    elif result == "D":
        points += 1
        d += 1
    elif result == "L":
        l += 1

if number_matches == 0:
    print(f"{football_team_name} hasn't played any games during this season.")
else:
    print(f"{football_team_name} has won {points} points during this season.\n"
          f"Total stats:\n"
          f"## W: {w}\n"
          f"## D: {d}\n"
          f"## L: {l}\n"
          f"Win rate: {w / number_matches * 100:.2f}%"
          )

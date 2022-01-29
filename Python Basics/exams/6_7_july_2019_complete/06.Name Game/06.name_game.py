
winner = ""
total_points = 0

while True:
    name_player = input()
    points = 0
    if name_player == "Stop":
        break

    for i in name_player:
        number = int(input())
        if ord(i) == number:
            points += 10
        else:
            points += 2

    if total_points <= points:
        total_points = points
        winner = name_player

print(f"The winner is {winner} with {total_points} points!")

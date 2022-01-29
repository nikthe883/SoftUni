import math

number_tournaments = int(input())
initial_points = int(input())

total_points = 0
wins = 0

for i in range(number_tournaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

wins_percentage = wins / number_tournaments * 100
average_points = math.floor(total_points / number_tournaments)

print(f"Final points: {total_points + initial_points}\n"
      f"Average points: {average_points}\n"
      f"{wins_percentage:.2f}%")

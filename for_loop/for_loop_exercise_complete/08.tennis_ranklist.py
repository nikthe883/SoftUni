
number_tournaments_participations = int(input())
starting_points_rank_list = int(input())

points = 0
total_participations = 0
total_tournaments_won = 0

for _ in range(number_tournaments_participations):
    tournament_outcome = input()
    total_participations += 1

    if tournament_outcome == "W":
        points += 2000
        total_tournaments_won += 1
    elif tournament_outcome == "F":
        points += 1200
    else:
        points += 720

final_points = points + starting_points_rank_list
average_points = points / total_participations
average_win_rate = total_tournaments_won / total_participations * 100

print(f"Final points: {final_points}\n"
      f"Average points: {int(average_points)}\n"
      f"{average_win_rate:.02f}%")

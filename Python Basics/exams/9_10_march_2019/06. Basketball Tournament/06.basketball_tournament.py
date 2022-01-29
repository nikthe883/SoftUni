
name_tournament = input()
wins = 0
losses = 0
total_matches = 0
while name_tournament != "End of tournaments":

    number_games = int(input())

    for i in range(1, number_games + 1):
        total_matches += 1
        team_desi = int(input())
        team_two = int(input())
        if team_desi > team_two:
            print(f"Game {i} of tournament {name_tournament}: win with {abs(team_two - team_desi)} points.")
            wins += 1
        else:
            print(f"Game {i} of tournament {name_tournament}: lost with {abs(team_two - team_desi)} points.")
            losses += 1

    name_tournament = input()

print(f"{wins/ total_matches * 100:.2f}% matches win\n"
        f"{losses/ total_matches * 100:.2f}% matches lost")

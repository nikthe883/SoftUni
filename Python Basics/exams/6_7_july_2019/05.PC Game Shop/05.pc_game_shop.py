sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(sold_games):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {hearthstone / sold_games * 100:.2f}%\n"
      f"Fornite - {fornite / sold_games * 100:.2f}%\n"
      f"Overwatch - {overwatch / sold_games * 100:.2f}%\n"
      f"Others - {others / sold_games * 100:.2f}%"
      )

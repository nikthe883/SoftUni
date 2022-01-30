player_one = input()
player_two = input()

player_one_points = 0
player_two_points = 0

while True:
    player_one_draw = input()
    if player_one_draw == "End of game":
        print(f"{player_one} has {player_one_points} points\n"
              f"{player_two} has {player_two_points} points")
        break
    player_two_draw = input()

    if int(player_one_draw) > int(player_two_draw):
        player_one_points += int(player_one_draw) - int(player_two_draw)
    elif int(player_one_draw) < int(player_two_draw):
        player_two_points += int(player_two_draw) - int(player_one_draw)
    else:
        print("Number wars!")
        player_one_draw = input()
        player_two_draw = input()
        if int(player_one_draw) > int(player_two_draw):
            print(f"{player_one} is winner with {player_one_points} points")
            break
        elif int(player_one_draw) < int(player_two_draw):
            print(f"{player_two} is winner with {player_two_points} points")
            break

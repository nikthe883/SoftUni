
player_one_eggs = int(input())
player_two_eggs = int(input())

win = input()

while win != "End of battle":

    if win == "one":
        player_two_eggs -= 1
    elif win == "two":
        player_one_eggs -= 1

    if player_one_eggs <= 0:
        print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
        break
    elif player_two_eggs <= 0:
        print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
        break

    win = input()

if win == "End of battle":
    print(f"Player one has {player_one_eggs} eggs left.\n"
    	f"Player two has {player_two_eggs} eggs left.")

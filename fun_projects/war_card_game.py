

# NEED MORE WORK
# text based game on the war card game
# up to 4 players

# imports

import random
import numpy as np

# main menu

def main_menu():
    print("\n"
          "================\n"
          "     MAIN MENU    \n"
          "=================\n"
          "\n"
          "1.Number of players.\n"
          "2.Play Game\n"
          "3.Rules"
          "4.Exit\n")

    options = input("Choose from 1 to 3")

    if options == "1":
        number_of_players_and_name()
    elif options == "2":
        pass
     #   start_game()
    elif options == "3":
        pass
      #  game_rules()
    elif options == "4":
        exit()
    else:
        print("Please make a valid input.")



# choosing number of players and their names


def number_of_players_and_name():
    players = {}
    num_players = input("Choose number of from 2 to 4.\n")
    if num_players not in  ["2", "3", "4"]:
        print("Please put the number of players. Thanks !")

    else:


        name = True
        while name:

            for i in range(int(num_players) + 1):
                if i == 0:
                    pass
                else:
                    player_name = input(f"\nPick a name for Player{i} : ")
                    if player_name != "":
                        print(f"Your name is {player_name}.\n"
                              f"==================")
                        players[player_name] = 0
                    else:
                        print(f"You will stick with Player{i}.\n"
                              f"==================")
                        players[f"Player{i}"] = 0
            name = False

        return players

def deck_shuffle():
    # we are creating the deck, shuffle it and give values to the cards.

    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    deck = card_values * 4
    random.shuffle(deck)

    return deck

def war(deck,num_players, players):



    # giving each player points 1 card is 1 point

    if players is None:
        pass
    else:
        for i in range(num_players):
            for k,v in players.items():
                players[k] = (len(deck) // num_players)

    # splitting the deck for the players

    deck_split = np.array_split(deck,num_players)
    print(deck_split)


    player1 = deck_split[0].tolist()

    player2 = deck_split[1].tolist()

    if len(deck_split) > 2:
        player3 = deck_split[2].tolist()

    else:
        player3 = [0,0]
    if len(deck_split) > 3:
        player4 = deck_split[3].tolist()

    else:
        player4 = [0,0]




    last_stand = False

    while not last_stand:



        highest_card = max(player1[0],player2[0])
      #  highest_card = max(player1[0], max(player2[0], max(player3[0], player4[0])))

        if player1[0] > player2[0]:
            to_add = [player2[0]]
            player1.extend(to_add)
            player2.pop(0)

        else:
            to_add = [player1[0]]
            player2.extend(to_add)
            player1.pop(0)
        # if highest_card == player1[0]:
        #     to_add = [player2[0]]
        #     player1.extend(player2[0])
        #     player2.pop(0)
        #
        #
        #
        #
        # elif highest_card == player2[0]:
        #     to_add = [player1[0]]
        #     player2.extend(to_add)
        #     player1.pop(0)


        # elif highest_card == player3[0]:
        #     to_add = [player2[0], player1[0], player4[0]]
        #     player3.extend(to_add)
        #     player2[0] = 0
        #     player1[0] = 0
        #     player4[0] = 0
        #
        # elif highest_card == player4[0]:
        #     to_add = [player2[0], player3[0], player1[0]]
        #     player4.extend(to_add)
        #     player2[0] = 0
        #     player3[0] = 0
        #     player1[0] = 0



        print(f'{highest_card}, players cards {player1[0]} {player2[0]} {player3} {player4}')
        print(f'Player 1 : {player1}, Player 2 : {player2}, Player 3 : {player3} ,Player 4 : {player4} ')

        player1 = [player1[-1]] + player1[:-1]
        player2 = [player2[-1]] + player2[:-1]
    #    player3 = [player3[-1]] + player3[:-1]
      #  player4 = [player4[-1]] + player4[:-1]


        if sum(player1) > 400:
            print("Player1 won")
            last_stand = True
        elif sum(player2) > 400:
            print("Player2 won")
            last_stand = True
        elif sum(player3) == 104:
            print("Player3 won")
            last_stand = True
        elif sum(player4) == 104:
            print("Player4 won")
            last_stand = True



if __name__ == "__main__":
    players = number_of_players_and_name()


    deck = deck_shuffle()
    opa = war(deck,2,players)




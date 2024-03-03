from project.player import Player

class Team:

    def __init__(self, name, rating) -> None:
        self.__players = []
        self.__name = name
        self.__rating = rating

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"
    
    def remove_player(self, player_name):
        for i ,name in enumerate(self.__players):
            if player_name == name.name:
                return self.__players.pop(i)
        return f"Player {player_name} not found"
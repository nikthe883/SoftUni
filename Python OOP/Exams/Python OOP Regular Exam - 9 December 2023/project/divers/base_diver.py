from abc import ABC, abstractmethod


class BaseDiver(ABC):

    def __init__(self,name, oxygen_level):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0
        self.has_health_issue = False

    @abstractmethod
    def miss(self,time_to_catch):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    
    def hit(self,fish):
        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points = round(fish.points + self.competition_points , 1)
        else:
            self.oxygen_level = 0
        


    def update_health_status(self):
        if self.has_health_issue:
            self.has_health_issue = False
        else:
            self.has_health_issue = True

    def __str__(self) -> str:
        return f"{type(self).__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
    
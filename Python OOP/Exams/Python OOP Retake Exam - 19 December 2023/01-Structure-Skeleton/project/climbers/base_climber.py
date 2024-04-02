from abc import ABC, abstractmethod


class BaseClimber (ABC):


    def __init__(self, name, strengtht):
        self.name = name
        self.strengtht = strengtht
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value


    @property
    def strengtht(self):
        return self.__strengtht
    
    @strengtht.setter
    def strengtht(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self):
        pass

    def rest(self):
        self.strengtht += 15

    def __str__(self) -> str:
        conquered_peaks = sorted(self.conquered_peaks)
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered " \
               f"peaks: {', '.join(conquered_peaks)} ///"
        
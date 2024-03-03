from .animal import Animal

class Lion(Animal):
    
    DEFAULT_MONEY_FOR_CARE = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.DEFAULT_MONEY_FOR_CARE )
        self.money_for_care = self.DEFAULT_MONEY_FOR_CARE
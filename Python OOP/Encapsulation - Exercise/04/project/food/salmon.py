from .main_dish import MainDish

class Salmon(MainDish):

    GRAMS = 22

    def __init__(self, name, price) -> None:
        super().__init__(name, price, self.GRAMS)
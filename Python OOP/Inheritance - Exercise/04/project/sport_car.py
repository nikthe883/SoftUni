from .car import Car

class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
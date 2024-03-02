from .motorcycle import Motorcycle

class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
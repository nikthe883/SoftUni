from .vehicle import Vehicle

class Motorcycle(Vehicle):
    
    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
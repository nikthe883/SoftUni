from abc import ABC, abstractmethod


class Vehicle(ABC):

    

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self,fuel_quantity,fuel_consumption):

        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        fuel = self.fuel_quantity
        self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

        if self.fuel_quantity < 0:
            self.fuel_quantity = fuel

    def refuel(self,liters):
        self.fuel_quantity += liters

class Truck(Vehicle):
    def __init__(self,fuel_quantity,fuel_consumption):

        self.fuel_quantity = fuel_quantity 
        self.fuel_consumption = fuel_consumption 
        

    def drive(self,distance):
        fuel = self.fuel_quantity
        self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

        if self.fuel_quantity < 0:
            self.fuel_quantity = fuel

    def refuel(self,liters):
        self.fuel_quantity += liters *0.95
        self.fuel_quantity 

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


class Customer:

    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    
    def get_customer(self):
        return self.name,self.age,self.id,self.rented_dvds 

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({' ,'.join([x.name for x in self.rented_dvds])})"
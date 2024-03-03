

class Zoo():

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:

       self.name = name
       self.__budget = budget
       self.__animal_capacity = animal_capacity
       self.__workers_capacity = workers_capacity 

       self.animals = []
       self.workers = []

    
    def add_animal(self,animal, price):
        if price <= self.__budget:
            if self.__animal_capacity > 0:
                self.animals.append(animal)
                self.__animal_capacity -= 1
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return f"Not enough space for animal"
        return f"Not enough budget"
    
    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"
    
    def fire_worker(self, worker):
        for i,w in enumerate(self.workers):
            if w.name == worker:
                del self.workers[i]
                return f"{worker} fired successfully"
        return f"There is no {worker} in the zoo"
    
    def pay_workers(self):
        salaries = sum([x.salary for x in self.workers])
        print(salaries)
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_price = sum([x.money_for_care for x in self.animals])
        if self.__budget >= tend_price:
            self.__budget -= tend_price
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."
    
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(x) for x in result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]

        return "\n".join(result)
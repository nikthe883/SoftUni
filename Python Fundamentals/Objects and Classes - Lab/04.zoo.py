class Zoo:
    __animals = 0

    def __init__(self, name):
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.name = name

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result +=  f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result +=  f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result +=  f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


zoo_name_input = input()
zoo = Zoo(zoo_name_input)
numbers = int(input())

for i in range(numbers):
    animal = input().split(" ")
    zoo.add_animal(animal[0], animal[1])

info = input()
print(zoo.get_info(info))

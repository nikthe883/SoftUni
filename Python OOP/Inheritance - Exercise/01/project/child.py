from .person import Person

class Child(Person):

    def __init__(self, name, age) -> None:
        super().__init__(name, age)


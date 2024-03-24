from .cat import Cat

class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, gender = 'Male')

    def __repr__(self):
        return super().__repr__()
    

    def make_sound(self):
        return "Hiss"
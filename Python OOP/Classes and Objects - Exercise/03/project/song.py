
class Song:

    def __init__(self, name, length, single) -> None:
        self.name = name
        self.length = length
        self.single = False

    def get_info(self):
        return f"{self.name} - {self.length}"
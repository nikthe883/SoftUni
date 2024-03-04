class Category:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def edit(self, new_name):
        self.name = new_name
    

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
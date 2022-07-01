class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):

        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [i for i in self.products if i.startswith(first_letter)]

    def __repr__(self):
        my_string  = f"Items in the {self.name} catalogue:\n"
        my_string += "\n".join(sorted(self.products))
        return my_string




catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

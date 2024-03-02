from project.product import Product


class ProductRepository:

    products= []

    def add(self, product: Product):
        self.products.append(product)

    
    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
            
    def remove(self, product_name): 
        for x, product in enumerate(self.products):
            if product.name == product_name:
               del self.products[x]

    def __repr__(self):
        show = ""
        for x in self.products:
            if x.name not in show:
                show += f"{x.name}: {x.quantity}\n"
        return show.rstrip()
    

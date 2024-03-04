class MovieWorld:

    DEFAULT_DVD_CAPACITY = 15
    DEFAULT_CUSTOMER_CAPACITY = 10

    def __init__(self,name) -> None:
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15
    
    @staticmethod
    def customer_capacity():
        return 10
    
    def add_customer(self, customer):
        if len(self.customers) < self.DEFAULT_CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self,dvd):
        if len(self.dvds) < self.DEFAULT_DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):

        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"

                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if customer.age <= dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        if dvd.is_rented:
                                return f"DVD is already rented"
                          
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f"{customer.name} has successfully rented {dvd.name}"
        
                        

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for i, dvd in enumerate(customer.rented_dvds):
                    
                    if dvd.id == dvd_id:
                        dvd_name = dvd.name
                        dvd.is_rented = False
                        del customer.rented_dvds[i]
                        return f"{customer.name} has successfully returned {dvd_name}"
                    
                
                return f"{customer.name} does not have that DVD"
                
    def __repr__(self) -> str:
        result = ''
        for c in self.customers:
            result += f"{repr(c)}\n"
        
        for d in self.dvds:
            result += f"{repr(d)}\n"
        
        return result


        

        
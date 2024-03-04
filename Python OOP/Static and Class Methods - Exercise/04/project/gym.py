class Gym:

    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self,customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    
    def add_equipment(self, v):
        if v not in self.equipment:
            self.equipment.append(v)
    
    def add_plan(self, v):
        if v not in self.plans:
            self.plans.append(v)
    
    def add_subscription(self,v):
        if v not in self.subscriptions:
            self.subscriptions.append(v)
    
    def subscription_info(self, subscription_id):
        result = ""
        id = subscription_id
        for s,c,t,e,p in zip(self.subscriptions,self.customers,self.trainers,self.equipment,self.plans):
            if s.id == id and c.id == id and t.id == id and e.id == id and p.id == id:
                result += f"{repr(s)}\n{repr(c)}\n{repr(t)}\n{repr(e)}\n{repr(p)}"

        return result
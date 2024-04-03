from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    OXIGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level = self.OXIGEN_LEVEL)

    def miss(self,time_to_catch):
        self.oxygen_level -= time_to_catch * 0.6
        round(self.oxygen_level)
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.OXIGEN_LEVEL




    
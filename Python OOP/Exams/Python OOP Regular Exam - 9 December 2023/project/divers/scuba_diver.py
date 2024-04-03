from project.divers.base_diver import BaseDiver

class ScubaDiver(BaseDiver):

    OXIGEN_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level = self.OXIGEN_LEVEL)

    def miss(self,time_to_catch):
        self.oxygen_level -= time_to_catch * 0.3
        round(self.oxygen_level)
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.OXIGEN_LEVEL

from .base_peak import BasePeak


class SummitPeak(BasePeak):
    difficulty_level = 2500
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > self.difficulty_level:
            return "Extreme"
        if 1500 <= self.elevation <= self.difficulty_level:
            return "Advanced"

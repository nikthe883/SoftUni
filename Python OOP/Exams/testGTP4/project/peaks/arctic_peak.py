from .base_peak import BasePeak


class ArcticPeak(BasePeak):
    difficulty_level = 3000
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > self.difficulty_level:
            return "Extreme"
        if 2000 <= self.elevation <= self.difficulty_level:
            return "Advanced"


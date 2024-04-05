from .base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    STRENGHT = 200
    def __init__(self, name: str):
        super().__init__(name, strength=self.STRENGHT)

    def can_climb(self):
        return  self.strength >= 100

    def climb(self, peak):
        if peak.calculate_difficulty_level() == "Extreme":
             self.strength -= 40  # 20 * 2
         
        else:
             self.strength -= 30  # 20 * 1.5
        self.conquered_peaks.append(peak.name)

from .base_climber import BaseClimber


class SummitClimber(BaseClimber):
    """Summit Climber"""
    STRENGHT = 150
    def __init__(self, name: str):
        super().__init__(name, strength=self.STRENGHT)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak):
        # Reduce strength based on the peak's difficulty level and record the peak as conquered
        if peak.calculate_difficulty_level() == "Advanced":
            self.strength -= (30 * 1.3)
        else:  # Assuming "Extreme" or any other difficulty level uses a 2.5 multiplier
            self.strength -= (30 * 2.5)
        self.conquered_peaks.append(peak.name)
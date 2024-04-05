from peaks.summit_peak import SummitPeak
from peaks.arctic_peak import ArcticPeak
from climbers.arctic_climber import ArcticClimber
from climbers.summit_climber import SummitClimber


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def _find_climber(self, name):
        return next((climber for climber in self.climbers if climber.name == name), None)

    def _find_peak(self, name):
        return next((peak for peak in self.peaks if peak.name == name), None)

    def register_climber(self, climber_type: str, climber_name: str):
        if self._find_climber(climber_name):
            return f"{climber_name} has been already registered."
        
        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        elif climber_type == "SummitClimber":
            climber = SummitClimber(climber_name)
        else:
            return f"{climber_type} doesn't exist in our register."

        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if self._find_peak(peak_name):
            return f"{peak_name} has already been added to the wish list."
        
        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
        elif peak_type == "SummitPeak":
            peak = SummitPeak(peak_name, peak_elevation)
        else:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = self._find_climber(climber_name)
        peak = self._find_peak(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        recommended_gear = set(peak.get_recommended_gear())
        climber_gear = set(gear)

        if climber_gear >= recommended_gear:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            missing_gear = recommended_gear - climber_gear
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._find_climber(climber_name)
        peak = self._find_peak(peak_name)

        # Climber Validation
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        # Peak Validation
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        # Check if the climber is prepared with the right gear
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        # Pre-climb strength check to ensure climber has enough strength
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        # Perform the climb, which assumes the reduction of strength
        climber.climb(peak)
        
        # After successful climb
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."



    def get_statistics(self):
        # Use a set to keep track of unique peak names conquered by all climbers
        unique_conquered_peaks = set(peak for climber in self.climbers for peak in climber.conquered_peaks)

        # Prepare the statistics string
        stats = f"Total climbed peaks: {len(unique_conquered_peaks)}\n**Climber's statistics:**\n"
        
        # Filter for climbers who have conquered at least one peak and sort them as specified
        climbers_who_climbed = filter(lambda c: c.conquered_peaks, self.climbers)
        sorted_climbers = sorted(climbers_who_climbed, key=lambda c: (-len(c.conquered_peaks), c.name))

        # Generating statistics for each climber
        for climber in sorted_climbers:
            # Sort the conquered peaks alphabetically for each climber
            sorted_peaks = sorted(climber.conquered_peaks)
            climber_info = f"{type(climber).__name__}: /// Climber name: {climber.name} * Left strength: {climber.strength:.1f} * Conquered peaks: {', '.join(sorted_peaks)} ///"
            stats += climber_info + "\n"

        return stats.strip()


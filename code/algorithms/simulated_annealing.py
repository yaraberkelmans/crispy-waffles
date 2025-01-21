import random
import math

from .malus import calculate_malus
from .hill_climber import HillClimber


class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class performs a random change to the timetable, just as in HillClimber.
    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.

    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """
    def __init__(self, timetable, temperature=1):

        # use the init of the Hillclimber class for the timetable
        super().__init__(timetable)

        # starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)

    def check_solution(self, new_timetable):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_value = new_timetable.calculate_malus()
        old_value = self.value

        # calculate the probability of accepting this new timetable
        delta = new_value - old_value
        probability = math.exp(-delta / self.T)

        # pull a random number between 0 and 1 and see if we accept the timetable!
        if random.random() < probability:
            self.timetable = new_timetable
            self.value = new_value

        # update the temperature
        self.update_temperature()
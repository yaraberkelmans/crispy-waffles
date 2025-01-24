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

        self.iterations = 0
        
    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        if self.iterations > 0:
            self.T = self.T - (self.T0 / self.iterations)

    def check_solution_1(self, new_timetable):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_value = calculate_malus(new_timetable)
        old_value = self.value

        # calculate the probability of accepting this new timetable
        delta = new_value - old_value

        # prevent crashing for huge improvements
        if delta < -1:
            delta = -1

        # with negative delta, so an improvement, prob is always more than 1, so always larger than random.random()
        probability = math.exp(-delta / self.T)

        # pull a random number between 0 and 1 and see if we accept the timetable!
        if random.random() < probability:
            self.timetable = new_timetable
            self.value = new_value

        # update the temperature
        self.update_temperature()

    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_value = self.best_neighbour_value
        old_value = self.value

        # calculate the probability of accepting this new timetable
        delta = new_value - old_value

        # prevent crashing for huge improvements, eg delta = -1000
        if delta < -1:
            delta = -1
            

        # with negative delta, so an improvement, prob is always more than 1, so always larger than random.random()
        probability = math.exp(-delta / self.T)

        # update the temperature
        self.update_temperature()

        # pull a random number between 0 and 1 and see if we accept the timetable!
        if random.random() < probability:
            self.timetable = self.best_neighbour
            self.value = new_value
            return True

        

        

        

        
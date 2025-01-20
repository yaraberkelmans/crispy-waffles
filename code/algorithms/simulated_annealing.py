import random
import math

from .malus import calculate_malus
from .hill_climber import HillClimber


class SimulatedAnnealing(HillClimber):
    """
    
    """
    def __init__(self, timetable, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(timetable)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_value = new_graph.calculate_malus()
        old_value = self.value

        # Calculate the probability of accepting this new graph
        delta = new_value - old_value
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.graph = new_graph
            self.value = new_value

        # Update the temperature
        self.update_temperature()
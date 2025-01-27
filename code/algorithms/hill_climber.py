import copy
import random
import math

from .randomize import apply_random_swap
from .malus import calculate_malus


class HillClimber():
    """
    This class creates instances of the Hill Climbing algorithm. The algorithm works by
    generating n amount of neighbours, which are deepcopy's of the current best timetable
    with x amount of random swaps applied to it. Then the best neighbour is chosen based on 
    the neighbour that has the least malus points. If the best neighbour has a malus score 
    lower then the current best timetable, this neighbour now becomes the new best timetable
    and the next iteration starts. If the best neighbour is not better then the current best 
    timetable, the timetable is not updated and the next iteration of the algorithm starts.
    """
    def __init__(self, timetable):
        self.timetable = timetable
        #self.neighbours = {}
        #self.best_neighbour = timetable
        #self.best_neighbour_malus_points = timetable.calculate_malus() 
        self.value = calculate_malus(timetable)
        self.iteration_values = {}
        self.best_iteration = 0
        self.iterations_ran = 0

    def mutate_timetable(self, new_timetable, number_of_swaps):
        """
        This method applies n amount of random swaps to the current best
        timetable.
        """
        for i in range(number_of_swaps):
            apply_random_swap(new_timetable)

    def generate_individual_neighbour(self, n_swaps):
        """
        This method generates a single neighbour by deepcopying the current 
        best timetable and then aplies n amount of swaps to this deepcopy.
        """
        timetable = copy.deepcopy(self.timetable)
        for i in range(n_swaps):
            apply_random_swap(timetable)
        return timetable
    

    def choose_best_neighbour(self, neighbours):
        """
        This method loops over all generated neighbours and calculates their
        malus scores. It then stores the neighbour with the best malus score
        in self.
        """
        self.best_neighbour_value = None
        self.best_neighbour = None

        for neighbour in neighbours:
            neighbour_malus = calculate_malus(neighbour)
            if self.best_neighbour_value == None:
                self.best_neighbour_value = neighbour_malus
                self.best_neighbour = neighbour
            
            if neighbour_malus < self.best_neighbour_value:
                self.best_neighbour_value = neighbour_malus
                self.best_neighbour = neighbour

    def check_solution(self):
        """
        This method checks if the malus score of the best neighbour is lower
        then the current best timetable and if so it assigns the best neighbour
        as the new current best timetable in self and also the associated malus
        score.
        """
        new_value = self.best_neighbour_value
        old_value = copy.deepcopy(self.value)

        if new_value < old_value:
            self.timetable = self.best_neighbour
            self.value = new_value
            return True

    # TODO ADD DOCSTRINGS!!!
    def run(self,  neighbours_, swaps_per_neighbour, iterations, verbose_alg = False):
        self.iterations = iterations
        
        for iteration in range(iterations):
            neighbours = []
            
            if verbose_alg:
                print(f'Iteration {iteration}/{iterations} now running, value of timetable malus points is now {self.value}')
            
            for i in range(neighbours_):
                neighbours.append(self.generate_individual_neighbour(swaps_per_neighbour))
            
            self.choose_best_neighbour(neighbours)
            improved = self.check_solution()

            self.iteration_values[iteration] = self.value

            if improved:
                self.best_iteration = iteration

            i_since_last_best = iteration - self.best_iteration
            
            if iteration == 10000 and self.value > 50:
                return self.value

            if i_since_last_best == 1000:
                print(f'{iteration} iterations')
                self.iterations_ran = iteration
                return self.value
            
            # elif i_since_last_best > 250 and self.value > 130:
            #     print(f'{iteration} iterations')
            #     self.iterations_ran = iteration
            #     return self.value 
        
        self.iterations_ran = iteration
        return self.value




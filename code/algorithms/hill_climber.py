import copy
import random
import math

from .randomize import apply_random_swap
from .malus import calculate_malus


class HillClimber():
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
        for i in range(number_of_swaps):
            apply_random_swap(new_timetable)

    def generate_individual_neighbour(self, n_swaps):
        timetable = copy.deepcopy(self.timetable)
        for i in range(n_swaps):
            apply_random_swap(timetable)
        return timetable
    

    def choose_best_neighbour(self, neighbours):
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
        new_value = self.best_neighbour_value
        old_value = copy.deepcopy(self.value)

        if new_value < old_value:
            self.timetable = self.best_neighbour
            self.value = new_value
            return True


    def run(self,  n_neighbours, n_swaps_per_neighbour, iterations, verbose_alg = False):
        self.iterations = iterations
        for iteration in range(iterations):
            neighbours = []
            if verbose_alg:
                print(f'Iteration {iteration}/{iterations} now running, value of timetable malus points is now {self.value}')
            for i in range(n_neighbours):
                neighbours.append(self.generate_individual_neighbour(n_swaps_per_neighbour))
            
            self.choose_best_neighbour(neighbours)
            improved = self.check_solution()

            # if iteration // 10 == 0 and n_swaps_per_neighbour > 1:
            #     n_swaps_per_neighbour -= 4

            # store current malus points 
            self.iteration_values[iteration] = self.value

            if improved:
                self.best_iteration = iteration

            i_since_last_best = iteration - self.best_iteration
            
            if iteration > 1000 and self.value > 1000:
                return self.value

            if i_since_last_best == 1000:
                print(f'{iteration} iterations')
                self.iterations_ran = iteration
                return self.value
            elif i_since_last_best > 250 and self.value > 130:
                print(f'{iteration} iterations')
                self.iterations_ran = iteration
                return self.value 
        
        self.iterations_ran = iteration
        return self.value




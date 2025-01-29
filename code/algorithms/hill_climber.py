from .malus import calculate_malus
from .algorithm_mutations import Algorithm
import copy

class HillClimber(Algorithm):
    def __init__(self, timetable):
        super().__init__(timetable)
        self.value = calculate_malus(timetable)
        self.iteration_values = {}
        self.best_iteration = 0
        self.iterations_ran = 0

    def mutate_timetable(self, new_timetable, number_of_swaps):
        for i in range(number_of_swaps):
            self.apply_random_swap(new_timetable)

    def check_solution(self, new_timetable):
        new_value = calculate_malus(new_timetable)
        old_value = copy.deepcopy(self.value)

        if new_value < old_value:
            self.timetable = new_timetable
            self.value = new_value
            return True


    def run(self, iterations, number_of_swaps, verbose_alg=False):
        
        for iteration in range(iterations):
            if verbose_alg:
                print(f'Iteration {iteration}/{iterations} now running, value of timetable malus points is now {self.value}')
            
            new_timetable = copy.deepcopy(self.timetable)
            
            self.mutate_timetable(new_timetable, number_of_swaps)

            if self.check_reset_conditions(iteration):
                return self.value
            
        return self.value
    

    def check_reset_conditions(self, iteration):
        improved = self.check_solution
        
        if improved:
                self.best_iteration = iteration

        i_since_last_best = iteration - self.best_iteration
        if i_since_last_best == 500:
            print(f'{iteration} iterations')
            self.iterations = iteration

            return True
from .malus import calculate_malus
from .algorithm_mutations import Algorithm
import copy

class HillClimber(Algorithm):
    def __init__(self, timetable):
        super().__init__(timetable)
        self.iteration_values = {}
        self.best_iteration = 0

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


    def run(self, number_of_swaps, iterations, verbose_alg=False, heuristic=False):
        self.swaps = number_of_swaps
        self.iterations = iterations

        for iteration in range(iterations):
            if verbose_alg:
                print(f'Iteration {iteration}/{iterations} now running, value of timetable malus points is now {self.value}')
            
            new_timetable = copy.deepcopy(self.timetable)
           
            self.mutate_timetable(new_timetable, number_of_swaps)
            
            if heuristic:
                self.decrease_swaps(iteration)

            if self.check_reset_conditions(iteration, new_timetable):
                return self.value
            
        return self.value
    

    def check_reset_conditions(self, iteration, new_timetable):
        improved = self.check_solution(new_timetable)
        
        if improved:
                self.best_iteration = iteration

        i_since_last_best = iteration - self.best_iteration
        if i_since_last_best == 500:
            print(f'{iteration} iterations')
            self.iterations = iteration

            return True
        
    def decrease_swaps(self, iteration):
        if iteration % 250 == 0 and iteration > 1:
            if self.swaps > 2:
                self.swaps = self.swaps - 1
        
    # def adjust_swaps(self, iteration):
    #      if
    #      if iteration % 1000 == 0 and iteration > 1:
    #             self.swaps = self.swaps // 2
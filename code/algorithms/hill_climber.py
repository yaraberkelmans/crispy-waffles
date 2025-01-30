from .malus import calculate_malus
from .algorithm_mutations import Algorithm
import copy

class HillClimber(Algorithm):
    """
    The Hill Climber class works by generating a new timetable
    with a certain number of swaps, and only accepts this new
    timetable if the new score is lower than the previous one.
    """
    def __init__(self, timetable):
        super().__init__(timetable)
        self.iteration_values = {}
        self.best_iteration = 0

    def mutate_timetable(self, new_timetable, number_of_swaps):
        """
        This method applies n amount of random swaps to the current best
        timetable.
        """
        for i in range(number_of_swaps):
            self.apply_random_swap(new_timetable)

    def check_solution(self, new_timetable):
        """
        This method checks if the malus score of the new_timetable is lower
        then the current best timetable and if so it assigns the new_timetable
        as the new current best timetable in self and also the associated malus
        score.
        """
        new_value = calculate_malus(new_timetable)
        old_value = copy.deepcopy(self.value)

        if new_value < old_value:
            self.timetable = new_timetable
            self.value = new_value
            return True


    def run(self, number_of_swaps, iterations, verbose_alg=False, heuristic=False):
        """
        This method runs the Genetic Hill climber algorithm. It takes in the parameters: 
        - number_of_swaps: the amount of swaps applied to the timetable
        - iterations: the amount of iterations the algorithm runs
        - verbose_alg: if True, prints updates at every iteration.
        - heuristic: if True, lowers the number_of_swaps at every 250 iterations to become more specific.
        """
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
        """
        This method checks if the stop conditions for restarting an algorithm have
        been met. If so the method returns True and the hill climber loop stops.
        If not the method returns false and the algorithm will keep running.
        """
        improved = self.check_solution(new_timetable)
        
        if improved:
                self.best_iteration = iteration

        i_since_last_best = iteration - self.best_iteration
        if i_since_last_best == 500:
            print(f'{iteration} iterations')
            self.iterations = iteration

            return True
        
    def decrease_swaps(self, iteration):
        """
        This method decreases the number of swaps with 1 every 250 iterations.
        However, the swaps minimum number is 2.
        """
        if iteration % 250 == 0 and iteration > 1:
            if self.swaps > 2:
                self.swaps = self.swaps - 1
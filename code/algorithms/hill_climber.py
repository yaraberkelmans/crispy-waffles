import copy
from .randomize import apply_random_swap
from .malus import calculate_malus
class HillClimber():
    def __init__(self, timetable):
        self.timetable = timetable
        #self.neighbours = {}
        #self.best_neighbour = timetable
        #self.best_neighbour_malus_points = timetable.calculate_malus() 
        self.value = calculate_malus(timetable)
        self.best_iteration = 0


    def mutate_timetable(self, new_timetable, number_of_swaps):
        for i in range(number_of_swaps):
            apply_random_swap(new_timetable)

    def check_solution(self, new_timetable):
        new_value = calculate_malus(new_timetable)
        old_value = copy.deepcopy(self.value)

        if new_value < old_value:
            self.timetable = new_timetable
            self.value = new_value
            return True
        # else:
        #     print(f'Not better')

    def run_1(self, iterations, number_of_swaps):
        for iteration in range(iterations):
            #print(f'Iteration {iteration}/{iterations} now running, value of timetable malus points is now {self.value}')
            
            new_timetable = copy.deepcopy(self.timetable)
            
            self.mutate_timetable(new_timetable, number_of_swaps)
            improved = self.check_solution(new_timetable)
            
            if improved:
                self.best_iteration = iteration

            i_since_last_best = iteration - self.best_iteration
            if i_since_last_best == 500:
                print(f'{iteration} iterations')
                return self.value
        return self.value

    # def generate_individual_neighbour(self):
    #     timetable = copy.deepcopy(self.timetable)
    #     for i in range(self.n_swaps):
    #         timetable.apply_random_swap()
    #     self.neighbours[timetable] = None
    
    # def calculate_malus(self):
    #     for neighbour in self.neighbours.keys():
    #         malus_points = neighbour.calulate_malus()
    #         self.neighbours[neighbour] = malus_points

    # def choose_best_neighbour(self):
    #     for neighbour, malus_points in self.neighbours.items():
    #         if malus_points < self.best_neighbour_malus_points:
    #             self.best_neighbour = neighbour
    #             self.best_neighbour_malus_points = malus_points

    # def run(self,  n_neighbours, n_swaps_per_neighbour):
    #     for i in range(n_neighbours):
    #         self.generate_individual_neighbour()
        
    #     self.calculate_malus()
    #     self.choose_best_neighbour()



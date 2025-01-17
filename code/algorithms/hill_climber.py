import copy
from .randomize import apply_random_swap
from .malus import calculate_malus
class HillClimber():
    def __init__(self, timetable):
        self.timetable = copy.deepcopy(timetable)

    def generate_neighbours(self, iterations=10, random_swaps_per_neighbour=10):
        best_timetable = None
        last_timetable = self.timetable
        for i in range(iterations):
            for j in range(random_swaps_per_neighbour):
                random_swapped_timetable = apply_random_swap(last_timetable)
                pass

    def perform_random_swap(self):
        pass
            
        

    def choose_random_swap(self):
        pass
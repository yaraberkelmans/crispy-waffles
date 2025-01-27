from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment
from code.algorithms.randomize import random_student_course_assignment
from code.algorithms.randomize import random_student_activity_assignment
from code.algorithms.randomize import randomize
from code.algorithms.randomize import *
from code.algorithms.malus import calculate_malus
from code.algorithms.hill_climber import HillClimber
from code.algorithms.visualize import *
from code.classes.experiment import Experiment
from code.algorithms.simulated_annealing import SimulatedAnnealing

import csv
import sys
import copy
import pickle

#
import cProfile
import pstats
#

if __name__ == "__main__":
    
    # initialize timetable
    timetable = Timetable()
    timetable.generate_initial_timetable()
    sys.setrecursionlimit(10**6)

    # # -------------------------------------------------------- Hill Climber -----------------------------------------------------
    # experiment = Experiment(timetable, iterations=10)

    # # run Hill Climber
    # hill_climber_summary = experiment.run_algorithm("data/best_timetable_exptest_12_neighbours.pkl", HillClimber, verbose=True, verbose_alg=True,
    #                                                   neighbours=12, swaps_per_neighbour=3, iterations=15000)
    # print("Hill Climber Summary:", hill_climber_summary)
    # print('Malus per cat', experiment.malus_per_cat)


    # # -------------------------------------------------------Simulated Annealing -----------------------------------------------
    # experiment = Experiment(timetable, iterations=3)

    # # run SimAnn
    # sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, 'data/experiment_pickle_test/', verbose=True, verbose_alg=True, 
    #                                              neighbours=2, swaps_per_neighbour=2, iterations=10)
    # print("Simulated Annealing Summary:", sim_ann_summary)
    # print('Malus per cat', experiment.malus_per_cat)


    ## ---------------------------------- Format for loading in timetable and exporting to csv --------------------------------
    input_file_path = None
    stored_timetable = load_pickle_file(input_file_path)

    output_file_path = None
    timetable_to_csv(stored_timetable, output_file_path)



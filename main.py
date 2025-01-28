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


    # ------------------------------------------------------ Simulated Annealing -----------------------------------------------
    experiment = Experiment(timetable, iterations=10)

    # run SimAnn
    sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, 'data/final_runs_3/', verbose=True, verbose_alg=False, 
                                                 neighbours=9, swaps_per_neighbour=2, iterations=20000, temperature=2.5)
    print("Simulated Annealing Summary:", sim_ann_summary)
    print('Malus per cat', experiment.malus_per_cat)


    ## ---------------------------------- Format for loading in timetable and exporting to csv --------------------------------
    # input_file_path = None
    # stored_timetable = load_pickle_file(input_file_path)

    # output_file_path = None
    # timetable_to_csv(stored_timetable, output_file_path)

    # testing the experiment plot function 

    # swaps_per_neighbour_values = [1, 2, 3]
    # neighbours_values = [7, 8, 9]


    # import os
    # os.makedirs("test_data", exist_ok=True)

    # for swaps in swaps_per_neighbour_values:
    #     for neighbours in neighbours_values:
         
    #         experiment = Experiment(timetable, iterations=5) 
            
    
    #         experiment.run_algorithm(
    #             SimulatedAnnealing,
    #             folder_path="test_data/",
    #             file_name_addition=f"sim_ann_{swaps}_{neighbours}",
    #             verbose=False,
    #             neighbours_=neighbours,
    #             swaps_per_neighbour=swaps,
    #             iterations=10,
    #             temperature=1  
    #         )
            
    #         file_name = f"test_data/experiment_sim_ann_{swaps}_{neighbours}.pkl"
    #         with open(file_name, "wb") as f:
    #             pickle.dump(experiment, f)

    # file_paths = [
    #     "test_data/experiment_sim_ann_1_7.pkl",
    #     "test_data/experiment_sim_ann_1_8.pkl",
    #     "test_data/experiment_sim_ann_1_9.pkl",
    #     "test_data/experiment_sim_ann_2_7.pkl",
    #     "test_data/experiment_sim_ann_2_8.pkl",
    #     "test_data/experiment_sim_ann_2_9.pkl",
    #     "test_data/experiment_sim_ann_3_7.pkl",
    #     "test_data/experiment_sim_ann_3_8.pkl",
    #     "test_data/experiment_sim_ann_3_9.pkl",
    # ]

    # malus_df = load_experiment_data(file_paths)
        
    # print(malus_df.head(10))
        
    # plot_experiment_results(malus_df)

# ----------------------- Experiment loader --------------------------
exp = load_pickle_data('data/final_runs/SimulatedAnnealing_9_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl')
print(exp.results)


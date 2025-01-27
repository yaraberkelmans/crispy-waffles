from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment
from code.algorithms.randomize import random_student_course_assignment
from code.algorithms.randomize import random_student_activity_assignment
from code.algorithms.randomize import randomize
from code.algorithms.randomize import *
from code.algorithms.malus import calculate_malus
from code.algorithms.hill_climber import HillClimber
from code.algorithms.visuealize_timetable import *
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
    # def main():
    # initialize timetable
    timetable = Timetable()
    timetable.generate_initial_timetable()

    # N=10000
    # malus_points_list = []
    # iter_list= list(range(1, N + 1))
    # for exp in range(N):
    #     full_randomized_timetable = randomize(timetable)
    #     malus_points = calculate_malus(full_randomized_timetable)
    #     malus_points_list.append(malus_points)
    
    # plot_malus_histogram(malus_points_list)
                
    # test new apply_random_swap
    # full_randomized_timetable = randomize(timetable)
    
    # random_swapped_timetable = apply_random_swap(full_randomized_timetable)

    # malus_points = calculate_malus(full_randomized_timetable)
    # print(f'malus points is {malus_points}')

    sys.setrecursionlimit(10**6)
    #####
    # hill_climber_hi_scores = []
    # hill_climber_scores_iterations = []

    # hillclimber_range = 100
    # for i in range(1):
    #     hill_climber_individual_score_iterations = []
    # full_randomized_timetable = randomize(timetable)
    # hill_climber = HillClimber(full_randomized_timetable)
    #     hill_climber_score = hill_climber.run(10, 3, hillclimber_range)
    
        
    #     # append to list to make list in list for results and iterations exports
    #     hill_climber_individual_score_iterations.append(hill_climber_score)
    #     hill_climber_individual_score_iterations.append(hill_climber.iterations)

    #     hill_climber_hi_scores.append(hill_climber_score)
    #     hill_climber_scores_iterations.append(hill_climber_individual_score_iterations)
        
    #     print(f'The score for iteration {i} is {hill_climber_score}')
    #     if hill_climber_score <= min(hill_climber_hi_scores):
    #         best_timetable = copy.deepcopy(hill_climber.timetable)
    #         # barplot_malus(best_timetable)
    #         # print('malus plotted')
    #         with open("data/best_timetable_test.pkl", "wb") as f:
    #             pickle.dump(best_timetable, f)
    #             print(f"New best Timetable saved. at score {hill_climber_score}")
    #####
            
    #     plot_malus_iter(list(range(1, hillclimber_range + 1)), hill_climber.iteration_values)

        
    # print(min(hill_climber_hi_scores))
    
    # header = ['results', 'iterations']
    # with open ('Results_and_iterations.csv', "w", newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(header)
    #         writer.writerow(hill_climber_scores_iterations)

    # with open ('Results.csv', "w", newline='') as f:
    #         writer = csv.writer(f)
    #         for result in hill_climber_hi_scores:
    #             writer.writerow([result])
    # with open("data/best_timetable_exptest3.pkl", "rb") as f:
    #     stored_timetable = pickle.load(f)

    
    # print(calculate_malus(stored_timetable))
    # for course in stored_timetable.courses:
    #     print(f'---------------------Check for course {course}----------------------')
    #     print(len(course.student_list))
    #     for activity_type in course.activities.keys():
    #         for activity in course.activities[activity_type]:
    #             print(f'----Capactity check for {activity}----')
    #             print(activity.location)
    #             print(activity.timeslot)
    #             print(len(activity.student_list))
    #             print(f'----Student list of {activity}----')
    #             for student in activity.student_list:
    #                 print(student)
        

    # dit uitcommenten na het aanmaken van csv, dan handmatig de C kringeltjes aanpassen en dan (naar ###)
    # data = []
    # for timeslot in stored_timetable.timetable.keys():
    #         for location, activity in stored_timetable.timetable[timeslot].items():
    #             if activity:
    #                 for student in activity.student_list:
    #                     data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name, 'Student': student.name}) 
    #             else:
    #                 data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id,'Vak': 'Empty'})

    # column_names = ['Tijdslot', 'Zaal', 'Vak', 'Activiteit', 'Student']
    # with open('Timetable_pres_3.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=column_names)
    #     writer.writeheader()
    #     writer.writerows(data) 

    # ### vanaf hier nog een keer runnen
    # timetable_file = 'Timetable_pres_3.csv'
    # pivot_table = visualize_timetable(timetable_file)

    # # save the timetable to an HTML file
    # output_html_path = 'Timetable_pres_3.html'
    # save_timetable_to_html(pivot_table, output_html_path)

    # print(f"Timetable saved as HTML: {output_html_path}")
    
    # greedy = Greedy(full_randomized_timetable)
    # greedy.sort_activities_by_capacity()
    # for activity in full_randomized_timetable.activity_list:
    #     print(activity, activity.capacity)


    # barplot_malus(best_timetable)



    # experiment = Experiment(timetable, iterations=100)

    # # run Hill Climber
    # hill_climber_summary = experiment.run_algorithm("data/best_timetable_exptest_12_neighbours.pkl", HillClimber, verbose=True, verbose_alg=True,
    #                                                   neighbours_=12, swaps_per_neighbour=3, iterations=15000)
    # print("Hill Climber Summary:", hill_climber_summary)
    # print('Malus per cat', experiment.malus_per_cat)

    # experiment = Experiment(timetable, iterations=3)

    # # # # run SimAnn
    # sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, 'data/experiment_pickle_test/', verbose=True, verbose_alg=True, 
    #                                              neighbours_=2, swaps_per_neighbour=2, iterations=10)
    # print("Simulated Annealing Summary:", sim_ann_summary)
    # print('Malus per cat', experiment.malus_per_cat)

    # stored_timetables = []
    # with open("data/neighbour_n_exp_3_swaps/HillClimber_n_neighbours_8_n_swaps_per_neighbour_3_iterations_20000__all_timetables.pkl", "rb") as f:
    #     while True:
    #         try:
    #             timetable_obj = pickle.load(f)
    #             stored_timetables.append(timetable_obj)
    #         except EOFError:
    #             break

    # calculate_malus(stored_timetables[1], verbose=True)

    with open('data/conflict_test/SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__experiment_info.pkl', 'rb') as f:
        stored_experiment = pickle.load(f)
    #calculate_malus(stored_timetable, verbose=True)
    #print(stored_experiment.alg_params)

    plot_malus_iter_test(stored_experiment)

    # # plot the malus points per iteration for each experiment iteration
    # with open('data/swap_per_neighbour_experiments/SimulatedAnnealing_n_neighbours_10_n_swaps_per_neighbour_2_iterations_20000__experiment_info.pkl', 'rb') as f:
    #     stored_experiment_scores = pickle.load(f)
    
    # for alg in stored_experiment_scores:
    #     plot_malus_iter(list(alg.keys()), list(alg.values()))

    # # plot the end maluspoints for each iteration to get a distribution (all_timetables is not working yet)
    # with open('data/swap_per_neighbour_experiments/SimulatedAnnealing_n_neighbours_10_n_swaps_per_neighbour_2_iterations_20000__all_timetables.pkl', 'rb') as f:
    #     all_stored_timetables = pickle.load(f)
    
    
    
    # malus_per_timetable = []
    # for alg in stored_experiment_scores:
    #     min_malus_points = min(list(alg.values()))
    #     malus_per_timetable.append(min_malus_points)
    
    # malus_per_experiment_step(malus_per_timetable)
    # print(stored_timetable.conflict_students)
    # for student in stored_timetable.conflict_students:
    #     print(f'\nStudent: {student} has the following conflicts: \n')
    #     for timeslot in student.conflict_activities.keys():
    #         print(f'Timeslot {timeslot} has the following conflicting acitvities:')
    #         for activity in student.conflict_activities[timeslot]:
    #             print(activity, activity.timeslot)
    # for i in range(16):
    #     switch_conflict_student(stored_timetable)
    #     calculate_malus(stored_timetable, verbose=True)
    # print(stored_timetable.conflict_students)
    # for student in stored_timetable.conflict_students:
    #     print(f'\nStudent: {student} has the following conflicts: \n')
    #     for timeslot in student.conflict_activities.keys():
    #         print(f'Timeslot {timeslot} has the following conflicting acitvities:')
    #         for activity in student.conflict_activities[timeslot]:
    #             print(activity, activity.timeslot)
    
    # for timeslot in stored_timetable.timetable.keys():
    #     print(timeslot, stored_timetable.timetable[timeslot])


    # extract malus points and iterations using a loop
    # algorithm_malus_points = []
    # iterations = []

    # kijken hoe goed te accessen 
    # experiment.indiv_scores is een lijst met dictionaries voor elke hill climber run
    # for iteration, malus in experiment.indiv_scores.items():
    #     iterations.append([])
    #     algorithm_malus_points.append(result)

    # print(experiment.indiv_scores)
    


    # test the barplot_hillclimber_performance function
    # barplot_hillclimber_performance(
    #     hillclimber=hill_climber,
    #     iterations=50,
    #     parameter_values=[6, 7, 10],  
    #     parameter_name="swaps",
    #     fixed_neighbours=10
    # )

    # barplot_hillclimber_performance(
    #     hillclimber=hill_climber,
    #     iterations=50,
    #     parameter_values=[8, 10, 12],  
    #     parameter_name="neighbours",
    #     fixed_swaps=4
    # )

    results_iter_malus_per_alg_temp100 = load_pickle_file("data/SIM_ANN_temperature_tests/SimulatedAnnealing_8_neighbours__2_swaps_per_neighbour_2500_iterations__Temp=100_experiment_info.pkl")
    print(results_iter_malus_per_alg_temp100)
    # for alg in results_iter_malus_per_alg_temp100:
    plot_malus_iter(results_iter_malus_per_alg_temp100, title='Malus drop for Temp = 100')

    # results_iter_malus_per_alg_temp50 = load_pickle_file("data/SIM_ANN_temperature_tests/SimulatedAnnealing_8_neighbours__2_swaps_per_neighbour_2500_iterations__Temp=50_experiment_info.pkl")
    # for alg in results_iter_malus_per_alg_temp50:
    #     plot_malus_iter(list(alg.keys()), list(alg.values()), title='Malus drop for Temp = 50')
    
    # results_iter_malus_per_alg_temp1 = load_pickle_file("data/SIM_ANN_temperature_tests/SimulatedAnnealing_8_neighbours__2_swaps_per_neighbour_2500_iterations__Temp=1_experiment_info.pkl")
    # for alg in results_iter_malus_per_alg_temp1:
    #     plot_malus_iter(list(alg.keys()), list(alg.values()), title='Malus drop for Temp = 1')
    
   
    ## profile the main function
    ## create a profiler and save the results in a file
    # profiler = cProfile.Profile()
    # profiler.enable()
    # main()
    # profiler.disable()
    # profiler.dump_stats("data/profile_test/profile_results.prof")  # Save binary profile data



import sys

from code.classes.timetable import Timetable
from code.algorithms.malus import calculate_malus
from code.algorithms.hill_climber import HillClimber
from code.visualize.visualize import *
from code.classes.experiment import Experiment
from code.algorithms.simulated_annealing import SimulatedAnnealing


if __name__ == "__main__":
    
    # initialize timetable
    timetable = Timetable()
    timetable.generate_initial_timetable()
    sys.setrecursionlimit(10**6)

    # # # -------------------------------------------------------- Hill Climber -----------------------------------------------------
    # experiment = Experiment(timetable, iterations=30)

    # # run Hill Climber
    # hill_climber_summary = experiment.run_algorithm( HillClimber, "results/pickle_files/final_runs/", verbose=True, verbose_alg=True,
    #                                                   neighbours=1, swaps_per_neighbour=3, iterations=20000)
    # print("Hill Climber Summary:", hill_climber_summary)
    # print('Malus per cat', experiment.malus_per_cat)


    """
    ------------------------------------------------------- Simulated Annealing -------------------------------------------------

    Voor het uitvoeren van een experiment in Simulated Annealing hebben we een experiment class die wordt aangeroepen met 
    bepaalde waardes. Hiervoor hebben we gebruik gemaakt van parallel running, en iedere keer de waardes aangepast om die versie
    vervolgens in een nieuwe terminal te laten runnen. Als we dit achter elkaar hadden gedaan was het een hele lange run geworden, 
    en dit af ons de modelijkheid om binnen een redelijke tijd met meerdere waardes te kunnen experimenteren. 
    
    Voor het eerste experiment hebben we het aantal neighbours en swaps gevarieerd. Met waardes van:

    - 7 neighbours en 1 swaps per neighbour
    - 7 neighbours en 2 swaps per neighbour
    - 7 neighbours en 3 swaps per neighbour
    - 8 neighbours en 1 swaps per neighbour
    - 8 neighbours en 2 swaps per neighbour
    - 8 neighbours en 3 swaps per neighbour
    - 9 neighbours en 1 swaps per neighbour
    - 9 neighbours en 2 swaps per neighbour
    - 9 neighbours en 3 swaps per neighbour

    Het algoritme slaat deze experimenten automatisch op als aparte en verschillende pickle files, het geeft namelijk een naam op 
    basis van de parameters, welke bij elk experiment verschillend zijn. Ook maakt de experiment automatisch een folder aan die je 
    mee kan geven.
    We hebben elk experiment 30 keer gerund met 20.000 iteraties per algoritme.

    Voor het tweede experiment hebben we gekeken naar een goede Temperatuur voor Simulated Annealling. De manier van experimenteren
    blijft hetzelfde, maar hierbij varieren we alleen de temperatuur. Hierin hebben we neighbours op 8 gehouden en swaps op 3.
    De temperaturen die zijn getest:

    - 1
    - 2.5
    - 5
    - 10
    - 20
    - 50

    In verband met beperkt resterende tijd, hebben we er voor gekozen om elke Temperatuur 10 keer te runnen, elk met 5000 iteraties.
    """
    # # -------------------------------------------------------Simulated Annealing -----------------------------------------------

    experiment = Experiment(timetable, iterations=10)

    # run SimAnn
    sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, 'results/pickle_files/new_runs/', verbose=True, verbose_alg=False, 
                                                 neighbours=6, swaps_per_neighbour=1, iterations=20000, temperature=1)
    print("Simulated Annealing Summary:", sim_ann_summary)
    print('Malus per cat', experiment.malus_per_cat)


    # # ---------------------------------- Format for loading in timetable and exporting to csv -----------------------------------
    # input_file_path = None
    # stored_timetable = load_pickle_file(input_file_path)

    # output_file_path = None
    # timetable_to_csv(stored_timetable, output_file_path)

    # file_paths = [
    #     "results/pickle_files/final_runs/SimulatedAnnealing_7_neighbours_1_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_7_neighbours_2_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_7_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_8_neighbours_1_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_8_neighbours_2_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_9_neighbours_1_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_9_neighbours_2_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    #     "results/pickle_files/final_runs/SimulatedAnnealing_9_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl",
    # ]


    # malus_df = load_experiment_data(file_paths)
        
# #     # print(malus_df)
        
    # plot_experiment_results(malus_df, 'neighbours_and_swaps')

# # # ---------------------------------------------------------- Experiment loader -----------------------------------------------------------------
# # # exp = load_pickle_data('results/pickle_files/neighbour_n_exp_3_swaps/HillClimber_n_neighbours_8_n_swaps_per_neighbour_3_iterations_20000__experiment_info.pkl')
# # # print(exp)

# # exp2 = load_pickle_data('results/pickle_files/neighbour_n_exp_3_swaps/SimulatedAnnealing_n_neighbours_8_n_swaps_per_neighbour_3_iterations_20000__experiment_info.pkl')

# # results = []


# exp_3 = load_pickle_data('results/pickle_files/final_runs/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl')

# exp_4 = load_pickle_data('results/pickle_files/final_runs_2/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl')

# exp_5 = load_pickle_data('results/pickle_files/final_runs_3/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_20000_iterations__Temp=1_experiment_instance.pkl')

# print(len(exp_5.results))
# print(len(exp_4.results))
# print(len(exp_3.results))


# # print(len(results))

# # # file_paths_best_timetable_only = [
# # #     ''
# # # ]
# # # best_timetables = collect_best_timetables(root_dir="data")
# # # for timetable in best_timetables:
# # #     malus_points = calculate_malus(timetable))


# def get_result_from_idiv_values(exp):
#     malus_list = []
#     count = 0
#     for alg_run in exp:
#         last_value = alg_run[max(alg_run.keys())]
#         if last_value < 1000:
#             malus_list.append(last_value)
#             count += 1
#     return malus_list


# # malus_list_1 = get_result_from_idiv_values(exp2)
# # print(len(malus_list_1))

   

# info = load_pickle_data('results/pickle_files/conflict_test/SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__experiment_info.pkl')


# file_paths_2 = [
#     'results/pickle_files/conflict_test/SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__experiment_info.pkl',
#     'results/pickle_files/neighbour_n_exp_3_swaps/SimulatedAnnealing_n_neighbours_8_n_swaps_per_neighbour_3_iterations_20000__experiment_info.pkl'
# ]

# total_malus = []
# for i, filepath in enumerate(file_paths_2):
#     loaded_data = load_pickle_data(filepath)
#     malus_per_file = get_result_from_idiv_values(loaded_data)
#     total_malus.extend(malus_per_file)

# print(total_malus)
# print(len(total_malus))
# exp_list = [exp_3, exp_4, exp_5]
# for exp in exp_list:
#     for result_dict in exp.results:
#         result = result_dict.get('score')
#         if result < 1000:
#             total_malus.append(result)

# print(total_malus)
# print(len(total_malus))

# plot_malus_histogram(total_malus, info='neighbours: 8, swaps: 3, iterations: 20000, temp: 1', suptitle='Simulated Annealing Malus Point Distribution', export=True, output_file_name='results/pickle_files/Sim_ann_8n_3s')




# low_malus_timetable = load_pickle_data('results/pickle_files/conflict_test/29_malus_SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__best_timetable.pkl')
# timetable_to_csv(low_malus_timetable, 'best_timetable_29_malus')
# pivot = visualize_timetable('best_timetable_29_malus.csv')
# save_timetable_to_html(pivot, 'best_timetable_ever_made_in_the_history_of_lectures_en_lesroosters_better_than_verenigde_bond_dieren_ofzo_made_by_the_crispy_waffles.html')


# # plot for temps
# file_paths_temps = ["results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=1_experiment_instance.pkl",
#                     "results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=2.5_experiment_instance.pkl",
#                      "results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=5_experiment_instance.pkl",
#                       "results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=10_experiment_instance.pkl",
#                        "results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=20_experiment_instance.pkl",
#                         "results/pickle_files/temperature_experiments/SimulatedAnnealing_8_neighbours_3_swaps_per_neighbour_5000_iterations__Temp=50_experiment_instance.pkl"]

# plot_temperature(file_paths_temps, output_file_name= None, export=False)

    
    timetable_29 = load_pickle_data('results/pickle_files/conflict_test/29_malus_SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__best_timetable.pkl')
    print(timetable_29.full_student_list[5].pers_timetable)
    # [0]


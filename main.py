import sys
import argparse

from code.classes.timetable import Timetable
from code.algorithms.malus import calculate_malus
from code.algorithms.genetic_hill_climber import GeneticHillClimber
from code.visualize.visualize import *
from code.classes.experiment import Experiment
from code.algorithms.simulated_annealing import SimulatedAnnealing
from code.algorithms.genetic_simulated_annealing import GeneticSimulatedAnnealing
from code.algorithms.hill_climber import HillClimber
from code.algorithms.randomize import Randomize
from code.algorithms.randomize import Randomize


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    parser= argparse.ArgumentParser(description="Run algorithm with custom parameters.")

    # type of algorithm and output_file_path
    parser.add_argument("algorithm", type=str, 
                        choices=["HillClimber","GeneticHillClimber","SimulatedAnnealing","GeneticSimulatedAnnealing"], 
                        help="Algorithm to run ((Genetic)HillClimber or (Genetic) SimulatedAnnealing)")
    parser.add_argument("output_file_path", type=str, help="Creates a new output_file_path")

    # experiment parameters
    parser.add_argument("--experiment_iters", type=int, default=20, help="Number of iters the experiment should run")
    parser.add_argument("--neighbours", type=int, default=8, help="Number of neighbours")
    parser.add_argument("--swaps", type=int, default=1, help="Number of swaps per neighbour")
    parser.add_argument("--iterations", type=int, default=20000, help="Number of iterations")
    parser.add_argument("--temperature", type=float, default=1.0, help="Initial temperature")
    
    # parse the arguments
    args = parser.parse_args()

    # initialize timetable
    timetable = Timetable()
    timetable.generate_initial_timetable()
    experiment = Experiment(timetable, args.experiment_iters)
    
    # ------------------------------------------------------- Randomize -----------------------------------------------------------
    if args.algorithm == "Randomize" :
        randomize_summary = experiment.run(Randomize, args.output_file_path)
        print("Randomize Summary", randomize_summary)
        print("Malus per cat", experiment.malus_per_cat)



    # ----------------------------------------------------- Hill Climber ----------------------------------------------------------
    if args.algorithm == "HillClimber":
        hill_climber_summary = experiment.run(HillClimber, args.output_file_path, verbose=True, verbose_alg=False,
                                                swaps_per_neighbour=args.swaps, iterations= args.iterations)
        print("Hill Climber Summary:", hill_climber_summary)
        print("Malus per cat", experiment.malus_per_cat)



    # -------------------------------------------------- Genetic Hill Climber -----------------------------------------------------
    if args.algorithm == "GeneticHillClimber":

        genetic_hill_climber_summary = experiment.run_algorithm(GeneticHillClimber, args.output_file_path, verbose=True, verbose_alg=False, 
                                                   neighbours=args.neighbours, swaps_per_neighbour=args.swaps, 
                                                   iterations=args.iterations)
        print("Genetic Hill Climber Summary:", genetic_hill_climber_summary)
        print("Malus per cat", experiment.malus_per_cat)



    # --------------------------------------------------- Simulated Annealing -----------------------------------------------------
    if args.algorithm == "SimulatedAnnealing":
        sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, args.output_file_path, verbose=True, verbose_alg=False, 
                                                   swaps_per_neighbour=args.swaps, iterations=args.iterations, temperature=args.temperature)
        print("Simulated Annealing Summary:", sim_ann_summary)
        print("Malus per cat", experiment.malus_per_cat)



    # ------------------------------------------------- Genetic Simulated Annealing -----------------------------------------------
    if args.algorithm == "GeneticSimulatedAnnealing":
        genetic_sim_ann_summary = experiment.run_algorithm(GeneticSimulatedAnnealing, args.output_file_path, verbose=True, verbose_alg=False, 
                                                   neighbours=args.neighbours, swaps_per_neighbour=args.swaps, 
                                                   iterations=args.iterations, temperature=args.temperature)
        print("Genetic Simulated Annealing Summary:", genetic_sim_ann_summary)
        print("Malus per cat", experiment.malus_per_cat)



    # # ---------------------------------- Format for loading in timetable and exporting to csv ---------------------------------
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
        
    # print(malus_df)
        
    # plot_experiment_results(malus_df, 'neighbours_and_swaps')

    # ---------------------------------------------------------- Experiment loader -----------------------------------------------------------------
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

    
    # timetable_29 = load_pickle_data('results/pickle_files/conflict_test/29_malus_SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__best_timetable.pkl')
    # for student in timetable_29.full_student_list:
    #     for course, course_activities in student.pers_activities.items():
    #         for activity in course_activities:
    #             student.fill_pers_timetable(activity)
    
    # print(calculate_malus(timetable_29))
    # [0]

    timetable = Timetable()
    timetable.generate_initial_timetable()

    print(calculate_malus(timetable))
    

    
    randomize = Randomize(timetable)

    randomize.randomize()
    print(calculate_malus(randomize.timetable))
    randomize.randomize()
    print(calculate_malus(randomize.timetable))
    hill_climber = GeneticSimulatedAnnealing(timetable)
    hill_climber.run(9, 20, 20000, verbose_alg=True, heuristic=True)
    print(hill_climber.timetable.full_student_list[0].pers_timetable)
    print(hill_climber.timetable.full_student_list[0])
    print(hill_climber.timetable.full_student_list[0].pers_activities)

    # print(len(timetable.activity_list))
    # for student in hill_climber.timetable.full_student_list:
    #     p
    #     for course, course_activities in student.pers_activities.items():
    #         for activity in course_activities:
    #             student.fill_pers_timetable(activity)
    # print(calculate_malus(hill_climber.timetable))
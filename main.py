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



if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    # parser= argparse.ArgumentParser(description="Run algorithm with custom parameters.")

    # # type of algorithm and output_file_path
    # parser.add_argument("algorithm", type=str, 
    #                     choices=["Randomize", "HillClimber","GeneticHillClimber","SimulatedAnnealing","GeneticSimulatedAnnealing"], 
    #                     help="Algorithm to run (Randomize, (Genetic) HillClimber or (Genetic) SimulatedAnnealing)")
    # parser.add_argument("output_file_path", type=str, help="Creates a new output_file_path")

    # # experiment parameters
    # parser.add_argument("--experiment_iters", type=int, default=20, help="Number of iters the experiment should run")
    # parser.add_argument("--heur", type=bool, default=True, help="Apply heuristic of decreasing swaps")
    # parser.add_argument("--neighbours", type=int, default=8, help="Number of neighbours")
    # parser.add_argument("--swaps", type=int, default=10, help="Number of swaps per neighbour")
    # parser.add_argument("--iterations", type=int, default=20000, help="Number of iterations")
    # parser.add_argument("--temperature", type=float, default=1.0, help="Initial temperature")
    
    # # parse the arguments
    # args = parser.parse_args()

    # # initialize timetable
    # timetable = Timetable()
    # timetable.generate_initial_timetable()
    # experiment = Experiment(timetable, args.experiment_iters)
    
    # # ------------------------------------------------------- Randomize -----------------------------------------------------------
    # if args.algorithm == "Randomize" :
    #     randomize_summary = experiment.run_algorithm(Randomize, args.output_file_path)
    #     print("Randomize Summary", randomize_summary)
    #     print("Malus per cat", experiment.malus_per_cat)



    # # ----------------------------------------------------- Hill Climber ----------------------------------------------------------
    # if args.algorithm == "HillClimber":
    #     hill_climber_summary = experiment.run_algorithm(HillClimber, args.output_file_path, verbose=True, verbose_alg=False,
    #                                             heuristic=args.heur, number_of_swaps=args.swaps, iterations= args.iterations)
    #     print("Hill Climber Summary:", hill_climber_summary)
    #     print("Malus per cat", experiment.malus_per_cat)



    # # -------------------------------------------------- Genetic Hill Climber -----------------------------------------------------
    # if args.algorithm == "GeneticHillClimber":

    #     genetic_hill_climber_summary = experiment.run_algorithm(GeneticHillClimber, args.output_file_path, verbose=True, verbose_alg=False, 
    #                                                heuristic=args.heur, neighbours=args.neighbours, swaps_per_neighbour=args.swaps, 
    #                                                iterations=args.iterations)
    #     print("Genetic Hill Climber Summary:", genetic_hill_climber_summary)
    #     print("Malus per cat", experiment.malus_per_cat)



    # # --------------------------------------------------- Simulated Annealing -----------------------------------------------------
    # if args.algorithm == "SimulatedAnnealing":
    #     sim_ann_summary = experiment.run_algorithm(SimulatedAnnealing, args.output_file_path, verbose=True, verbose_alg=False, 
    #                                                heuristic=args.heur, number_of_swaps=args.swaps, iterations=args.iterations, temperature=args.temperature)
    #     print("Simulated Annealing Summary:", sim_ann_summary)
    #     print("Malus per cat", experiment.malus_per_cat)



    # # ------------------------------------------------- Genetic Simulated Annealing -----------------------------------------------
    # if args.algorithm == "GeneticSimulatedAnnealing":
    #     genetic_sim_ann_summary = experiment.run_algorithm(GeneticSimulatedAnnealing, args.output_file_path, verbose=True, verbose_alg=False, 
    #                                                heuristic=args.heur, neighbours=args.neighbours, swaps_per_neighbour=args.swaps, 
    #                                                iterations=args.iterations, temperature=args.temperature)
    #     print("Genetic Simulated Annealing Summary:", genetic_sim_ann_summary)
    #     print("Malus per cat", experiment.malus_per_cat)


    # ---------------------------------------------- Plot different neighbours against swaps ------------------------------------
    # -- Genetic Hill Climber --
    file_paths_hc = [
        "results/pickle_files/for_real/GeneticHillClimber_True_heuristic_3_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticHillClimber_True_heuristic_5_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticHillClimber_True_heuristic_7_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticHillClimber_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
        "results/pickle_files/for_real/wouter_runs/GeneticHillClimber_True_heuristic_15_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
        "results/pickle_files/for_real/wouter_runs/GeneticHillClimber_True_heuristic_20_neighbours_10_swaps_per_neighbour_20000_iterations__experiment_instance.pkl",
    ]

    malus_df_hc = load_experiment_data(file_paths_hc)
        
    print(malus_df_hc)
        
    plot_experiment_results(malus_df_hc, 'Genetic Hill Climber with Iterations = 20.000', output_file_name='results/plots/neighbours_exp_ghc', export=True)

    # -- Genetic Simulated Annealing --
    file_paths_sa = [
        "results/pickle_files/for_real/GeneticSimulatedAnnealing_True_heuristic_3_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticSimulatedAnnealing_True_heuristic_5_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticSimulatedAnnealing_True_heuristic_7_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
        "results/pickle_files/for_real/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
        "results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_15_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
        "results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_20_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
    ]

    malus_df_sa = load_experiment_data(file_paths_sa)
        
    print(malus_df_sa)
        
    plot_experiment_results(malus_df_sa, suptitle='Genetic Simulated Annealing with Temperature = 1 and Iterations = 20.000',output_file_name='results/plots/neighbours_exp_gsa', export=True)



    # ---------------------------------------------------------- Experiment loader -----------------------------------------------------------------
    # low_malus_timetable = load_pickle_data('results/pickle_files/for_real/29_malus_SimulatedAnnealing_8_neighbours__3_swaps_per_neighbour_20000_iterations__best_timetable.pkl')
    # timetable_to_csv(low_malus_timetable, 'best_timetable_29_malus')

    # ---------------------------------- Format for loading in timetable and exporting to csv ---------------------------------
    # input_file_path = 'results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=10.0_best_timetable.pkl'
    # stored_timetable = load_pickle_data(input_file_path)

    # output_file_path = 'results/best_timetable_data/best_timetable'
    # timetable_to_csv(stored_timetable, output_file_path)




    # --------------------------------------------------------- Export to html file ----------------------------------------------------------------
    # input_csv = "results/best_timetable_data/best_timetable.csv"
    # output_name = 'results/best_timetable_data/best_timetable.html'
    # pivot = visualize_timetable(input_csv)
    # save_timetable_to_html(pivot, output_name)



    # ------------------------------------------------ Plot temperature of different SA experiments ------------------------------------------------
    # plot for temps
    # file_paths_temps = ["results/pickle_files/for_real/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=1.0_experiment_instance.pkl",
    #                      "results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=5.0_experiment_instance.pkl",
    #                       "results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=10.0_experiment_instance.pkl",
    #                         "results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=50.0_experiment_instance.pkl"]

    # plot_temperature(file_paths_temps, output_file_name= 'results/plots/temperature_exp', export=True)

    

    # ---------------------------------------------------------------- Plot Bar Chart -------------------------------------------------------------
    # best_timetable = load_pickle_data("results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=10.0_best_timetable.pkl")
    # barplot_malus_per_category(best_timetable, info= 'Iterations = 20.000, Neighbours = 9, Swaps = 10, Temperature = 10', export=True, output_file_name='results/plots/best_timetable_malus_cat_bar')


    # ------------------------------------------------------ Plot single iteration distribution ---------------------------------------------------
    # best_experiment= load_pickle_data("results/pickle_files/for_real/wouter_runs/GeneticSimulatedAnnealing_True_heuristic_9_neighbours_10_swaps_per_neighbour_20000_iterations__Temp=10.0_experiment_instance.pkl")
    # print(best_experiment.results)
    # plot_malus_iter(2, best_experiment.indiv_scores, output_file_name='results/plots/best_timetable_malus_per_iter', export=True)
    
  
    malus_point_list = get_scores('results/pickle_files/for_real/2/HillClimber_True_heuristic_10_number_of_swaps_20000_iterations__Results.csv')
    plot_malus_histogram(malus_point_list, output_file_name='results/plots/HC_10S_heur_TRUE', bins='auto', info='Starting swaps: 10, Iterations: 20000, N=20', export=True, suptitle='Histogram of Malus Points - Hill Climber', binwidth=None)
from code.algorithms.randomize import randomize
from code.algorithms.malus import *


import csv
import pickle
import copy

class Experiment():
    """
    This class experiments by running an algorithm on a timetable for a given number of iterations.
    and keeps track of the best timetable, scores, and malus points per category.
    """
    def __init__(self, timetable, iterations):
        self.timetable = timetable
        self.iterations = iterations
        self.results = []
        self.indiv_scores = []

        # initialize with none and inf to be sure the first timetable always overwrites the variables
        self.best_timetable = None
        self.best_score = float('inf')
        
    
    def run_algorithm(self, algorithm_class, folder_path='data/', file_name_addition = '', verbose = False, **algorithm_params):
        """
        This method runs a given algorithm for a number of iterations in experiment. Parameters are:
        output_file name: A name for the pickle file where the best timetable is stored in
        algorithm_class: The class of the algorithm to run
        algorithm_params: Parameters to pass to the algorithms run method.
        """
        self.results = []  
        self.malus_per_cat = {'capacity': 0, 'evening':  0, 'indiv_confl': 0, 'gap_hours': 0}

        # create a format for output file name based on the algorithm params
        params_string = '_'.join(f"{key}_{value}" for key, value in algorithm_params.items() if key != 'verbose_alg')
        self.output_file_name = f'{folder_path}{algorithm_class.__name__}_{params_string}_{file_name_addition}'
        
        
        for iter in range(self.iterations):

            # create a randomized starting timetable before running the algorithm
            randomized_timetable = randomize(self.timetable)
            algorithm = algorithm_class(randomized_timetable)
            score = algorithm.run(**algorithm_params)

            # add a dictionary to the list with malus points per iteration for each algorithm run
            self.indiv_scores.append(algorithm.iteration_values)

            # save the result for this iteration
            self.results.append({"iteration": iter, "score": score})

            # check if this score is better
            if score < self.best_score:
                self.best_score = score
                self.best_timetable = copy.deepcopy(algorithm.timetable)


                # save the best timetable to a file
                with open(f'{self.output_file_name}_best_timetable.pkl', "wb") as f:
                    pickle.dump(self.best_timetable, f)
                if verbose:
                    print(f"New best timetable saved at score {score}")
            
            # calculate the malus points per category for this timetable and add to the total dictionary
            self.malus_per_cat['capacity'] += check_capacity(algorithm.timetable)
            self.malus_per_cat['evening'] += check_evening_slot(algorithm.timetable)
            self.malus_per_cat['indiv_confl'] += check_individual_conflicts(algorithm.timetable)
            self.malus_per_cat['gap_hours'] += check_gap_hours(algorithm.timetable)

            # be sure to save all timetables for analyzing
            with open(f'{self.output_file_name}_results.pkl', "ab") as f:
                pickle.dump(self.results, f)
            if verbose:
                print(f"Result saved at score {score}")
                print(f"Iteration {iter}: Score = {score}")
            
            ### check
            with open(f'{self.output_file_name}_experiment_info.pkl', "wb") as f:
                pickle.dump(self.indiv_scores, f)
            ### check
            ### dubbel check

        # calculate the average malus points per category
        for cat in self.malus_per_cat.keys():
            self.malus_per_cat[cat] = self.malus_per_cat.get(cat) / self.iterations
        
        
        

        # generate summary statistics for every experiment iteration
        scores = [result["score"] for result in self.results]
        summary = {"best_score": self.best_score,
                    "average_score": sum(scores) / len(scores),
                    "all_scores": scores}
        self.export_results()

        return summary



    def export_results(self):
        with open (f'{self.output_file_name}_Results.csv', "a", newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.results)

from code.algorithms.randomize import randomize
from code.algorithms.malus import *
from collections import defaultdict
import os
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
        
    
    def run_algorithm(self, algorithm_class, folder_path='data/', file_name_addition = '', verbose = False, temperature=None, **algorithm_params):
        """
        This method runs a given algorithm for a number of iterations in experiment. Parameters are:
        output_file name: A name for the pickle file where the best timetable is stored in
        algorithm_class: The class of the algorithm to run
        algorithm_params: Parameters to pass to the algorithms run method.
        """
        self.results = []  
        
        self.check_folder_existence(folder_path)
        self.alg_params = algorithm_params
        # create a format for output file name based on the algorithm params
        params_string = '_'.join(f"{value}_{key}" for key, value in algorithm_params.items() if key != 'verbose_alg')
        if temperature:
            file_name_addition += f'_Temp={temperature}'
        self.output_file_name = f'{folder_path}{algorithm_class.__name__}_{params_string}_{file_name_addition}'
        self.malus_per_cat_list = []
        self.all_timetables = defaultdict(list)
        for iter in range(self.iterations):

            self.malus_per_cat = {'capacity': 0, 'evening':  0, 'indiv_confl': 0, 'gap_hours': 0}

            # create a randomized starting timetable before running the algorithm
            randomized_timetable = randomize(self.timetable)
            algorithm = algorithm_class(randomized_timetable, temperature=temperature)
            score = algorithm.run(**algorithm_params)
            self.all_timetables[iter].append(algorithm.timetable)
            # add a dictionary to the list with malus points per iteration for each algorithm run
            self.indiv_scores.append(algorithm.iteration_values)

            # save the result for this iterationƒ
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
            
            self.update_total_malus(algorithm)
            # calculate the malus points per category for this timetable and add to the total dictionary
           
            
           
            
            ### check
            with open(f'{self.output_file_name}_experiment_instance.pkl', "wb") as f:
                pickle.dump(self, f)
            ### check
            ### dubbel check
            #### triple check
            if verbose:
               print('Experiment saved!')
        # calculate the average malus points per category
        #self.calculate_average_malus()
        
        

        # generate summary statistics for every experiment iteration
        self.scores = [result["score"] for result in self.results]
        self.summary = {"best_score": self.best_score,
                    "average_score": sum(self.scores) / len(self.scores),
                    "all_scores": self.scores}
        
        with open(f'{self.output_file_name}_experiment_instance.pkl', "wb") as f:
            pickle.dump(self, f)
        
        self.export_results()

        return self.summary

    def export_results(self):
        with open (f'{self.output_file_name}_Results.csv', "a", newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.results)

    def update_total_malus(self, algorithm):
        self.malus_per_cat['capacity'] = check_capacity(algorithm.timetable)
        self.malus_per_cat['evening'] = check_evening_slot(algorithm.timetable)
        self.malus_per_cat['indiv_confl'] = check_individual_conflicts(algorithm.timetable)
        self.malus_per_cat['gap_hours'] = check_gap_hours(algorithm.timetable)
        self.malus_per_cat_list.append(self.malus_per_cat)

    def calculate_average_malus(self):
        """
        This method combines all malus_per_cat_dictionaries into one dictionary
        holding the average malus of all dictionaries together per catgory. 
        """
        total_malus = {}
        
        # calculate total malus per category 
        for malus_dict in self.malus_per_cat_list:
            for cat, value in malus_dict.items():
                total_malus[cat] += value

        # calculate average malus per category 
        for cat in total_malus:
            total_malus[cat] /=  len(self.malus_per_cat_list)

        return total_malus
            

    def check_folder_existence(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  
        
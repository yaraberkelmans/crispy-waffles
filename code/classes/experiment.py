from code.algorithms.randomize import randomize
import csv
import pickle
import copy

class Experiment():
    def __init__(self, timetable, iterations):
        self.timetable = timetable
        self.iterations = iterations
        self.results = []
        self.best_timetable = None
        self.best_score = float('inf')
    
    def run_algorithm(self, output_file_name, algorithm_class, **algorithm_params):
        """
        Run a given algorithm for a number of iterations in experiment. Parameters are:
        output_file name: A name for the pickle file where the best timetable is stored in
        algorithm_class: The class of the algorithm to run
        algorithm_params: Parameters to pass to the algorithms run method.
        """
        self.results = []  

        for iter in range(self.iterations):

            # create a randomized starting timetable before running the algorithm
            randomized_timetable = randomize(self.timetable)
            algorithm = algorithm_class(randomized_timetable)
            score = algorithm.run(**algorithm_params)

            # save the result for this iteration
            self.results.append({"iteration": iter, "score": score})

            # check if this score is better
            if score < self.best_score:
                self.best_score = score
                self.best_timetable = copy.deepcopy(algorithm.timetable)  # Save the timetable

                # save the best timetable to a file
                with open(output_file_name, "wb") as f:
                    pickle.dump(self.best_timetable, f)
                print(f"New best timetable saved at score {score}")

            print(f"Iteration {iter}: Score = {score}")

        # generate summary statistics for every experiment iteration
        scores = [result["score"] for result in self.results]
        summary = {"best_score": self.best_score,
                    "average_score": sum(scores) / len(scores),
                    "all_scores": scores}

        return summary



    def export_results(self):
        with open ('Results.csv', "a", newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.results)
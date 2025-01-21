from code.algorithms.randomize import randomize

class Experiment():
    def __init__(self, timetable, iterations):
        self.timetable = timetable
        self.iterations = iterations

    def run_algorithm(self, algorithm, alg_iters):
        results= []
        for iter in range(self.iterations):
            randomized_timetable = randomize(self.timetable)
            result= algorithm.run(self.timetable, alg_iters)
            results.append(result)

        scores = [res["score"] for res in results]
        summary = {"best_score": max(scores),
                    "average_score": sum(scores) / len(scores),
                    "all_scores": scores}
        
        return summary


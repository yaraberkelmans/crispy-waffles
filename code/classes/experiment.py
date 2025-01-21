class Experiment():
    def __init__(self, timetable, iterations):
        self.timetable = timetable
        self.iterations = iterations

    def run_algorithm(self, algorithm, alg_iters):
        results= []
        for iter in range(self.iterations):
            result= algorithm.run(self.timetable, alg_iters)
            results.append(result)
            

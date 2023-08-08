from Optimization import *
from RASTRIGIN_FUNCTION import *

class RastriginOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -5.12, 5.12)

    def fitness(self, chromosome: list[float]):
        result = rastrigin(chromosome)
        return math.exp(-result)
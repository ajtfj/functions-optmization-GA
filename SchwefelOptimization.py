from Optimization import *
from SCHWEFEL_FUNCTION import *

class SchwefelOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -500, 500)

    def fitness(self, chromosome: list[float]):
        result = schwefel(chromosome)
        return math.exp(-result)
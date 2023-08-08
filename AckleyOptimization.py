from Optimization import *
from ACKLEY_FUNCTION import *

class AckleyOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -32.768, 32.768)

    def fitness(self, chromosome: list[float]):
        result = ackley(chromosome)
        return math.exp(-result)

import math
from Optimization import *
from ROSENBROCK_FUNCTION import *

class RosenbrockOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -5, 10)

    def fitness(self, chromosome: list[float]):
        result = rosenbrock(chromosome)
        return result
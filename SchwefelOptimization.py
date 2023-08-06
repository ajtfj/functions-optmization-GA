from Optimization import *

class RastriginOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -500, 500)
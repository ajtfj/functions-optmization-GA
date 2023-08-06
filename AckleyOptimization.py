from Optimization import *

class AckleyOptimization(Optimization):
    def generate_population(self):
        Optimization.generate_population(self, -32.768, 32.768)

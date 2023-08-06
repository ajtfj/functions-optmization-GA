import random

class Optimization:
    population = []

    def __init__(self, population_size: int, dimension: int):
        self.population_size = population_size
        self.dimension = dimension

    def mutate(self):
        raise Exception("Not implemented")

    def crossover(self):
        raise Exception("Not implemented")
        
    def parents_select(self):
        raise Exception("Not implemented")

    def survivors_select(self):
        raise Exception("Not implemented")
        
    def generate_population(self, min_gene: float, max_gene: float):
        for _ in range(self.population_size):
            chromossome = []
            for _ in range(self.dimension):
                gene = random.uniform(min_gene, max_gene)
                chromossome.append(gene)
            self.population.append(chromossome)

    def fitness(self):
        raise Exception("Not implemented")

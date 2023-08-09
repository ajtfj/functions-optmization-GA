import random

class Optimization:
    population = []

    def __init__(self, population_size: int, dimension: int):
        self.population_size = population_size
        self.dimension = dimension
    def mutate(self, chromosome: list[float]):
        if random.uniform(0,1) > self.mutate_rate:
            return chromosome
        
        start = random.randint(0, len(chromosome) - 2)
        end = random.randint(start + 1, len(chromosome) - 1)
        segment = chromosome[start:end]
        random.shuffle(segment)
        chromosome[start:end] = segment

        return chromosome


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

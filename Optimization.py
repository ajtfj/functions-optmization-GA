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

    def crossover(self, parent_1: list[float], parent_2: list[float]):
        if random.uniform(0,1) > self.crossover_rate:
            return [parent_1, parent_2]

        crossover_point = random.randint(1, len(parent_1) - 1)
        a = random.uniform(0,1)
        offspring_1 = parent_1[:crossover_point] + [
            a * g1 + (1 - a) * g2 
            for g1, g2 in zip(parent_1[crossover_point:], parent_2[crossover_point:])
        ]
        offspring_2 = parent_2[:crossover_point] + [
            a * g2 + (1 - a) * g1 
            for g1, g2 in zip(parent_1[crossover_point:], parent_2[crossover_point:])
        ]

        offspring_1 = self.mutate(offspring_1)
        offspring_2 = self.mutate(offspring_2)

        return [offspring_1, offspring_2]
        
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

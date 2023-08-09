import random

class Optimization:
    population = []
    EPSILON = 1e-6

    def __init__(
        self, 
        population_size: int, 
        dimension: int,
        mutate_rate: float,
        crossover_rate: float,
        gene_mutation_rate: float
    ):
        self.population_size = population_size
        self.dimension = dimension
        self.mutate_rate = mutate_rate
        self.crossover_rate = crossover_rate
        self.gene_mutation_rate = gene_mutation_rate

    def mutate(self, chromosome: list[float]):
        if random.random() > self.mutate_rate:
            return chromosome

        for i in range(len(chromosome)):
            if random.random() > self.gene_mutation_rate:
                continue
            chromosome[i] += random.gauss(0, 1)
            if chromosome[i] < self.gene_lower_bound:
                chromosome[i] = self.gene_lower_bound
            elif chromosome[i] > self.gene_upper_bound:
                chromosome[i] = self.gene_upper_bound
        
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
        
    def parents_select(self, rank: list[tuple[list[float], float, int]]):
        total_fitness = sum([individual[1] for individual in rank])
        probabilities = [individual[1] / total_fitness for individual in rank]
        selected = []
        for _ in range(2):
            pick = random.uniform(0, 1)
            current = 0
            for i, individual in enumerate(rank):
                current += probabilities[i]
                if pick < current:
                    selected.append(individual)
                    break
        return list(map(lambda tup: tup[0], selected))

    def survivors_select(self, offspring: list[list[float]]):
        self.population.extend(offspring)
        rank = self.rank()
        worts = []
        for i in range(len(offspring)):
            worts.append(rank[len(self.population)-1-i][2])
            worts.sort(reverse=True)
        for w in worts:
            self.population.pop(w)
        
    def generate_population(self, min_gene: float, max_gene: float):
        self.population = []
        for _ in range(self.population_size):
            chromossome = []
            for _ in range(self.dimension):
                gene = random.uniform(min_gene, max_gene)
                chromossome.append(gene)
            self.population.append(chromossome)

    def fitness(self):
        raise Exception("Not implemented")
    
    def rank(self):
        sample = self.population[:]

        fitness = [self.fitness(chromosome) for chromosome in sample]
        rank = [list(s) for s in zip(sample, fitness, range(len(sample)))]
        rank.sort(key=lambda item: item[1], reverse=False)

        return rank
    
    def solution(self):
        rank = self.rank()
        if rank[0][1] <= self.EPSILON:
            return rank[0]
from Optimization import Optimization
import numpy as np

def find_solution(optimization: Optimization, evaluations=100000):
    optimization.generate_population()
    population_fitness = optimization.rank()
    solution = optimization.solution()
    best_fitness_history = [population_fitness[0][1]]
    average_fitness_history = [np.mean(list(map(lambda x: x[1], population_fitness)))]

    evaluation = 0
    while solution == None and evaluation < evaluations:
        parents = optimization.parents_select(population_fitness)
        children = []
        children.extend(optimization.crossover(parents[0], parents[1]))
        optimization.survivors_select(children)
        population_fitness = optimization.rank()
        solution = optimization.solution()
        best_fitness_history.append(population_fitness[0][1])
        average_fitness_history.append(np.mean(list(map(lambda x: x[1], population_fitness))))
        evaluation += 1
    
    return evaluation, best_fitness_history, average_fitness_history
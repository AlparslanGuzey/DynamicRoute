import random

def crossover(parent1, parent2, num_drones, max_payload, package_weights):
    crossover_point = random.randint(1, num_drones - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return [offspring1, offspring2]
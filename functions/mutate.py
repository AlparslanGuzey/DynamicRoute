import random
from functions.is_route_valid import is_route_valid

def mutate(chromosome, mutation_rate, max_payload, package_weights):
    mutated_chromosome = []
    for route in chromosome:
        if random.random() < mutation_rate:
            mutated_route = route.copy()
            i, j = random.sample(range(len(mutated_route)), 2)
            mutated_route[i], mutated_route[j] = mutated_route[j], mutated_route[i]

            if is_route_valid(mutated_route, max_payload, package_weights):
                mutated_chromosome.append(mutated_route)
            else:
                mutated_chromosome.append(route)
        else:
            mutated_chromosome.append(route)

    return mutated_chromosome
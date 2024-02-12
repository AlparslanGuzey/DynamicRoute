import random

def generate_clustered_population(num_drones, delivery_points, package_weights, population_size, clusters):
    population = []
    for _ in range(population_size):
        chromosome = [[] for _ in range(num_drones)]
        for point in delivery_points:
            drone = clusters[point - 1]
            chromosome[drone].append(point)
        for route in chromosome:
            route.insert(0, 0)
            route.append(0)
            random.shuffle(route[1:-1])
        population.append(chromosome)
    return population
from functions.cluster_delivery_points import cluster_delivery_points
from functions.generate_clustered_population import generate_clustered_population
from functions.tournament_selection import tournament_selection
from functions.crossover import crossover
from functions.mutate import mutate
from functions.two_opt import two_opt
from functions.calculate_enhanced_fitness import calculate_enhanced_fitness


def enhanced_genetic_algorithm(coordinates, delivery_points, package_weights, num_drones, max_payload, population_size, max_generations, mutation_rate, tournament_size):
    clusters = cluster_delivery_points(coordinates, num_drones)
    population = generate_clustered_population(num_drones, delivery_points, package_weights, population_size, clusters)

    best_solution = None
    best_fitness = float('inf')

    for generation in range(max_generations):
        new_population = []
        for _ in range(len(population) // 2):
            parent1 = tournament_selection(population, tournament_size, coordinates, package_weights, max_payload)
            parent2 = tournament_selection(population, tournament_size, coordinates, package_weights, max_payload)
            offspring1, offspring2 = crossover(parent1, parent2, num_drones, max_payload, package_weights)
            offspring1 = mutate(offspring1, mutation_rate, max_payload, package_weights)
            offspring2 = mutate(offspring2, mutation_rate, max_payload, package_weights)

            for i in range(num_drones):
                if i < len(offspring1):
                    offspring1[i] = two_opt(offspring1[i], coordinates)
                if i < len(offspring2):
                    offspring2[i] = two_opt(offspring2[i], coordinates)

            new_population.extend([offspring1, offspring2])

        population = new_population

        for individual in population:
            fitness = calculate_enhanced_fitness(individual, coordinates, package_weights, max_payload)
            if fitness < best_fitness and fitness != 0:
                best_fitness = fitness
                best_solution = individual

        print(f"Generation Best Fitness: {best_fitness if best_fitness != float('inf') else 'No valid solution'}")

    return best_solution, best_fitness
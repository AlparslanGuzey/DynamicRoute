import random
from functions.calculate_enhanced_fitness import calculate_enhanced_fitness

def tournament_selection(population, tournament_size, coordinates, package_weights, max_payload):
    tournament = random.sample(population, tournament_size)
    best = max(tournament, key=lambda individual: calculate_enhanced_fitness(individual, coordinates, package_weights, max_payload))
    return best
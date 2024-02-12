from functions.calculate_distance import calculate_distance

def calculate_enhanced_fitness(chromosome, coordinates, package_weights, max_payload):
    total_distance = 0
    capacity_penalty = 0
    for route in chromosome:
        route_weight = sum(package_weights[point] for point in route)
        if route_weight > max_payload:
            capacity_penalty += (route_weight - max_payload) ** 2

        if route:
            for i in range(len(route) - 1):
                total_distance += calculate_distance(route[i], route[i + 1], coordinates)
            total_distance += calculate_distance(route[-1], 0, coordinates)

    if total_distance + capacity_penalty == 0:
        return 0

    fitness = 1 / (total_distance + capacity_penalty)
    print(f"Total Distance: {total_distance}, Capacity Penalty: {capacity_penalty}, Fitness: {fitness}")
    return fitness
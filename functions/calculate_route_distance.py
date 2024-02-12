from functions.calculate_distance import calculate_distance

def calculate_route_distance(route, coordinates):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(route[i], route[i + 1], coordinates)
    distance += calculate_distance(route[-1], route[0], coordinates)
    return distance
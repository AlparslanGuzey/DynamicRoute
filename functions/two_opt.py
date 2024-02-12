from functions.calculate_route_distance import calculate_route_distance

def two_opt(route, coordinates):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_route_distance(new_route, coordinates) < calculate_route_distance(best, coordinates):
                    best = new_route
                    improved = True
        route = best
    return best
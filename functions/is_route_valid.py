def is_route_valid(route, max_payload, package_weights):
    if not route or route[0] != 0 or route[-1] != 0:
        return False

    route_weight = sum(package_weights[point] for point in route)
    if route_weight > max_payload:
        return False

    return True
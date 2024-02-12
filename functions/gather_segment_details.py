from functions.calculate_distances import calculate_distances
from functions.calculate_segment_energy import calculate_segment_energy

def gather_segment_details(best_solution, coordinates, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h):
    """
    Gathers detailed segment metrics for plotting purposes.

    Args:
    - best_solution: List of routes, where each route is a list of delivery point indices.
    - coordinates: Dict of delivery point indices to their coordinates.
    - package_weights: Dict of delivery point indices to their package weights.
    - drone_base_weight, rho, A, C_d, g, h: Various parameters for flight dynamics.

    Returns:
    - A list of segment details, where each detail is a dictionary with keys 'payload' and 'epsilon'.
    """
    segment_details = []
    distances = calculate_distances(coordinates)

    for route in best_solution:
        remaining_payload = sum(package_weights[point] for point in route[1:-1])
        for i in range(len(route) - 1):
            start_point, end_point = route[i], route[i + 1]
            payload = remaining_payload
            if end_point != 0:
                remaining_payload -= package_weights[end_point]

            segment_distance = distances[start_point][end_point]
            drone_weight_with_payload = drone_base_weight + payload
            _, _, optimal_speed, epsilon = calculate_segment_energy(m=drone_weight_with_payload, h=h, d=segment_distance, rho=rho, A=A, C_d=C_d, g=g, drone_base_weight=drone_base_weight, max_payload=max_payload)

            segment_details.append({
                'payload': payload,
                'epsilon': epsilon,
                'optimal_speed': optimal_speed  # This is optional, only if you need it for the plot
            })

    return segment_details

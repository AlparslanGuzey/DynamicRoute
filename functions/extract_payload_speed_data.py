from functions.calculate_distances import calculate_distances
from functions.calculate_flight_time_and_energy import calculate_flight_time_and_energy


def extract_payload_speed_data(best_solution, coordinates, package_weights, drone_base_weight, rho, A, C_d, g, h):
    print("Extracting payload and speed data from the best solution...")
    segment_data = []

    for drone_id, route in enumerate(best_solution):
        distances = calculate_distances(coordinates)
        segment_details, _, _, _ = calculate_flight_time_and_energy(
            distances, route, drone_id, package_weights, drone_base_weight, rho, A, C_d, g, h
        )
        for detail in segment_details:
            segment_data.append((detail['payload'], detail['optimal_speed']))

    return segment_data
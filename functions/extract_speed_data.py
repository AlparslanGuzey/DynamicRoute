from functions.calculate_distances import  calculate_distances
from functions.calculate_flight_time_and_energy import calculate_flight_time_and_energy


def extract_speed_data(best_solution, coordinates, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h):
    print("Extracting speed data from the best solution...")
    drone_speeds = {}
    for drone_id, route in enumerate(best_solution):
        distances = calculate_distances(coordinates)
        segment_details, _, _, _ = calculate_flight_time_and_energy(
            distances, route, drone_id, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h
        )
        speeds = [detail['optimal_speed'] for detail in segment_details]
        drone_speeds[f'Drone {drone_id + 1}'] = speeds
    return drone_speeds
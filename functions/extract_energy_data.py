from functions.calculate_flight_time_and_energy import calculate_flight_time_and_energy
from functions.calculate_distances import calculate_distances

def extract_energy_data(best_solution, coordinates, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h):
    print("Extracting energy data from the best solution...")
    drone_energy = {}
    max_segments = 0

    for drone_id, route in enumerate(best_solution):
        distances = calculate_distances(coordinates)
        segment_details, _, _, _ = calculate_flight_time_and_energy(
            distances, route, drone_id, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h
        )
        energies = [detail['energy'] for detail in segment_details]
        drone_energy[f'Drone {drone_id + 1}'] = energies
        max_segments = max(max_segments, len(energies))

    for drone in drone_energy:
        while len(drone_energy[drone]) < max_segments:
            drone_energy[drone].append(0)

    return drone_energy
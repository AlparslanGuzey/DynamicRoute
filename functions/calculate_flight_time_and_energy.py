from functions.calculate_optimal_speed import calculate_optimal_speed
from functions.calculate_segment_energy import calculate_segment_energy

def calculate_flight_time_and_energy(distances, route, drone_id, package_weights, drone_base_weight, max_payload, rho, A, C_d, g=9.81, h=50):
    drone_weight = drone_base_weight
    total_time, total_energy = 0, 0
    segment_details = []
    remaining_payload = sum(package_weights[point] for point in route[1:-1])

    for i in range(len(route) - 1):
        start_point = route[i]
        end_point = route[i + 1]
        segment_distance = distances[start_point][end_point]
        payload = package_weights[end_point] if end_point != 0 else 0
        drone_weight_with_payload = drone_weight + remaining_payload

        # Calculate optimal speed for the current weight
        optimal_speed = calculate_optimal_speed(m=drone_weight_with_payload, A=A, C_d=C_d, rho=rho, drone_base_weight=drone_base_weight, max_payload=max_payload)

        # Calculate time for cruise
        t_cruise = segment_distance / optimal_speed

        # Calculate energy, time, optimal speed, and epsilon for the segment
        energy, _, _, epsilon = calculate_segment_energy(m=drone_weight_with_payload, h=h, d=segment_distance, rho=rho, A=A, C_d=C_d, g=g, drone_base_weight=drone_base_weight, max_payload=max_payload)

        # Time for takeoff and landing (calculated within calculate_segment_energy)
        t_takeoff = h / optimal_speed
        t_landing = h / optimal_speed

        # Total time for the segment
        segment_time = t_cruise + t_takeoff + t_landing

        total_time += segment_time
        total_energy += energy

        segment_details.append({
            'segment': (start_point, end_point),
            'optimal_speed': optimal_speed,
            'epsilon': epsilon,
            'energy': energy,
            'flight_time': segment_time,
            'payload': remaining_payload,
            'package_weight': payload
        })

        if end_point != 0:
            remaining_payload -= payload

    return segment_details, total_time, total_energy, remaining_payload

from functions.calculate_distances import calculate_distances
from functions.calculate_flight_time_and_energy import calculate_flight_time_and_energy
from graphics.export_excel_output import export_excel_output


def display_detailed_metrics(best_solution, coordinates, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h):
    total_mission_energy = 0
    max_subtour_time = 0

    for drone_id, route in enumerate(best_solution):
        distances = calculate_distances(coordinates)
        segment_details, total_subtour_time, total_subtour_energy, _ = calculate_flight_time_and_energy(
            distances, route, drone_id, package_weights, drone_base_weight, max_payload, rho, A, C_d, g, h
        )

        export_excel_output(drone_id, segment_details, total_subtour_time, total_subtour_energy)

        if segment_details:
            print(f"\nDrone {drone_id + 1} Total Load from Depot: {segment_details[0]['payload']} kg")
            for segment_detail in segment_details:
                print(f"  Segment {segment_detail['segment']}:")
                print(f"    Optimal Speed: {segment_detail['optimal_speed']} m/s")
                print(f"    Acceleration Coefficient (Epsilon): {segment_detail['epsilon']}")
                print(f"    Flight Time: {segment_detail['flight_time']}s")
                print(f"    Energy: {segment_detail['energy']}Wh")
                print(f"    Payload: {segment_detail['payload']} kg")
                print(f"    Package Weight: {segment_detail['package_weight']} kg")
            print(f"  Total Subtour Time: {total_subtour_time}s")
            print(f"  Total Subtour Energy: {total_subtour_energy}Wh")

            max_subtour_time = max(max_subtour_time, total_subtour_time)
            total_mission_energy += total_subtour_energy
        else:
            print(f"Drone {drone_id + 1} has no valid route.")

    print(f"\nTotal Mission Time: {max_subtour_time}s")
    print(f"Total Mission Energy: {total_mission_energy}Wh")

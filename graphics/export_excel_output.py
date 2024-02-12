import pandas as pd

def export_excel_output(drone_id, segment_details, total_subtour_time, total_subtour_energy):
    total_mission_energy = 0
    max_subtour_time = 0

    if segment_details:
        drone_name = f"Drone {drone_id + 1}"
        segment_count = len(segment_details)
        drone_start_payload = segment_details[0]['payload']
        segments_data = []

        print(f"\nDrone {drone_id + 1} Total Load from Depot: {segment_details[0]['payload']} kg")
        segment_id = 1
        for segment_detail in segment_details:
            segment = segment_detail['segment']
            optimal_speed = segment_detail['optimal_speed']
            epsilon = segment_detail['epsilon']
            flight_time = segment_detail['flight_time']
            energy = segment_detail['energy']
            payload = segment_detail['payload']
            package_weight = segment_detail['package_weight']
            segments_data.append([segment_id, segment, optimal_speed, epsilon, flight_time, energy, payload, package_weight, total_subtour_time, total_subtour_energy])
            segment_id += 1

        columns = ['Segment', 'Route', 'Optimal Speed', 'Epsilon', 'Flight Time', 'Energy', 'Payload', 'Package Weight', 'Total Subtour Time', 'Total Subtour Energy']
        df = pd.DataFrame(segments_data, columns=columns)

        excel_filename = f"drone_{drone_id + 1}_segments.xlsx"
        df.to_excel(excel_filename, index=False)

        max_subtour_time = max(max_subtour_time, total_subtour_time)
        total_mission_energy += total_subtour_energy

        print(f"Data exported to {excel_filename}")
    else:
        print(f"Drone {drone_id + 1} has no valid route.")

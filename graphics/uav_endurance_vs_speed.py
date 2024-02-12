import matplotlib.pyplot as plt
from functions.calculate_endurance import calculate_endurance

def uav_endurance_vs_speed(payload_range, speed_range, drone_base_weight, battery_capacity):
    plt.figure(figsize=(10, 6))
    for payload in payload_range:
        total_mass = drone_base_weight + payload
        endurances = [calculate_endurance(speed, total_mass, drone_base_weight, battery_capacity) for speed in
                      speed_range]
        plt.plot(speed_range, endurances, label=f'Payload {payload} kg')

    plt.xlabel('UAV Speed (m/s)')
    plt.ylabel('UAV Endurance (seconds)')
    plt.title('UAV Endurance vs Speed for Different Payloads')
    plt.legend()
    plt.grid(True)
    plt.show()
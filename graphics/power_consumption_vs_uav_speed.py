import matplotlib.pyplot as plt
from functions.calculate_power import calculate_power

def power_consumption_vs_uav_speed(payload_range, speed_range, drone_base_weight):
    plt.figure(figsize=(10, 6))
    for payload in payload_range:
        total_mass = drone_base_weight + payload
        powers = [calculate_power(speed, total_mass, drone_base_weight) for speed in speed_range]
        plt.plot(speed_range, powers, label=f'Payload {payload} kg')

    plt.xlabel('Speed (m/s)')
    plt.ylabel('Power Consumption (W)')
    plt.title('Power Consumption vs UAV Speed for Different Payloads')
    plt.legend()
    plt.grid(True)
    plt.show()
import matplotlib.pyplot as plt
from functions.calculate_range import calculate_range
from functions.calculate_endurance import calculate_endurance

def uav_range_vs_speed(payload_range, drone_base_weight, speed_range, battery_capacity):
    plt.figure(figsize=(10, 6))
    for payload in payload_range:
        total_mass = drone_base_weight + payload
        ranges = [calculate_range(speed, calculate_endurance(speed, total_mass, drone_base_weight, battery_capacity))
                  for speed in speed_range]
        plt.plot(speed_range, ranges, label=f'Payload {payload} kg')

    plt.xlabel('UAV Speed (m/s)')
    plt.ylabel('UAV Range (m)')
    plt.title('UAV Range vs Speed for Different Payloads')
    plt.legend()
    plt.grid(True)
    plt.show()
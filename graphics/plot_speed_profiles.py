import matplotlib.pyplot as plt

def plot_speed_profiles(drone_speeds):
    print("Generating combined speed profile line graph for all drones...")

    fig, ax = plt.subplots(figsize=(10, 6))

    for drone, speeds in drone_speeds.items():
        ax.plot(range(len(speeds)), speeds, label=drone, marker='o')  # 'o' for markers on each point

    ax.set_xlabel('Segment')
    ax.set_ylabel('Optimal Speed (m/s)')
    ax.set_title('Optimal Speed for Each Segment by Drone')
    ax.legend()

    plt.grid(True)
    plt.show()
    print("Combined speed profile line graph generated.")

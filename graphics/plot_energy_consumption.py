import matplotlib.pyplot as plt

def plot_energy_consumption(drone_energy):
    print("Generating stacked bar graph for energy consumption per segment...")

    # Create a single plot
    fig, ax = plt.subplots(figsize=(10, 6))

    num_segments = max(len(energy) for energy in drone_energy.values())

    bottom_values = [0] * num_segments

    for drone, energies in drone_energy.items():
        ax.bar(range(num_segments), energies, label=drone, bottom=bottom_values)
        bottom_values = [bottom + energy for bottom, energy in zip(bottom_values, energies)]

    ax.set_xlabel('Segment')
    ax.set_ylabel('Energy Consumed (Wh)')
    ax.set_title('Energy Consumption per Segment by Drone')
    ax.set_xticks(range(num_segments))
    ax.set_xticklabels([f'Segment {i+1}' for i in range(num_segments)])
    ax.legend()

    plt.show()
    print("Stacked bar graph for energy consumption generated.")

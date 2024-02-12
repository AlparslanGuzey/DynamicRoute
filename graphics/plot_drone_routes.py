import matplotlib.pyplot as plt

def plot_drone_routes(coordinates, routes, package_weights):
    plt.figure(figsize=(12, 8))

    for point, (x, y) in coordinates.items():
        plt.plot(x, y, 'o')
        label = f'{point} ({package_weights[point]}kg)' if point != 0 else 'Depot'
        plt.text(x, y, label, fontsize=9, ha='right')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    color_legend = {}

    for drone_id, route in enumerate(routes):
        color = colors[drone_id % len(colors)]
        color_legend[f'Drone {drone_id + 1}'] = color

        for i in range(len(route) - 1):
            start_point = route[i]
            end_point = route[i + 1]
            start_x, start_y = coordinates[start_point]
            end_x, end_y = coordinates[end_point]

            plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y, color=color,
                      length_includes_head=True, head_width=0.5, head_length=0.5,
                      overhang=0.3, linewidth=1)

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Drone Delivery Routes')

    # Adding legend for drone colors
    custom_lines = [plt.Line2D([0], [0], color=color, lw=2) for color in color_legend.values()]
    plt.legend(custom_lines, color_legend.keys(), loc='upper right')

    plt.grid(True)
    plt.show()
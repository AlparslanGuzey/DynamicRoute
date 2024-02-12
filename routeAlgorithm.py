from functions.enhanced_genetic_algorithm import enhanced_genetic_algorithm
from functions.extract_speed_data import extract_speed_data
from functions.extract_energy_data import extract_energy_data
from functions.extract_payload_speed_data import extract_payload_speed_data
from functions.extract_payload_epsilon_data import extract_payload_epsilon_data
from functions.gather_segment_details import gather_segment_details

from graphics.uav_range_vs_speed import uav_range_vs_speed
from graphics.display_detailed_metrics import display_detailed_metrics
from graphics.plot_drone_routes import plot_drone_routes
from graphics.plot_speed_profiles import plot_speed_profiles
from graphics.plot_energy_consumption import plot_energy_consumption
from graphics.plot_payload_vs_speed import plot_payload_vs_speed
from graphics.power_consumption_vs_uav_speed import power_consumption_vs_uav_speed
from graphics.uav_endurance_vs_speed import uav_endurance_vs_speed
from graphics.plot_payload_vs_epsilon import plot_payload_vs_epsilon


def routeAlgorithm(num_points, num_drones, max_payload, drone_base_weight, A, h, coordinates, package_weights, payload_range, speed_range, battery_capacity, rho=1.225,
                   C_d=1, g=9.81, population_size=50, max_generations=100, mutation_rate=0.1, tournament_size=5):
    """
        Solves a drone routing problem to optimize delivery routes for a fleet of drones.

        - num_points (int): Number of delivery points including the depot.
        - num_drones (int): Number of drones available for deliveries.
        - max_payload (float): Maximum payload capacity of each drone in kilograms.
        - drone_base_weight (float): Base weight of each drone in kilograms.
        - A (float): Wing area of the drones in square meters.
        - h (float): Height for takeoff and landing in meters.
        - coordinates (dict): Dictionary mapping delivery points to their respective (x, y) coordinates.
        - package_weights (dict): Dictionary specifying the weights of packages at each delivery point.
        - rho (float, optional): Air density in kg/m^3 (default is 1.225).
        - C_d (float, optional): Drag coefficient (default is 1).
        - g (float, optional): Gravitational acceleration in m/s^2 (default is 9.81).
        - population_size (int, optional): Size of the genetic algorithm population (default is 50).
        - max_generations (int, optional): Maximum number of generations for the genetic algorithm (default is 100).
        - mutation_rate (float, optional): Rate of mutation for genetic algorithm individuals (default is 0.1).
        - tournament_size (int, optional): Size of the tournament selection for genetic algorithm (default is 5).

        Note: The function uses a genetic algorithm approach to find optimal routes, considering drone constraints
        such as payload capacity and aerodynamic parameters.
    """

    settings = {
        "num_points": num_points,  # Number of delivery points including the depot
        "num_drones": num_drones,
        "max_payload": max_payload,  # (KG)
        "payload_range": payload_range,
        "speed_range": speed_range,
        "drone_base_weight": drone_base_weight,  # (KG)
        "battery_capacity": battery_capacity,
        "rho": rho,  # Air density (kg/m^3)
        "C_d": C_d,  # Drag coefficient
        "A": A,  # Wing area (m^2)
        "g": g,  # Gravitational acceleration (m/s^2)
        "h": h,  # Height for takeoff and landing in meters
        "coordinates": coordinates,
        "package_weights": package_weights,
        "ga_params": {
            "population_size": population_size,
            "max_generations": max_generations,
            "mutation_rate": mutation_rate,
            "tournament_size": tournament_size
        }
    }

    delivery_points = list(range(1, settings['num_points']))


    # Run the Enhanced GA
    best_solution, best_fitness = enhanced_genetic_algorithm(
        settings['coordinates'], delivery_points, settings['package_weights'], settings['num_drones'], settings['max_payload'],
        settings['ga_params']['population_size'], settings['ga_params']['max_generations'], settings['ga_params']['mutation_rate'], settings['ga_params']['tournament_size']
    )

    # Display detailed metrics and plot routes
    if best_solution is not None:
        display_detailed_metrics(best_solution, settings['coordinates'], settings['package_weights'], settings['drone_base_weight'], settings['max_payload'], settings['rho'], settings['A'], settings['C_d'], settings['g'], settings['h'])
        plot_drone_routes(settings['coordinates'], best_solution, settings['package_weights'])

        # Extract and plot speed data
        drone_speeds = extract_speed_data(best_solution, settings['coordinates'], settings['package_weights'], settings['drone_base_weight'], settings['max_payload'], settings['rho'], settings['A'], settings['C_d'], settings['g'], settings['h'])
        plot_speed_profiles(drone_speeds)

        # Extract and plot energy data
        drone_energy = extract_energy_data(best_solution, settings['coordinates'], settings['package_weights'], settings['drone_base_weight'], settings['max_payload'], settings['rho'], settings['A'], settings['C_d'],
                          settings['g'], settings['h'])
        plot_energy_consumption(drone_energy)

        # Extract data for Payload vs. Speed plot
        segment_data = extract_payload_speed_data(best_solution, settings['coordinates'], settings['package_weights'], settings['drone_base_weight'], settings['rho'], settings['A'], settings['C_d'],
                          settings['g'], settings['h'])
        plot_payload_vs_speed(segment_data)

        segment_details = gather_segment_details(best_solution, settings['coordinates'], settings['package_weights'], settings['drone_base_weight'], settings['max_payload'], settings['rho'], settings['A'], settings['C_d'],
                          settings['g'], settings['h'])
        payloads, epsilons = extract_payload_epsilon_data(segment_details)
        plot_payload_vs_epsilon(payloads, epsilons)

        # Plotting Power Consumption vs UAV Speed
        power_consumption_vs_uav_speed(settings['payload_range'], settings["speed_range"], settings["drone_base_weight"])

        # Plotting UAV Endurance vs Speed
        uav_endurance_vs_speed(settings['payload_range'], settings["speed_range"], settings["drone_base_weight"], settings["battery_capacity"])

        # Plotting UAV Range vs Speed
        uav_range_vs_speed(settings["payload_range"], settings["drone_base_weight"], settings["speed_range"], settings["battery_capacity"])
    else:
        print("No valid solution found.")

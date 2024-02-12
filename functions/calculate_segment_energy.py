from functions.calculate_optimal_speed import calculate_optimal_speed
import math


def calculate_segment_energy(m, h, d, rho, A, C_d, drone_base_weight, max_payload, g=9.81, min_speed=5, max_speed=15):
    optimal_speed = calculate_optimal_speed(m, A, C_d, rho, drone_base_weight=drone_base_weight, max_payload=max_payload, base_min_speed=min_speed, base_max_speed=max_speed)
    t_takeoff = h / optimal_speed
    t_landing = h / optimal_speed
    epsilon = 4 * h / t_takeoff**2

    # Power during takeoff
    P_takeoff = math.sqrt((m * (g + epsilon)) ** 3 / (2 * rho * A))
    E_takeoff = P_takeoff * t_takeoff

    # Time for cruise
    t_cruise = d / optimal_speed

    # Power during cruise (now includes hovering power and power to overcome drag)
    P_hover = math.sqrt((m * g) ** 3 / (2 * rho * A))
    P_drag = 0.5 * C_d * rho * A * optimal_speed**2
    P_cruise = P_hover + P_drag

    # Energy during cruise
    E_cruise = P_cruise * t_cruise

    # Energy during landing (assumed same as takeoff)
    E_landing = E_takeoff

    # Total energy for the segment
    E_segment = E_takeoff + E_cruise + E_landing

    # Convert energy to Watt-hours
    E_segment_Wh = E_segment / 3600

    return E_segment_Wh, t_cruise, optimal_speed, epsilon
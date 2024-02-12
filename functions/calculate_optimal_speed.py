import numpy as np

def calculate_optimal_speed(m, A, C_d, rho, drone_base_weight, max_payload, g=9.81, base_min_speed=40, base_max_speed=60):
    weight_factor = m / (drone_base_weight + max_payload)
    min_speed = base_min_speed * weight_factor
    max_speed = base_max_speed * weight_factor

    def power_required(speed):
        drag_force = 0.5 * rho * C_d * A * speed**2
        power_for_drag = drag_force * speed
        power_for_lift = m * g * speed
        return power_for_drag + power_for_lift

    speeds = np.linspace(min_speed, max_speed, 200)
    optimal_speed = min(speeds, key=power_required)
    return optimal_speed
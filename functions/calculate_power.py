def calculate_power(speed, total_mass, drone_base_weight):
    base_power_values = {5: 20, 10: 50, 15: 100, 20: 200}
    base_power = base_power_values.get(total_mass - drone_base_weight, 400)
    power = base_power * (speed / 5) ** 2

    return power
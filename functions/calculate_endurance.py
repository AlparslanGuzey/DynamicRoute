from functions.calculate_power import calculate_power


def calculate_endurance(speed, total_mass, drone_base_weight, battery_capacity):
    power = calculate_power(speed, total_mass, drone_base_weight)
    if power > 0:
        return battery_capacity / power
    else:
        return 0
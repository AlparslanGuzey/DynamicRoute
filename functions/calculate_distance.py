def calculate_distance(point1, point2, coordinates):
    return ((coordinates[point1][0] - coordinates[point2][0]) ** 2 + (coordinates[point1][1] - coordinates[point2][1]) ** 2) ** 0.5
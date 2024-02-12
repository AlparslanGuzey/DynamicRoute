import numpy as np

def calculate_distances(coordinates):
    num_points = len(coordinates)
    distances = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(num_points):
            distances[i][j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))
    return distances
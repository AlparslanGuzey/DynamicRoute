import numpy as np
from sklearn.cluster import KMeans

def cluster_delivery_points(coordinates, num_drones):
    points = np.array([coordinates[i] for i in range(1, len(coordinates))])
    kmeans = KMeans(n_clusters=num_drones, random_state=0).fit(points)
    clusters = kmeans.labels_
    return clusters
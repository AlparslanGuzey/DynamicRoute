# Route Algorithm
This library created for finding optimal routes by drones using efficiency of power, flight route and package weights. This module cannot be used without permission!

 ## Example Usage

```python
from routeAlgorithm import routeAlgorithm
import numpy as np

coordinates = {
    0: (342, 598), 1: (200, 900), 2: (120, 300), 3: (250, 990),
    4: (300, 700), 5: (350, 500), 6: (400, 400), 7: (900, 150),
    8: (600, 600), 9: (900, 100), 10: (550, 850)
}

package_weights = {
    0: 0,  # Depot
    1: 5, 2: 10, 3: 15, 4: 10, 5: 20, 6: 5, 7: 10, 8: 15, 9: 5, 10: 10
}

payload_range = [5, 10, 15, 20]
speed_range = np.linspace(5, 40, 8)

routeAlgorithm(
    num_points=11,
    num_drones=4,
    max_payload=40,
    drone_base_weight=5,
    A=2,
    h=50,
    coordinates=coordinates,
    package_weights=package_weights,
    payload_range=payload_range,
    speed_range=speed_range,
    battery_capacity=1000
)
```

## How to create coordinates?
Coordinates are managed by tuple lists. The first point must be the depot. Drone always returns to depot. 
```python
coordinates = {
    0:(x, y), # Depot
    1:(x_1,y_1), # Point
    2:(x_2,y_2), # Point
    3:(x_3,y_3), # Point
    4:(x_4,y_4), # Point
}
```

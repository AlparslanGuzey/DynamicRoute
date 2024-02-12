import matplotlib.pyplot as plt
import numpy as np


def plot_payload_vs_epsilon(payloads, epsilons):
    plt.figure(figsize=(10, 6))
    plt.scatter(payloads, epsilons, color='blue', alpha=0.7, edgecolors='black', s=100)

    degree = 2
    coeffs = np.polyfit(payloads, epsilons, degree)
    polynomial = np.poly1d(coeffs)

    x_values = np.linspace(min(payloads), max(payloads), 100)
    y_values = polynomial(x_values)

    plt.plot(x_values, y_values, "r--", label='Non-linear Fit')

    plt.title('Drone Payload vs. Acceleration Coefficient (Epsilon)')
    plt.xlabel('Payload (kg)')
    plt.ylabel('Acceleration Coefficient (Epsilon)')
    plt.legend()
    plt.grid(True)
    plt.show()
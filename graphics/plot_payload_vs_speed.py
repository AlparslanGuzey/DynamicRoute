import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def plot_payload_vs_speed(segment_data):
    print("Generating scatter plot for Payload vs. Optimal Speed...")

    payloads, speeds = zip(*sorted(segment_data))

    unique_payloads = np.unique(payloads)
    avg_speeds = [np.mean([speed for p, speed in zip(payloads, speeds) if p == up]) for up in unique_payloads]

    plt.figure(figsize=(10, 6))
    plt.scatter(unique_payloads, avg_speeds, alpha=0.7, c='blue', edgecolors='w', s=100)

    try:
        f = interp1d(unique_payloads, avg_speeds, kind='cubic')
        payload_new = np.linspace(min(unique_payloads), max(unique_payloads), 300)
        speed_smooth = f(payload_new)

        plt.plot(payload_new, speed_smooth, 'r-', label='Fitted Curve')
    except Exception as e:
        print("Error during interpolation:", e)
        # Fallback to linear if cubic fails
        f_linear = interp1d(unique_payloads, avg_speeds, kind='linear')
        plt.plot(unique_payloads, f_linear(unique_payloads), 'g--', label='Linear Fit')

    plt.xlabel('Payload (kg)')
    plt.ylabel('Optimal Speed (m/s)')
    plt.title('Payload vs. Optimal Speed for Each Segment')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Scatter plot with curve generated.")
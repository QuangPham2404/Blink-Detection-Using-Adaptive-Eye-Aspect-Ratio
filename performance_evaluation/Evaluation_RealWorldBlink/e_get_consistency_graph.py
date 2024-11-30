import matplotlib.pyplot as plt
import numpy as np
import random

def plot_multiple_y(x, *y_lists):
    """
    Plots multiple y-lists against a single x-list.

    Parameters:
    x (list): List of x-coordinates
    *y_lists: Variable number of y-lists to plot against x
    """
    if not y_lists:
        print("Error: At least one y-list must be provided.")
        return

    for i, y in enumerate(y_lists):
        if len(x) != len(y):
            print(f"Error: The length of x and y[{i}] must be the same.")
            return

    plt.figure(figsize=(10, 6))
    colors = plt.cm.tab10.colors  # Use a colormap for distinct colors

    for idx, y in enumerate(y_lists):
        plt.plot(x, y, marker='o', linestyle='-', color=colors[idx % len(colors)],
                 label=f"y[{idx}]")

    plt.title("Precision of different EAR threshold with 0.01 difference")
    plt.xlabel("EAR Thresholds")
    plt.ylabel("Precision")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
x = [round(0.191 + i * 0.001, 3) for i in range(int((0.209 - 0.191) / 0.001) + 2)]
x = [value for value in x if value <= 0.209]  # Ensure 0.209 is included
print(x)
y_dad = [0.63,
0.56,
0.41,
0.34,
0.32,
0.26,
0.12,
0.07,
0.12,
0.12,
0.22,
0.49,
0.52,
0.52,
0.57,
0.67,
0.82,
0.89,
1]
y_bao = [0.83,
0.76,
0.71,
0.64,
0.65,
0.62,
0.68,
0.33,
0.52,
0.17,
0.07,
0.1,
0.09,
0,
0,
0,
0,
0,
0]
y_nhien = [0.5,
0.4,
0.33,
0.47,
0.53,
0.48,
0.36,
0.23,
0.18,
0.13,
0.12,
0.1,
0.12,
0.18,
0.2,
0.33,
0.36,
0.33,
0.21]
y_quang = [0.93,
0.93,
0.92,
0.93,
0.93,
0.87,
0.78,
0.6,
0.54,
0.3,
0.38,
0.27,
0.33,
0.36,
0.5,
0.45,
0.33,
0.38,
0.36]
y_minh = [0.81,
0.84,
0.87,
0.88,
0.88,
0.86,
0.87,
0.86,
0.88,
0.69,
0.74,
0.64,
0.43,
0.3,
0.23,
0.18,
0.07,
0.04,
0]
y_mom = [0.92,
0.92,
0.92,
0.92,
0.89,
0.82,
0.86,
0.84,
0.83,
0.67,
0.66,
0.65,
0.46,
0.26,
0.1,
0.03,
0.03,
0.03,
0]

plot_multiple_y(x,y_dad,y_bao,y_nhien,y_quang,y_minh,y_mom)

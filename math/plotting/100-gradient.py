#!/usr/bin/env python3
"""Create scatter plot of elevation of mountain"""

import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """title Mountain Elevation"""

    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")
    scatter = plt.scatter(x, y, c=z, cmap="viridis")
    cb = plt.colorbar(scatter)
    cb.set_label("elevation (m)")
    plt.show()


gradient()

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

''' plot y as a line graph '''


def line():
    ''' y should be plotted as a solid red line '''
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.xlim(0, 10)
    plt.plot(y, color="red")
    plt.show()


# line()

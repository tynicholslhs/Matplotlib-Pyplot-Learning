import matplotlib.pyplot as plt
import numpy as np

def graph_parabola(a, b, c, xmax = 10, ymax = 10):
    x = np.arange(0, xmax, 0.1)
    plt.plot(x, a * x**2 + b * x + c)
    plt.axis([0, xmax, 0, ymax])
    plt.show

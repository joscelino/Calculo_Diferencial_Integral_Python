import numpy as np


def partial_derivative(f, x: float, y: float, h: float = 0.01):
    return (f(x + h / 2, y + h / 2) - f(x - h / 2, y + h / 2) - f(x + h / 2, y - h / 2) +
            f(x - h / 2, y - h / 2)) / (h ** 2)


f = lambda x, y: x * np.sin(y)

d_partial = partial_derivative(f, 0, np.pi/4)
print(d_partial)
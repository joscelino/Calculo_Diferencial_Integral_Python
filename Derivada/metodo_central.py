import pylab as plt
import numpy as np

y = lambda x: x**2 - 5*x + 6


def derivada_central(f, a: float, h: float = 0.01) -> float:
    return(f(a+h/2) - f(a-h/2)) / h


derivada_central(y, 0)

dy = np.empty(10)

for i in range(0, 10):
    dy[i] = derivada_central(y, i)

for i in range(0, 10):
    plt.plot(i, derivada_central(y, i), 'ro')
plt.show()


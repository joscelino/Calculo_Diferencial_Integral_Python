import numpy as np
import pylab as plt

x = np.linspace(0, 10, 20)
y = x ** 2 - 5 * x + 6
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y, label='F(x) = x^2 - 5x + 6')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.legend()

ax2.fill_between(x, 0, y, label='I(x) = x^3/3 - 5x^2/2 + 6x')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.legend()

plt.show()
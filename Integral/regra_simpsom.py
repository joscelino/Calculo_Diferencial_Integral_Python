from scipy import integrate
import numpy as np

n = 10
a = 0.0
b = 10.0
h = (b-a) / n

x = np.linspace(0, 10, 11)
y = x ** 2 - 5 * x + 6

integer = integrate.simps(y, dx=1)

print(integer)

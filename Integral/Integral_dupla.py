from scipy import integrate
import numpy as np


function_1 = lambda x, y: x * y
integral = integrate.dblquad(function_1, 0, 1, lambda x: 0, lambda x: 1)
print(round(integral[0], 2))
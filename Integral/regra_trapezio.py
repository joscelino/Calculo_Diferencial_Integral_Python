
def y(x: float) -> float:
    return x**2 - 5*x + 6


n = 10000
a = 0.0
b = 10.0
h = (b-a) / n

constant = 0.5 * (y(a) + y(b))

sum_results = 0
for k in range(1, n):
    sum_results += y(a + k * h)

integral = h * (constant + sum_results)
print(integral)

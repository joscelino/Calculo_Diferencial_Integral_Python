
def second_derivative(f, a: int, h: float = 0.01) -> float:
    """ Return the second derivative formula """
    return (f(a+h) - 2 * f(a) + f(a-h)) / (h ** 2)


y = lambda x: x ** 2 - 5 * x + 6

d2 = second_derivative(y, 0)


y = lambda x: x**2 - 5*x + 6


def derivada_avanco(funcao, a, h=0.01):
    return (funcao(a+h) - funcao(a))/h


def derivada_retroceder(funcao, a, h=0.01):
    return (funcao(a) - funcao(a-h))/h

# y'(x) = 2x - 5

derivada_avanco(y, 0)
derivada_retroceder(y, 0)

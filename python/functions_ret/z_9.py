import math


def trigonometric_function(mode, x, n):
    result = 0.0
    for k in range(n + 1):
        if mode == 'sin':
            numerator = (-1) ** k * x ** (2 * k + 1)
            denominator = math.factorial(2 * k + 1)
            term = numerator / denominator
        elif mode == 'cos':
            numerator = (-1) ** k * x ** (2 * k)
            denominator = math.factorial(2 * k)
            term = numerator / denominator
        result += term
    return result
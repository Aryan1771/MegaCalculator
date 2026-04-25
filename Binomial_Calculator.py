from megacalculator.core.calculations import binomial_one_plus_x


def Binomial_Calculator(x: float, n: int) -> float:
    return binomial_one_plus_x(x, n)

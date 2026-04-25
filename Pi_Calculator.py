from megacalculator.core.calculations import pi_leibniz


def Pi_Calculator(iterations: int = 100_000) -> float:
    return pi_leibniz(iterations)

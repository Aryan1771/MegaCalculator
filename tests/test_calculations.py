import math

import pytest

from megacalculator.core.calculations import (
    binomial_one_plus_x,
    digit_parts,
    divide,
    euler_limit,
    evaluate_expression,
    factorial,
    fibonacci,
    is_prime,
    pi_leibniz,
    primes,
    trig_from_angle,
)


def test_basic_expression_and_division() -> None:
    assert evaluate_expression("2+3×4") == 14
    assert evaluate_expression("sqrt(9)+2^3") == 11
    assert divide(8, 2) == 4


def test_divide_by_zero_is_clear() -> None:
    with pytest.raises(ValueError, match="zero"):
        divide(1, 0)


def test_legacy_number_tools() -> None:
    assert factorial(5) == 120
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert primes(5) == [2, 3, 5, 7, 11]
    assert is_prime(29)
    assert digit_parts(2026) == [2, 0, 2, 6]
    assert binomial_one_plus_x(2, 3) == 27


def test_constants_and_trig() -> None:
    assert pi_leibniz(10_000) == pytest.approx(math.pi, abs=0.001)
    assert euler_limit(100_000) == pytest.approx(math.e, rel=0.001)
    assert trig_from_angle("sin", 30) == pytest.approx(0.5)

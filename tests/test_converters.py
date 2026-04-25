import pytest

from megacalculator.core.converters import (
    LENGTH_UNITS,
    calculate_bmi,
    convert_linear,
    convert_number_system,
    convert_temperature,
)


def test_linear_conversion() -> None:
    assert convert_linear(1, "Kilometer", "Meter", LENGTH_UNITS) == 1000
    assert convert_linear(12, "Inch", "Foot", LENGTH_UNITS) == pytest.approx(1)


def test_temperature_conversion() -> None:
    assert convert_temperature(0, "Celsius", "Fahrenheit") == 32
    assert convert_temperature(273.15, "Kelvin", "Celsius") == pytest.approx(0)


def test_bmi() -> None:
    bmi, label = calculate_bmi(70, 175)
    assert bmi == pytest.approx(22.857, rel=0.001)
    assert label == "Normal"


def test_number_system_conversion() -> None:
    assert convert_number_system("FF", 16, 10) == "255"
    assert convert_number_system("10", 10, 2) == "1010"

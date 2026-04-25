from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LinearUnit:
    label: str
    to_base: float


LENGTH_UNITS = {
    "Millimeter": LinearUnit("Millimeter", 0.001),
    "Centimeter": LinearUnit("Centimeter", 0.01),
    "Meter": LinearUnit("Meter", 1.0),
    "Kilometer": LinearUnit("Kilometer", 1000.0),
    "Inch": LinearUnit("Inch", 0.0254),
    "Foot": LinearUnit("Foot", 0.3048),
    "Mile": LinearUnit("Mile", 1609.344),
}

WEIGHT_UNITS = {
    "Milligram": LinearUnit("Milligram", 0.000001),
    "Gram": LinearUnit("Gram", 0.001),
    "Kilogram": LinearUnit("Kilogram", 1.0),
    "Pound": LinearUnit("Pound", 0.45359237),
    "Ounce": LinearUnit("Ounce", 0.028349523125),
}

AREA_UNITS = {
    "Square meter": LinearUnit("Square meter", 1.0),
    "Square kilometer": LinearUnit("Square kilometer", 1_000_000.0),
    "Square foot": LinearUnit("Square foot", 0.09290304),
    "Square inch": LinearUnit("Square inch", 0.00064516),
    "Acre": LinearUnit("Acre", 4046.8564224),
    "Hectare": LinearUnit("Hectare", 10_000.0),
}

SPEED_UNITS = {
    "Meter/second": LinearUnit("Meter/second", 1.0),
    "Kilometer/hour": LinearUnit("Kilometer/hour", 0.2777777778),
    "Mile/hour": LinearUnit("Mile/hour", 0.44704),
    "Knot": LinearUnit("Knot", 0.5144444444),
}

VOLUME_UNITS = {
    "Milliliter": LinearUnit("Milliliter", 0.001),
    "Liter": LinearUnit("Liter", 1.0),
    "Cubic meter": LinearUnit("Cubic meter", 1000.0),
    "Cup": LinearUnit("Cup", 0.2365882365),
    "Gallon": LinearUnit("Gallon", 3.785411784),
}

PRESSURE_UNITS = {
    "Pascal": LinearUnit("Pascal", 1.0),
    "Kilopascal": LinearUnit("Kilopascal", 1000.0),
    "Bar": LinearUnit("Bar", 100000.0),
    "Atmosphere": LinearUnit("Atmosphere", 101325.0),
    "PSI": LinearUnit("PSI", 6894.757293168),
}


def convert_linear(value: float, from_unit: str, to_unit: str, units: dict[str, LinearUnit]) -> float:
    if from_unit not in units or to_unit not in units:
        raise ValueError("Choose valid units.")
    return value * units[from_unit].to_base / units[to_unit].to_base


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Choose a valid temperature unit.")

    if to_unit == "Celsius":
        return celsius
    if to_unit == "Fahrenheit":
        return celsius * 9 / 5 + 32
    if to_unit == "Kelvin":
        return celsius + 273.15
    raise ValueError("Choose a valid temperature unit.")


def calculate_bmi(weight_kg: float, height_cm: float) -> tuple[float, str]:
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    bmi = weight_kg / ((height_cm / 100) ** 2)
    if bmi < 18.5:
        label = "Underweight"
    elif bmi < 25:
        label = "Normal"
    elif bmi < 30:
        label = "Overweight"
    else:
        label = "Obese"
    return bmi, label


def convert_number_system(value: str, from_base: int, to_base: int) -> str:
    if from_base not in (2, 8, 10, 16) or to_base not in (2, 8, 10, 16):
        raise ValueError("Base must be binary, octal, decimal, or hexadecimal.")
    try:
        decimal = int(value.strip(), from_base)
    except ValueError as exc:
        raise ValueError("Value does not match the selected number system.") from exc
    if to_base == 2:
        return bin(decimal)[2:]
    if to_base == 8:
        return oct(decimal)[2:]
    if to_base == 10:
        return str(decimal)
    return hex(decimal)[2:].upper()

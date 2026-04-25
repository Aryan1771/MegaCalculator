from megacalculator.core.converters import convert_temperature


def Temperature_Convertor(value: float, from_unit: str, to_unit: str) -> float:
    return convert_temperature(value, from_unit, to_unit)

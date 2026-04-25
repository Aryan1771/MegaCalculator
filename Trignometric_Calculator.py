from megacalculator.core.calculations import trig_from_angle


def Trignometric_Calculator(function_name: str, angle: float, degrees: bool = True) -> float:
    return trig_from_angle(function_name, angle, degrees)

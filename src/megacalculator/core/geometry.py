import math


def square_area(side: float) -> float:
    _positive(side)
    return side * side


def square_perimeter(side: float) -> float:
    _positive(side)
    return 4 * side


def rectangle_area(length: float, breadth: float) -> float:
    _positive(length, breadth)
    return length * breadth


def rectangle_perimeter(length: float, breadth: float) -> float:
    _positive(length, breadth)
    return 2 * (length + breadth)


def triangle_area(base: float, height: float) -> float:
    _positive(base, height)
    return base * height / 2


def circle_area(radius: float) -> float:
    _positive(radius)
    return math.pi * radius * radius


def circle_circumference(radius: float) -> float:
    _positive(radius)
    return 2 * math.pi * radius


def cube_volume(side: float) -> float:
    _positive(side)
    return side**3


def cube_surface_area(side: float) -> float:
    _positive(side)
    return 6 * side * side


def cuboid_volume(length: float, breadth: float, height: float) -> float:
    _positive(length, breadth, height)
    return length * breadth * height


def cuboid_surface_area(length: float, breadth: float, height: float) -> float:
    _positive(length, breadth, height)
    return 2 * ((length * breadth) + (breadth * height) + (height * length))


def cylinder_volume(radius: float, height: float) -> float:
    _positive(radius, height)
    return math.pi * radius * radius * height


def cone_volume(radius: float, height: float) -> float:
    _positive(radius, height)
    return math.pi * radius * radius * height / 3


def sphere_volume(radius: float) -> float:
    _positive(radius)
    return 4 * math.pi * radius**3 / 3


def hemisphere_volume(radius: float) -> float:
    _positive(radius)
    return 2 * math.pi * radius**3 / 3


def _positive(*values: float) -> None:
    if any(value <= 0 for value in values):
        raise ValueError("Measurements must be greater than zero.")

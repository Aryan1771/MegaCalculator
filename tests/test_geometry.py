import math

import pytest

from megacalculator.core import geometry


def test_2d_geometry() -> None:
    assert geometry.square_area(4) == 16
    assert geometry.rectangle_perimeter(4, 5) == 18
    assert geometry.triangle_area(10, 4) == 20
    assert geometry.circle_area(2) == pytest.approx(math.pi * 4)


def test_3d_geometry() -> None:
    assert geometry.cube_volume(3) == 27
    assert geometry.cuboid_surface_area(2, 3, 4) == 52
    assert geometry.cylinder_volume(2, 3) == pytest.approx(math.pi * 12)
    assert geometry.sphere_volume(3) == pytest.approx(36 * math.pi)

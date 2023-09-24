from src.Circle import Circle
from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(10, 314, 62.8),
                          (5, 78.5, 31.4)])
def test_circle(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == f"Circle {radius}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-4, 24, -20),
                          (0, 0, 0),
                          (-5, 50, 30)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        r = Circle(radius)
        assert r.name == f"Circle {radius}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Circle(5)
    assert r.add_area(s) == 88.5


def test_add_area_negative():
    r = Circle(5)
    s = 5
    assert r.add_area(s) == 15


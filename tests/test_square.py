from src.Square import Square
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_sq(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                        [(-4, 24, -20),
                        (0, 0, 0),
                        (-5, 50, 30)])
def test_sq_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        r = Square(side_a)
        assert r.name == f"Square {side_a}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


def test_add_area():
    r = Square(3)
    s = Circle(5)
    assert r.add_area(s) == 87.5


def test_add_area_negative():
    r = Square(2)
    c = 106
    assert c.add_area(r) == 15


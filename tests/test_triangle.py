from src.Triangle import Triangle
from src.Square import Square
from src.Figure import Figure
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(13, 14, 15, 84, 42),
                          (5, 12, 13, 30, 30)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-4, -6, 106, 24, -20),
                          (0, 0, 0, 0, 0),
                          (-5, 10, -156, 50, 30)])
def test_triangle_negative1(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 6, 1, 24, -20),
                          (2, 7, 10, 0, 0),
                          (1, 10, 156, 50, 30)])
def test_triangle_negative2(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


def test_add_area():
    r = Triangle(13, 14, 15)
    s = Square(5)
    assert r.add_area(s) == 109


def test_add_area_negative():
    r = Triangle(13, 14, 15)
    s = 106
    assert s.add_area(r) == 15


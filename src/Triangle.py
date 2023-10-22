from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        if (side_a + side_b) <= side_c or (side_a + side_c) <= side_b or (side_c + side_b) <= side_a:
            raise ValueError("Triangle doesn't exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        s = self.get_perimeter()/2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

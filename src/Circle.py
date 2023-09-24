from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle")
        self.radius = radius
        self.name = f"Circle {radius}"

    def get_area(self):
        return round((self.radius * self.radius * 3.14), 2)

    def get_perimeter(self):
        return round((2 * self.radius * 3.14), 2)


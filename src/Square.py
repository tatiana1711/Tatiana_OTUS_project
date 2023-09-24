from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Can't create Square")
        super().__init__(side, side)
        self.side_a = side
        self.name = f"Square {side}"


